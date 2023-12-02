import click
import copy
from mdutils.mdutils import MdUtils

from mlflow_reports.mlflow_model import mlflow_model_manager as model_manager
from mlflow_reports.common import mlflow_utils, io_utils, timestamp_utils, object_utils
from mlflow_reports.common.click_options import(
    opt_model_uri,
    opt_output_file,
    opt_get_permissions
)
from mlflow_reports.markdown.report_factory import ReportFactory, TAG_COLUMNS
from mlflow_reports.markdown.local_utils import newline_tweak, is_primitive, escape_dict
from mlflow_reports.data import enriched_tags


def build_report(model_uri, get_permissions, output_file, output_data_file=None, show_as_json=False, show_manifest=False):
    """
    Main entry point for report
    """
    card = MdUtils(file_name=output_file, title=f"MLflow Model: _{model_uri}_")
    rf = ReportFactory(card)

    data = model_manager.get(model_uri, get_permissions)
    if (output_data_file):
        io_utils.write_file(output_data_file, data)

    if "error" in data:
        rf.wf.mk_error(data)
        card.create_md_file()
        return data

    _build_overview_model(rf.wf, data, show_manifest)
    _build_model_info(rf, data.get("mlflow_model"), show_as_json, 1)
    _build_model_info_raw(rf, data.get("mlflow_model_raw"), show_as_json, 1)
    if data.get("model_version"):
        _build_model_version(rf.wf, data.get("model_version"))
    if data.get("registered_model"):
        _build_registered_model(rf, data.get("registered_model"))
    if data.get("run"):
        _build_run(rf, data.get("run"))
    if data.get("experiment"):
        _build_experiment(rf, data.get("experiment"))

    card.new_table_of_contents(table_title="Contents", depth=2)
    card.create_md_file()

    return data


def _build_overview_model(wf, data, show_manifest):
    wf.card.new_header(level=1, title="Model Overview")

    manifest = data.get("manifest")
    mlflow_model = data.get("mlflow_model")
    if mlflow_utils.has_error(mlflow_model):
        dct_mlflow_model = mlflow_model
    else:
        flavor = get_native_flavor_adjusted(mlflow_model.get("flavors"))
        utc_time = mlflow_model.get("utc_time_created")
        utc_time_created = utc_time.split(".")[0]
        reg_model = data.get("registered_model")
        model_size_bytes = mlflow_model.get("model_size_bytes")
        is_unity_catalog = reg_model.get(enriched_tags.TAG_IS_UNITY_CATALOG) if reg_model else ""
        dct_mlflow_model = {
            "model_uri": manifest.get("model_uri"),
            "flavor": flavor.get("flavor"),
            "flavor_version": flavor.get("version"),
            "mlflow_version": mlflow_model.get("mlflow_version"),
            "size_bytes": f"{model_size_bytes:,}",
            "databricks_runtime": mlflow_model.get("databricks_runtime",""),
            "is_unity_catalog": is_unity_catalog,
            "time_created": utc_time_created,
            "report_time": timestamp_utils.ts_now_fmt_utc
        }
    wf.build_table(dct_mlflow_model, "MLflow Model", level=0)
    _build_mlflow_model_uris(wf, manifest)

    if show_manifest:
        dct = copy.deepcopy(manifest)
        dct.pop("model_uris",None)
        wf.build_table(dct, "Manifest", level=0)


def _build_mlflow_model_uris(wf, manifest):
    dct = manifest.get("model_uris")
    wf.build_table(dct, "MLflow Model URIs", level=0, columns=["URI type","URI"])


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
    if mlflow_utils.has_error(flavors):
        return {}
    else:
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


def _build_model_info(rf, model_info, show_as_json=True, level=1, title="MLflow Model"):
    """
    Build MLflow model info section
    """
    rf.wf.card.new_header(level=level, title=title)
    _build_model_info_details(rf.wf, model_info, level+1)

    rf.build_flavors(model_info.get("flavors"), level=level+2, show_as_json=show_as_json)

    rf.build_signature(model_info.get("signature"), level=level+1)
    rf.build_saved_input_example_info(model_info.get("saved_input_example_info"), level=level+1)


def _build_model_info_raw(rf, fs_model_info, show_as_json=True, level=1, title="Raw Model - Feature Store"):
    if not fs_model_info:
        return
    rf.wf.card.new_header(level=level, title=title)
    model_info = fs_model_info["mlflow_model"]

    _build_model_info_details(rf.wf, model_info, level+1)
    rf.build_flavors(model_info.get("flavors"), level=level+1, show_as_json=show_as_json)

    rf.wf.card.new_header(level=level+1, title="Feature Spec")
    fs_spec = fs_model_info.get("feature_spec")
    rf.wf.card.new_line(escape_dict(fs_spec))


def _build_model_info_details(wf, model_info, level):
    dct = { k:v for k,v in model_info.items() if is_primitive(v) }
    wf.mk_list_as_table(dct, title="Details", level=level)


def _build_registered_model(rf, registered_model):
    rf.card.new_header(level=1, title="Registered Model")

    dct = { k:v for k,v in registered_model.items() if is_primitive(v) }
    newline_tweak(dct)
    rf.wf.build_table(dct, "Details", level=2)

    tags = registered_model.get("tags")
    rf.wf.build_table(tags, "Tags", level=2)

    rf.build_permissions(registered_model.get("permissions"), 2)


def _build_model_version(wf, model_version):
    wf.card.new_header(level=1, title="Registered Model Version")

    dct = { k:v for k,v in model_version.items() if is_primitive(v) }
    newline_tweak(dct)
    wf.build_table(dct, "Details", level=2)

    tags = model_version.get("tags")
    wf.build_table(tags, "Tags", level=2)

    transition_requests = model_version.get("transition_requests")
    if transition_requests:
        wf.card.new_header(level=2, title="Transition Requests")
        wf.card.new_line(escape_dict(transition_requests))


def _build_run(rf, run):
    """
    Build run
    """
    rf.card.new_header(level=1, title="Run")

    if "error" in run:
        msg = object_utils.json_to_dict(run.get("error"))
        rf.wf.mk_list_as_table(msg, title=rf.wf.mk_red("Error"), level=2)
        return

    data = run.get("data")
    tags = data.get("tags")

    info = run.get("info")
    newline_tweak(info)
    rf.wf.build_table(info, "Info", level=2)

    params = mlflow_utils.mk_tags_dict(data.get("params"))
    rf.wf.build_table(params, "Params", level=2, columns=["Param","Value"])

    x = mlflow_utils.mk_tags_dict(data.get("metrics"))
    rf.wf.build_table(x, "Metrics", level=2, columns=["Metric","Value"])

    rf.card.new_header(level=2, title="Inputs")
    _build_run_tags(rf, tags)


def _build_run_tags(rf, tags):
    rf.card.new_header(level=2, title="Tags")

    # == system and user tags

    def _strip_tag_prefix(dct, prefix):
        return { k.replace(prefix,""):v for k,v in dct.items() }

    def build_system_tags():
        #dct = _strip_tag_prefix(dct, "mlflow.databricks.")

        sys_tags, user_tags = {}, {}
        git_tags, nb_tags, cluster_tags, src_tags, ws_tags, job_tags = {}, {}, {}, {}, {}, {}

        for k,v in tags.items():
            if k.startswith("mlflow.databricks.gitRepo"):
                git_tags[k] = v
            elif k.startswith("mlflow.databricks.notebook"):
                nb_tags[k] = v
            elif k.startswith("mlflow.databricks.cluster"):
                cluster_tags[k] = v
            elif k.startswith("mlflow.databricks.w"):
                ws_tags[k] = v
            elif k.startswith("mlflow.source."):
                src_tags[k] = v
            elif k.startswith("mlflow.databricks.job"):
                job_tags[k] = v
            elif k.startswith("mlflow"):
                sys_tags[k] = v
            else:
                user_tags[k] = v

        if git_tags:
            rf.wf.build_table(git_tags, "Git Repo Tags", level=3, **TAG_COLUMNS)
        if nb_tags:
            rf.wf.build_table(nb_tags, "Notebook Tags", level=3, **TAG_COLUMNS)
        if cluster_tags:
            rf.wf.build_table(cluster_tags, "Cluster Tags", level=3, **TAG_COLUMNS)
        if ws_tags:
            rf.wf.build_table(ws_tags, "Workspace Tags", level=3, **TAG_COLUMNS)
        if src_tags:
            rf.wf.build_table(src_tags, "Source Tags", level=3, **TAG_COLUMNS)
        if job_tags:
            rf.wf.build_table(job_tags, "Job Tags", level=3, **TAG_COLUMNS)
        rf.wf.build_table(sys_tags, "Other System Tags", level=3, **TAG_COLUMNS)
        rf.wf.build_table(user_tags, "User Tags", level=3, **TAG_COLUMNS)

    build_system_tags()

    # == exploded tags

    # sparkDatasourceInfo
    rf.wf.card.new_header(level=3, title="Exploded Tags")
    rf.build_sparkDatasourceInfo(tags.get("sparkDatasourceInfo"), 4)
    rf.build_cluster_stuff(tags, 4)


def _build_experiment(rf, experiment):
    rf.wf.card.new_header(level=1, title="Experiment")
    exp_info = experiment.get("experiment")
    if not exp_info:
        exp_info = experiment
    dct = { k:v for k,v in exp_info.items() if is_primitive(v) }
    rf.wf.build_table(dct, "Details", level=2)

    tags = exp_info.get("tags")
    _build_tags(rf.wf, tags, level=2)

    rf.build_permissions(experiment.get("permissions"), 2)


def _build_tags(wf, tags, level):
    wf.card.new_header(level=level, title="Tags")
    if not tags:
        wf.mk_not_present()
        return
    sys_tags, user_tags = {}, {}
    for k,v in tags.items():
        if k.startswith("mlflow"):
            sys_tags[k] = v
        else:
            user_tags[k] = v
    wf.build_table(sys_tags, "MLflow System Tags", level=level+1, **TAG_COLUMNS)
    wf.build_table(user_tags, "User Tags", level=level+1, **TAG_COLUMNS)


@click.command()
@opt_model_uri
@click.option("--show-as-json",
     help="Show as JSON selected fields",
     type=bool,
     default=False,
     show_default=True
)
@click.option("--show-manifest",
     help="Show manifest stanza",
     type=bool,
     default=False,
     show_default=True
)
@opt_output_file
@click.option("--output-data-file",
     help="Output JSON data file",
     type=str,
     default=None,
     show_default=True
)
@opt_get_permissions

def main(model_uri, show_as_json, show_manifest, output_file, output_data_file, get_permissions):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    build_report(model_uri, get_permissions, output_file, output_data_file, show_as_json, show_manifest)

if __name__ == "__main__":
    main()
