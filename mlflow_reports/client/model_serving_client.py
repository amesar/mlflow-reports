# https://docs.databricks.com/api/workspace/servingendpoints

import time
from mlflow_reports.common import MlflowReportsException
from . http_client import dbx_20_client


class ModelServingClient:

    def __init__(self):
        self.client = dbx_20_client

    def get_endpoint(self, endpoint_name):
        return self.client.get(f"serving-endpoints/{endpoint_name}")

    def get_endpoint_openapi_schema(self, endpoint_name):
        return self.client.get(f"serving-endpoints/{endpoint_name}/openapi")

    def list_endpoints(self):
        return self.client.get("serving-endpoints")

    def start_endpoint(self, spec):
        return self.client.post("serving-endpoints", spec)

    def stop_endpoint(self, endpoint_name):
        try:
            self.client.delete(f"serving-endpoints/{endpoint_name}")
            return True
        except MlflowReportsException as e:
            if e.http_status_code != 404:
                raise e
        return False

    def wait_until_ready(self, endpoint_name, max=20, sleep_time=2):
        for i in range(0,max):
            endpoint = self.get_endpoint(endpoint_name)
            if not endpoint:
                return {}
            #  'state': {'ready': 'READY', 'config_update': 'NOT_UPDATING'},
            state = endpoint.get("state",None)
            now = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime(time.time()))
            print(f"{now}: Waiting {i+1}/{max}: {state}")
            if state["ready"] == "READY" or state["config_update"] == "UPDATE_FAILED":
                return state
            time.sleep(sleep_time)
        return {}
