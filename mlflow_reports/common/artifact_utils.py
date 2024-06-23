import os
import json
from dataclasses import dataclass
import mlflow
from mlflow_reports.common import timestamp_utils


@dataclass()
class Result:
    artifacts: dict = None
    num_bytes: int = 0
    num_artifacts: int = 0
    num_levels: int = 0
    def __repr__(self):
        msg = { "num_bytes": self.num_bytes, "num_artifacts": self.num_artifacts, "num_levels": self.num_levels }
        return json.dumps(msg)

def list_artifacts(artifact_uri, artifact_max_level=1, full_path=False):
    """
    Build recursive tree of calls to 'artifacts/list' API endpoint.
    :param run_id: Run ID.
    :param artifact_path: Relative artifact path.
    :param artifact_max_level: Levels to recurse.
    :return: Nested dict with list of artifacts representing tree node info.
    """
    res = _list_artifacts(artifact_uri, artifact_max_level, 0, full_path)
    summary = {
        "artifact_uri": artifact_uri,
        "num_bytes": res.num_bytes,
        "_num_bytes": f"{res.num_bytes:,}",
        "num_artifacts": res.num_artifacts,
        "num_levels": res.num_levels,
        "artifact_max_level": artifact_max_level,
        "timestamp": timestamp_utils.now(),
        "mlflow_tracking_uri": os.environ.get("MLFLOW_TRACKING_URI",""),
        "mlflow_registry_uri": os.environ.get("MLFLOW_REGISTRY_URI","")
    }
    return { **{ "summary": summary }, **{ "artifacts": res.artifacts } }


def _list_artifacts(artifact_uri, artifact_max_level=1, level=0, full_path=False):
    def _to_dict_without_underscore(obj):
        return { k[1:]:v for k,v in obj.__dict__.items() }

    if level >= artifact_max_level:
        return Result([], 0, 0, level)
    level += 1
    num_levels = level

    dir_num_bytes, num_artifacts = (0, 0)
    file_infos = mlflow.artifacts.list_artifacts(artifact_uri)
    artifacts = []
    for finfo in file_infos:
        dct = _to_dict_without_underscore(finfo)
        dct.pop("is_dir", None) # don't need this - the presence of 'artifacts' list indicates that its a directory
        if finfo.is_dir:
            _artifact_uri = os.path.join(artifact_uri, os.path.basename(finfo.path))
            res = _list_artifacts(_artifact_uri, artifact_max_level, level, full_path)
            num_levels = max(num_levels, res.num_levels)
            dir_num_bytes += res.num_bytes
            num_artifacts += res.num_artifacts
            dct["bytes"] = dir_num_bytes
            dct["_bytes"] = f"{dir_num_bytes:,}"
            dct["artifacts"] = res.artifacts
        else:
            num_artifacts += 1
            dir_num_bytes += finfo.file_size
            dct["bytes"] = finfo.file_size
            dct["_bytes"] = f"{finfo.file_size:,}"
        if not full_path:
            dct["path"] = os.path.basename(dct["path"])
        artifacts.append(dct)

    return Result(artifacts, dir_num_bytes, num_artifacts, num_levels)
