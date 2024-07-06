import click


def opt_model_uri(function):
    function = click.option("--model-uri",
        help="Model URI such as 'models:/my-model/123' or 'runs:/123/my-model'.",
        type=str,
        required=True
    )(function)
    return function

def opt_artifact_uri(function):
    function = click.option("--artifact-uri",
        help="Artifact URI such as 'models:/my-artifact/123' or 'runs:/123/my-artifact'.",
        type=str,
        required=True
    )(function)
    return function

def opt_run_id(function):
    function = click.option("--run-id",
        help="Run ID",
        type=str,
        required=True
    )(function)
    return function

def opt_experiment_id_or_name(function):
    function = click.option("--experiment-id-or-name",
        help="Experiment ID or name",
        type=str,
        required=True
    )(function)
    return function

def opt_registered_model(function):
    function = click.option("--registered-model",
        help="Registered model name.",
        type=str,
        required=True
    )(function)
    return function

def opt_model_version(function):
    function = click.option("--version",
        help="Model version.",
        type=str,
        required=True
    )(function)
    return function


def opt_get_run(function):
    function = click.option("--get-run",
        help="Get run.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_experiment(function):
    function = click.option("--get-experiment",
        help="Get experiment.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_registered_model(function):
    function = click.option("--get-registered-model",
        help="Get registered_model",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_versions(function):
    function = click.option("--get-versions",
        help="Get model versions.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_latest_versions(function):
    function = click.option("--get-latest-versions",
        help="Get model latest versions.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_runs(function):
    function = click.option("--get-runs",
        help="Get runs.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_permissions(function):
    function = click.option("--get-permissions",
        help="Get Databricks permissions.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function


def opt_artifact_max_level(function):
    function = click.option("--artifact-max-level",
        help="Number of artifact levels to recurse when displaying artifacts.",
        type=int,
        default=1,
        show_default=True
    )(function)
    return function

def opt_get_raw(function):
    function = click.option("--get-raw",
        help="Preserve raw JSON as received from API call.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_get_expanded(function):
    function = click.option("--get-expanded",
        help="Get all objects associated with model version",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_output_file(function):
    function = click.option("--output-file",
        help="JSON output file.",
        type=str,
        required=False
    )(function)
    return function

def opt_output_dir(function):
    function = click.option("--output-dir",
        help="Output directory.",
        type=str,
        default=".",
        show_default=True
    )(function)
    return function

def opt_output_file_base(function):
    function = click.option("--output-file-base",
        help="File base for JSON and CSV output files. For example, 'out' will result in 'out.csv' and 'out.json.'",
        type=str,
        default="out",
        show_default=True
    )(function)
    return function

def opt_silent(function):
    function = click.option("--silent",
        help="Do not display to stdout.",
        type=bool,
        default=False,
        show_default=True
    )(function)
    return function

def opt_table(function):
    function = click.option("--table",
        help="Table name",
        type=str,
        required=True
    )(function)
    return function

def opt_get_details(function):
    function = click.option("--get-details",
        help="Get details of each listed object.",
        type=bool,
        default=False
    )(function)
    return function
