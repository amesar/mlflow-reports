
from mlflow_reports.common import object_utils
from mlflow_reports.common import io_utils
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common.timestamp_utils import fmt_ts_millis

def finish(dct, output_file, silent):
    if output_file:
        io_utils.write_file(output_file, dct)
    if not silent:
        object_utils.dump_as_json(dct)


def mk_tags(dct):
    tags = dct.pop("tags", None)
    if tags:
        dct["tags"] = mlflow_utils.mk_tags_dict(tags)


def adjust_ts(dct, keys):
    def format_ts(dct, key):
        ts = dct.get(key)
        if ts:
            dct[f"_{key}"] = fmt_ts_millis(int(ts))
    for k in keys:
        format_ts(dct, k)
