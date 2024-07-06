import os
from mlflow_reports.common import dump_utils
from mlflow_reports.common import io_utils
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common.timestamp_utils import fmt_ts_millis
from mlflow_reports.data import enriched_tags
from mlflow_reports.tools.tree_artifacts_utils import artifacts_to_string

def dump_object(dct, output_file, silent):
    if output_file:
        io_utils.write_file(output_file, dct)
    if not silent:
        dump_utils.dump_as_json(dct)


def mk_tags(dct):
    tags = dct.pop("tags", None)
    if tags:
        dct["tags"] = mlflow_utils.mk_tags_dict(tags)


def adjust_ts(dct, keys):
    def format_ts(dct, key):
        ts = dct.get(key)
        if ts:
            dct[f"_{key}"] = fmt_ts_millis(int(ts))
    if keys:
        for k in keys:
            format_ts(dct, k)


def adjust_uc(reg_model_or_version):
    model_name = reg_model_or_version.get("name")
    reg_model_or_version[enriched_tags.TAG_IS_UNITY_CATALOG] = mlflow_utils.is_unity_catalog_model(model_name)


def write_artifacts_tree(artifacts, output_json_file):
    tree = artifacts_to_string(artifacts)
    base = os.path.splitext(output_json_file)[0]
    path = f"{base}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(tree+"\n")
