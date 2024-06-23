import click

def opt_full_path(function):
    function = click.option("--full-path",
        help="Display full artifact path name when displaying artifacts.",
        type=bool,
        required=False
    )(function)
    return function
