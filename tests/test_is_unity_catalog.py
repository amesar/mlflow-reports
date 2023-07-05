import os
import mlflow
from mlflow_reports.client.http_client import (
    is_unity_catalog,
    get_mlflow_client,
    MlflowHttpClient,
    UnityCatalogHttpClient
)

UC_VALUE = "databricks-uc"


def test_not_set_uc():
    _init()
    assert not is_unity_catalog()

def test_set_MLFLOW_REGISTRY_URI():
    _init()
    os.environ["MLFLOW_REGISTRY_URI"] = UC_VALUE
    assert is_unity_catalog()

def test_set_registry_uri():
    _init()
    mlflow.set_registry_uri(UC_VALUE)
    assert is_unity_catalog()

def test_registry_uri_not_uc():
    _init()
    mlflow.set_registry_uri("databricks")
    assert not is_unity_catalog()


def test_get_mlflow_client_MlflowHttpClient():
    _init()
    client = get_mlflow_client()
    assert isinstance(client, MlflowHttpClient)

def test_get_mlflow_client_UnityCatalogHttpClient():
    _init()
    os.environ["MLFLOW_REGISTRY_URI"] = UC_VALUE
    client = get_mlflow_client()
    assert isinstance(client, UnityCatalogHttpClient)


def _init():
    os.environ.pop("MLFLOW_REGISTRY_URI",None)
    mlflow.set_registry_uri("foo") 
    env_var = os.environ.get("MLFLOW_REGISTRY_URI")
    api_val = mlflow.get_registry_uri()
    assert env_var != UC_VALUE
    assert api_val != UC_VALUE
