from typing import Optional, Dict, List

from . http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import (
    SearchRegisteredModelsIterator,
    SearchModelVersionsIterator,
    SearchExperimentsIterator,
    SearchRunsIterator
)


class MlflowClient:

    def __init__(self):
        self.client = get_mlflow_client()


    # Registered models

    def get_registered_model(self, model_name: str) -> Dict:
        return self.client.get("registered-models/get", {"name": model_name} )
    
    def search_registered_models(self, filter: Optional[str]=None) -> List:
        return list(SearchRegisteredModelsIterator(self.client, filter=filter))
    

    # Model versions

    def get_model_version(self, model_name: str, version: str) -> Dict:
        return self.client.get("model-versions/get", {"name": model_name, "version": version} )
    
    def search_model_versions(self, filter: Optional[str]=None) -> List:
        return list(SearchModelVersionsIterator(self.client, filter=filter))
    
    def get_model_version_download_uri(self, model_name: str, version: str) -> Dict:
        return self.client.get("model-versions/get-download-uri", {"name": model_name, "version": version} )

    def get_latest_versions(self, model_name: str, version: str) -> List:
        return self.client.get("registered-models/get-latest-versions", {"name": model_name, "version": version} )
    
    def get_transition_requests(self, model_name: str, version: str) -> List:
        return self.client.get("transition-requests/list", {"name": model_name, "version": version} )
    

    # Experiments

    def get_experiment(self, experiment_id: str) -> Dict:
        return self.client.get("experiments/get", {"experiment_id": experiment_id })
    
    def get_experiment_by_name(self, experiment_name: str) -> Dict:
        return self.client.get("experiments/get-by-name", {"experiment_name": experiment_name })
    
    def search_experiments(self, filter: Optional[str]=None, view_type: Optional[str]=None, max_results: Optional[str]=None) -> List:
        return list(SearchExperimentsIterator(self.client, filter=filter, view_type=view_type, max_results=max_results))
    

    # Runs
    
    def get_run(self, run_id: str) -> Dict:
        return self.client.get("runs/get", {"run_id": run_id })
    
    def search_runs(self, experiment_ids: List[str]) -> List:
        return list(SearchRunsIterator(self.client, experiment_ids))
    
    def list_artifacts(self, run_id: str, path: Optional[str]=None) -> List:
        return self.client.get("artifacts/list", {"run_id": run_id, "path": path })

    
    def __repr__(self): 
        return self.client


client = MlflowClient()
