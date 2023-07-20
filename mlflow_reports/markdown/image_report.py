import os
import sys
import copy
import click
from mlflow.artifacts import download_artifacts
from mdutils.mdutils import MdUtils

from mlflow_reports.mlflow_model import mlflow_model_manager as model_manager
from mlflow_reports.common import mlflow_utils, io_utils, timestamp_utils
from mlflow_reports.common.click_options import(
    opt_model_uri,
    opt_get_permissions
)
from mlflow_reports.markdown.report_factory import ReportFactory
from mlflow_reports.data import enriched_tags


def build_report(model_uri, images, output_dir, get_permissions, show_manifest=False):
    """
    Main entry point for report
    """
    images = images.split(",")
    card = MdUtils(file_name=os.path.join(output_dir,"report.md"), title=f"MLflow Model: _{model_uri}_")
    rf = ReportFactory(card)

    data = model_manager.get(model_uri, get_permissions)
    io_utils.write_file(os.path.join(output_dir,"report.json"), data)

    if "error" in data:
        rf.wf.mk_error(data)
        card.create_md_file()
        return data

    _build_overview_model(rf.wf, data, show_manifest)
    _build_images(rf.wf, data, images, output_dir)
    card.new_table_of_contents(table_title="Contents", depth=2)
    card.create_md_file()

    return data


def _build_overview_model(wf, data, show_manifest):
    wf.card.new_header(level=1, title="Model Overview")

    run_id = data.get("mlflow_model").get("run_id")
    flavor = get_native_flavor_adjusted(data.get("mlflow_model").get("flavors"))
    model_artifacts_size = _calc_model_size(run_id, data.get("mlflow_model")["artifact_path"])

    utc_time = data.get("mlflow_model").get("utc_time_created")
    utc_time_created = utc_time.split(".")[0]
    manifest = data.get("manifest")
    reg_model = data.get("registered_model")
    is_unity_catalog = reg_model.get(enriched_tags.TAG_IS_UNITY_CATALOG) if reg_model else ""
    dct_mlflow_model = {
        "model_uri": manifest.get("model_uri"),
        "flavor": flavor.get("flavor"),
        "flavor_version": flavor.get("version"),
        "mlflow_version": data.get("mlflow_model").get("mlflow_version"),
        "size_bytes": f"{model_artifacts_size:,}",
        "databricks_runtime": data.get("mlflow_model").get("databricks_runtime",""),
        "is_unity_catalog": is_unity_catalog,
        "time_created": utc_time_created,
        "report_time": timestamp_utils.ts_now_fmt_utc
    }

    wf.build_table(dct_mlflow_model, "MLflow Model", level=0)

    if show_manifest:
        dct = copy.deepcopy(manifest)
        dct.pop("model_uris",None)
        wf.build_table(dct, "Manifest", level=0)


def _build_images(wf, data, images, output_dir):
    output_dir = "out"
    wf.card.new_header(level=1, title="Model Images")
    run_id = data.get("mlflow_model").get("run_id")

    for image in images:
        toks = image.split(";")
        image = toks[0]
        title = toks[1] if len(toks) > 1 else None
        _mk_image(wf, run_id, image, output_dir, 2, title)


def _mk_image(wf, run_id, artifact_path, output_dir, level, title):
    if title:
        title = title.replace("_"," ")
        wf.card.new_header(level=level, title=title)
    local_path = get_artifact(run_id, artifact_path, output_dir)
    str = "![]("+local_path+")"
    wf.card.new_line(str)


def get_artifact(run_id, artifact_path, output_dir):
    model_uri = f"runs:/{run_id}"
    artifact_uri = f"{model_uri}/{artifact_path}"
    return download_artifacts(artifact_uri=artifact_uri, dst_path=output_dir)


def get_native_flavor_adjusted(flavors):
    if len(flavors.keys()) == 1:
        return get_native_flavor_adjusted_fs(flavors)
    else:
        assert len(flavors.keys()) == 2
        return get_native_flavor_adjusted_std(flavors)
    
    
def get_native_flavor_adjusted_fs(flavors):
    """ 
    Process the raw feature store MLmodel.
    """ 
    keys = list(flavors.keys())
    flavor = flavors.get(keys[0])
    dct = {
        "flavor": flavor.get("loader_module"),
        "version": ""
    }
    return dct

def get_native_flavor_adjusted_std(flavors):
    """
    If standard model with one MLmodel file.
    """
    keys = list(flavors.keys())
    pyfunc, native = flavors.get(keys[0]), flavors.get(keys[1])
    keys = list(flavors.keys())
    if keys[1] == "python_function":
        tmp = pyfunc
        pyfunc = native
        native = tmp

    native = copy.deepcopy(native)

    matches = [ (k,v) for k,v in native.items() if k.endswith("_version") ]
    kv = matches[0]
    version = native.pop(kv[0], None)

    flavor_name = pyfunc.get("loader_module")

    flavor = { **{ "flavor": flavor_name, "version": version }, **native }
    return flavor


def _calc_model_size(run_id, model_artifact_path):  
    model_artifacts = mlflow_utils.build_artifacts(run_id, model_artifact_path, sys.maxsize)
    return model_artifacts["summary"]["num_bytes"]
    

@click.command()
@opt_model_uri
@click.option("--show-manifest",
     help="Show manifest stanza",
     type=bool,
     default=False,
     show_default=True
)
@click.option("--output-dir",
     help="Output directory",
     type=str,
     required=True,
     show_default=True
)
@click.option("--images",
     help="List of relative artifact paths of model run images (comma-delimited). Each list element can consist of image;title.",
     type=str,
     required=True,
     show_default=True
)
@opt_get_permissions

def main(model_uri, show_manifest, output_dir, images, get_permissions):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    build_report(model_uri, images, output_dir, get_permissions, show_manifest)

if __name__ == "__main__":
    main()
