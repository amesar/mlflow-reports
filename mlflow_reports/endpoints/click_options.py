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
