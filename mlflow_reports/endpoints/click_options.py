import click

def opt_endpoint(function):
    function = click.option("--endpoint",
        help="Model serving endpoint name.",
        type=str,
        required=False
    )(function)
    return function

def opt_sort(function):
    function = click.option("--sort",
        help="Sort restuls by name",
        type=bool,
        default=False
    )(function)
    return function

def opt_call_databricks_model_serving(function):
    function = click.option("--call-databricks-model-serving",
        help="Call Databricks 'api/2.0/serving-endpoints' resource directly instead of using mlflow.deployments.get_deploy_client",
        type=bool,
        default=False
    )(function)
    return function

def opt_model_type(function):
    function = click.option("--model-type",
        help="Model type: all|custom|foundation|external",
        type=click.Choice(["all", "custom", "foundation", "external"]), default = "all"
    )(function)
    return function

def opt_expand_model_version(function):
    function = click.option("--expand-model-version",
        help="Model type: version|version-and-signature|version-all",
        type=click.Choice(["none", "version", "version-and-signature", "version-all"]),
    )(function)
    return function

def opt_input_file(function):
    function = click.option("--input-file",
        help="Use saved JSON in filefrom a previous call to /api/2.0/serving-endpoints. Will not call API.",
        type=str,
        required=False
    )(function)
    return function
