import click

def opt_max_description(function):
    function = click.option("--max-description",
        help="max_description",
        type=int,
        show_default=True
    )(function)
    return function

def opt_max_models(function):
    function = click.option("--max-models",
        help="max_models",
        type=int,
        show_default=None
    )(function)
    return function

def opt_output_csv_file(function):
    function = click.option("--output-csv-file",
        help="Output CSV file.",
        type=str,
        required=False
    )(function)
    return function

def opt_prefix(function):
    function = click.option("--prefix",
        help="Output CSV file.",
        type=str,
        required=False
    )(function)
    return function

def opt_filter(function):
    function = click.option("--filter",
        help="Filter",
        type=str,
        required=False
    )(function)
    return function

def opt_unity_catalog(function):
    function = click.option("--unity-catalog",
        help="Use Databricks Unity Catalog",
        type=bool,
        default=False
    )(function)
    return function

def opt_get_tags_and_aliases(function):
    function = click.option("--get-tags-and-aliases",
        help="Get tags and aliases attribute from registered model.",
        type=bool,
        default=True
    )(function)
    return function

def opt_tags_and_aliases_as_string(function):
    function = click.option("--tags-and-aliases-as-string",
        help="Write tags and aliases as JSON string instead of dict. Needed for Pandas to Spark DataFrame conversion.",
        type=bool,
        default=False
    )(function)
    return function

def opt_get_model_details(function):
    function = click.option("--get-model-details",
        help="Get MLflow model flavor and size",
        type=bool,
        default=False
    )(function)
    return function
