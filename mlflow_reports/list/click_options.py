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

def opt_datetime_as_string(function):
    function = click.option("--datetime-as-string",
        help="Convert Pandas datetime to string since Databricks display() ignores rounding of seconds.",
        type=bool,
        default=False
    )(function)
    return function
