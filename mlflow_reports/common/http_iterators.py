"""
Iterators for MLflow search methods that handle page token magic for you.

https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_model_versions
https://mlflow.org/docs/latest/rest-api.html#search-modelversions

"""

# ====
# https://github.com/mlflow/mlflow/blob/master/mlflow/store/model_registry/__init__.py

from mlflow.store.model_registry.__init__ import (
    SEARCH_REGISTERED_MODEL_MAX_RESULTS_THRESHOLD # = 1000
    # SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD     # = 200_000 # incorrect value per API call
)
#_SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD = SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD # per API error message: {"error_code": "INVALID_PARAMETER_VALUE", "message": "Invalid max results 200000, should be between 0 and 10000"}}
_SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD = 10_000

#    SEARCH_REGISTERED_MODEL_MAX_RESULTS_DEFAULT = 100
#    SEARCH_MODEL_VERSION_MAX_RESULTS_DEFAULT    = 10000


# ====
# https://github.com/mlflow/mlflow/blob/master/mlflow/store/tracking/__init__.py

from mlflow.store.tracking.__init__ import (
    SEARCH_MAX_RESULTS_THRESHOLD # = 50000
)
#    SEARCH_MAX_RESULTS_DEFAULT = 1000

# ====

from mlflow.store.entities.paged_list import PagedList
from mlflow_reports.common import MlflowReportsException


class BaseIterator():
    """
    Base class to iterate for 'search' methods that return PageList.
    """
    def __init__(self, client, resource, object_name, max_results=None, filter=None, order_by=None, http_method="GET", kwargs=None):
        self.client = client
        self.resource = resource
        self.object_name = object_name
        self.filter = filter
        self.idx = 0
        self.paged_list = None
        self.kwargs = kwargs or {}
        if filter: self.kwargs["filter"] = filter
        if max_results: self.kwargs["max_results"] = max_results
        if order_by: self.kwargs["order_by"] = order_by
        self.http_method = http_method


    def _call_iter(self):
        return self._invoke()

    def _call_next(self):
        return self._invoke(self.paged_list.token)


    def _invoke(self, token=None):
        params = self.kwargs.copy()
        if token: params["page_token"] = token

        # NOTE: https://github.com/mlflow/mlflow/issues/7949
        # Some search endpoints are GET and others are POST :(
        if self.http_method.upper() == "POST":
            rsp = self.client.post(self.resource, params)
        else:
            rsp = self.client.get(self.resource, params)

        # extract the list of objects from the root key of the response
        objects = rsp.get(self.object_name, [])

        next_page_token = rsp.get("next_page_token")
        return PagedList(objects, next_page_token)


    def __iter__(self):
        try:
            self.paged_list = self._call_iter()
        except MlflowReportsException as e:
            print(f"WARNING: Search failed. {e}")
        return self

    def __next__(self):
        if not self.paged_list:
            raise StopIteration
        if self.idx < len(self.paged_list):
            chunk = self.paged_list[self.idx]
            self.idx += 1
            return chunk
        elif self.paged_list.token is None or self.paged_list.token == "":
            raise StopIteration
        else:
            self.paged_list = self._call_next()
            if len(self.paged_list) == 0:
                raise StopIteration
            self.idx = 1
            return self.paged_list[0]


class SearchExperimentsIterator(BaseIterator):
    """
    Usage:
        experiments = SearchExperimentsIterator(client, max_results)
        for experiment in experiments:
            print(experiment)
    """
    def __init__(self, client, view_type=None, max_results=SEARCH_MAX_RESULTS_THRESHOLD, filter=None, order_by=None):
        # NOTE: HACK because of https://github.com/mlflow/mlflow/issues/10819 - 2024-01-14
        # For OSS MLflow, max_results is required for experiments but not for any other search endpoints (:
        if not max_results:
            max_results = 1000  # NOTE: mlflow uses 1000 as default value per mlflow/store/tracking/__init__.py:SEARCH_MAX_RESULTS_DEFAULT = 1000
        kwargs = { "view_type": view_type } if view_type else {}
        super().__init__(client, "experiments/search", "experiments", max_results=max_results, filter=filter, order_by=order_by, kwargs=kwargs)


class SearchRegisteredModelsIterator(BaseIterator):
    """
    Usage:
        models = SearchRegisteredModelsIterator(client, max_results)
        for model in models:
            print(model)
    """
    def __init__(self, client, max_results=SEARCH_REGISTERED_MODEL_MAX_RESULTS_THRESHOLD, filter=None, order_by=None):
        super().__init__(client, "registered-models/search", "registered_models", max_results=max_results, filter=filter, order_by=order_by)


class SearchModelVersionsIterator(BaseIterator):
    """
    Usage:
        versions = SearchModelVersionsIterator(client)
        for vr in versions:
            print(vr)
    """
    def __init__(self, client, max_results=_SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD, filter=None, order_by=None):
        super().__init__(client, "model-versions/search", "model_versions", max_results=max_results, filter=filter, order_by=order_by)


class SearchRunsIterator(BaseIterator):
    def __init__(self, client, experiment_ids, max_results=SEARCH_MAX_RESULTS_THRESHOLD, filter=None, order_by=None, view_type=None):
        if isinstance(experiment_ids,str):
            experiment_ids = [ experiment_ids ]
        kwargs = { "experiment_ids": experiment_ids }
        if view_type:
            kwargs["run_view_type"] = view_type

        super().__init__(client, "runs/search", "runs", max_results=max_results, filter=filter, order_by=order_by, http_method="POST", kwargs=kwargs)


class SearchUcRegisteredModelsIterator(BaseIterator):
    """
    GET /api/2.1/unity-catalog/models
    https://docs.databricks.com/api/workspace/registeredmodels/list
    """
    def __init__(self, uc_mlflow_client, catalog=None, schema=None, max_results=None):
        super().__init__(uc_mlflow_client, "unity-catalog/models", "registered_models", max_results=max_results)
        self.kwargs["catalog_name"] = catalog
        if schema:
            self.kwargs["schema_name"] = schema

#class SearchUcModelVersions(BaseIterator): # TODO
#    """
#    GET /api/2.1/unity-catalog/models/{full_name}/versions
#    https://docs.databricks.com/api/workspace/modelversions/list
#    """
#    def __init__(self, uc_mlflow_client, full_name, max_results=None):


class FeatureTablesIterator(BaseIterator):
    """
    Endpoint: api/2.0/feature-store/feature-tables/search
    """
    def __init__(self, client, max_results=None, filter=None):
        super().__init__(client, "feature-store/feature-tables/search", "feature_tables", max_results=max_results, filter=filter)
