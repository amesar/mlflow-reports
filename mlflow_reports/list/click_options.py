import click

def opt_max_description(function):
    function = click.option("--max-description",
        help="max_description.",
        type=int,
        show_default=True
    )(function)
    return function

def opt_max_models(function):
    function = click.option("--max-models",
        help="Maximun models to show.",
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
        help="Model prefix to show.",
        type=str,
        required=False
    )(function)
    return function

def opt_filter(function):
    function = click.option("--filter",
        help="Model filter.",
        type=str,
        required=False
    )(function)
    return function

def opt_columns(function):
    function = click.option("--columns",
        help="Columns to display. Comma delimited.",
        type=str,
        default=None
    )(function)
    return function

def opt_get_search_object_again(function):
    function = click.option("--get-search-object-again",
        help="Call get() again for search object to return missing aliases and tag fields.",
        type=bool,
        default=False
    )(function)
    return function

def opt_unity_catalog(function):
    function = click.option("--unity-catalog",
        help="Use Databricks Unity Catalog.",
        type=bool,
        default=False
    )(function)
    return function

def opt_get_tags_and_aliases(function):
    function = click.option("--get-tags-and-aliases",
        help="Get tags and aliases attribute from registered model.",
        type=bool,
        default=False
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
        help="Get MLflow model flavor and size.",
        type=bool,
        default=False
    )(function)
    return function

def opt_view_type(function):
    function = click.option("--view-type",
        help="Experiment view type: ACTIVE_ONLY|DELETED_ONLY|ALL.",
        type=str,
        default=None
    )(function)
    return function

def opt_max_results(function):
    function = click.option("--max-results",
        help="Max results for search query",
        type=int,
        default=None
    )(function)
    return function

def opt_catalog(function):
    function = click.option("--catalog",
        help="Catalog name.",
        type=str,
        required=False
    )(function)
    return function
    
def opt_schema(function):
    function = click.option("--schema",
        help="Schema name.",
        type=str,
        required=False
    )(function)
    return function

def opt_normalize_pandas_df(function):
    function = click.option("--normalize-pandas-df",
        help="Convert JSON list with pd.json_normalize, otherwise use pd.DataFrame.",
        type=bool,
        default=False
    )(function)
    return function
