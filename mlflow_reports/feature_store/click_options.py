import click

def opt_table(function):
    function = click.option("--table",
        help="Table name",
        type=str,
        required=True
    )(function)
    return function
