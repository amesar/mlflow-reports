
import click

def opt_endpoint(function):
    function = click.option("--endpoint",
        help="Model serving endpoint name.",
        type=str,
        required=False
    )(function)
    return function

def opt_get_details(function):
    function = click.option("--get-details",
        help="Get details",
        type=bool,
        default=False
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
        help="Call Databricks 'api/2.0/serving-endpoints' resource eirectly instead of using DatabricksDeploymentClient",
        type=bool,
        default=False
    )(function)
    return function
