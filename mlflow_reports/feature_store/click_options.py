import click

def opt_get_from_search(function):
    function = click.option("--get-from-search",
        help="Get table details from search",
        type=bool,
        required=False
    )(function)
    return function
