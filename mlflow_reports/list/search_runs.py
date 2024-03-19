import copy
import numpy as np
import pandas as pd
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common.http_iterators import SearchRunsIterator
from mlflow_reports.client.http_client import mlflow_client
from . import list_utils

def search(experiment_id_or_name, filter=None):
    filter = filter or None
    exp = mlflow_utils.get_experiment(experiment_id_or_name)
    runs = list(SearchRunsIterator(mlflow_client, [exp["experiment_id"]], filter=filter))
    return runs

def as_pandas_df(runs):
    def clean(run):
        info = run["info"]
        info.pop("run_uuid")
        run_id = info.pop("run_id")
        run_name = info.pop("run_name")
        info = { **{ "run_id": run_id, "run_name": run_name}, **info }
        run["info"] = info
        run = { **{ "run_id": run_id, "run_name": run_name}, **run }
        return run
    if len(runs) == 0:
        return pd.DataFrame()
    runs = copy.deepcopy(runs)
    runs = [ clean(run) for run in runs ]
    df = pd.DataFrame.from_dict(runs)
    df = df.replace(np.nan, "", regex=True)
    #df = pd.json_normalize(runs)
    list_utils.to_datetime(df, ["start_time", "end_time"])
    return df
