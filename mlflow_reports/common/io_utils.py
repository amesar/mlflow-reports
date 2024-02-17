import json
import yaml
import pandas as pd
from mlflow_reports.data import data_utils
from mlflow_reports.list import list_utils


# Fix for PyYaml bug where yaml.safe_load() automatically converts to datetime-like fields to Python datetime
yaml.constructor.SafeConstructor.yaml_constructors[
    "tag:yaml.org,2002:timestamp"] = yaml.constructor.SafeConstructor.yaml_constructors["tag:yaml.org,2002:str"
]

def mk_local_path(path):
    return path.replace("dbfs:","/dbfs")


def _is_yaml(path, file_type=None):
    return any(path.endswith(x) for x in [".yaml",".yml"]) or file_type in ["yaml","yml"]


def write_file(path, content, file_type=None):
    """
    Write to JSON, YAML or text file.
    :param path: Output path.
    :param content: Python object to write.
    :param file_type: write in json, yaml or else in text
    """
    path = mk_local_path(path)
    if path.endswith(".json") or file_type=="json":
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(content, indent=2)+"\n")
    elif _is_yaml(path, file_type):
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(content, f, sort_keys=False)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def read_file(path, file_type=None):
    """
    Read a JSON, YAML or text file.
    """
    with open(path, "r", encoding="utf-8") as f:
        if path.endswith(".json") or file_type=="json":
            return json.loads(f.read())
        elif _is_yaml(path, file_type):
            return yaml.safe_load(f)
        else:
            return f.read()


def write_csv_and_json_files(output_file_base, list_of_dicts, columns=None, ts_columns=None, normalized_pandas_df=False):
    """
    Write a list of dicts in JSON format and its Pandas dataframe in CSV format.
    File base for JSON and CSV output files. For example, 'out' will result in 'out.csv' and 'out.json.
    Write to JSON, YAML or text file.
    :param output_file_base: File base for JSON and CSV output files. For example, 'out' will result in 'out.csv' and 'out.json.
    :param list_of_dicts: List of dicts
    :param columns: Dataframe columns to write
    :param ts_columns: Dataframe timestamp columns to convert from millis to human friendly format
    :param normalize: convert with pd.json_normalize, else use pd.DataFrame
    """
    df = pd.json_normalize(list_of_dicts) if normalized_pandas_df else pd.DataFrame(list_of_dicts)
    list_utils.to_datetime(df, ts_columns)
    list_utils.show_and_write(df, columns, f"{output_file_base}.csv")

    for dct in list_of_dicts:
        data_utils.adjust_ts(dct, ts_columns)
    data_utils.dump_object(list_of_dicts, f"{output_file_base}.json", silent=True)
