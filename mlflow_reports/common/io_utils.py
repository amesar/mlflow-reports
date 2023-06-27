import json
import yaml

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
