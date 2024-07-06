import click

def opt_full_path(function):
    function = click.option("--full-path",
        help="Display full artifact path name when displaying artifacts.",
        type=bool,
        required=False
    )(function)
    return function

def opt_show_run_artifacts(function):
    function = click.option("--show-run-artifacts",
        help="Display run artifacts of model version.",
        type=bool,
        required=False
    )(function)
    return function
