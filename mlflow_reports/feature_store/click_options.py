import click

def opt_table(function):
    function = click.option("--table",
        help="Table name",
        type=str,
        required=True
    )(function)
    return function

def opt_get_from_search(function):
    function = click.option("--get-from-search",
        help="Get table details from search",
        type=bool,
        required=False
    )(function)
    return function
