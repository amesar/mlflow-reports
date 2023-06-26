import click


def opt_model_uri(function):
    function = click.option("--model-uri",
        help="Model URI such as 'models:/my-model/123' or 'runs:/123/my-model'.",
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
        help="Number of artifact levels to recurse for run artifacts.",
        type=int,
        default=-1,
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

def opt_output_file(function):
    function = click.option("--output-file",
        help="JSON output file.",
        type=str,
        required=False
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
