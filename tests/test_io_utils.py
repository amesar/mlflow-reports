from tempfile import NamedTemporaryFile as TempFile
from mlflow_reports.common import io_utils

dct = {
    "name": "north",
    "year": 2020
}

def test_json_default():
    with TempFile(prefix="file_", suffix=".json", mode="w") as f:
        io_utils.write_file(f.name, dct)
        obj = io_utils.read_file(f.name)
        assert obj == dct
 
def test_json_filetype():
    with TempFile(prefix="MLmodel_", mode="w") as f:
        io_utils.write_file(f.name, dct, "json")
        obj = io_utils.read_file(f.name, "json")
        assert obj == dct


def test_yaml_default():
    with TempFile(prefix="file_", suffix=".yaml", mode="w") as f:
        io_utils.write_file(f.name, dct)
        obj = io_utils.read_file(f.name)
        assert obj == dct

def test_yaml_filetype():
    with TempFile(prefix="file_", mode="w") as f:
        io_utils.write_file(f.name, dct, "yaml")
        obj = io_utils.read_file(f.name, "yaml")
        assert obj == dct


def test_text_filetype():
    with TempFile(prefix="file_", mode="w") as f:
        txt = "circumpolar circuit"
        io_utils.write_file(f.name, txt)
        obj = io_utils.read_file(f.name)
        assert obj == txt
