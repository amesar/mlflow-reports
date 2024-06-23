"""
List the artifacts of an MLflow model.
"""

import click
from mlflow_reports.common.click_options import opt_model_uri, opt_output_file, opt_artifact_max_level
from mlflow_reports.common.dump_utils import dump_as_json
from mlflow_reports.common.io_utils import write_file
from mlflow_reports.common.artifact_utils import list_artifacts
from . click_options import opt_full_path

def _list(model_uri, output_file, artifact_max_level, full_path):
    artifacts = list_artifacts(model_uri, artifact_max_level, full_path)
    dump_as_json(artifacts["summary"])
    if output_file:
        write_file(output_file, artifacts, "json")


@click.command()
@opt_model_uri
@opt_output_file
@opt_artifact_max_level
@opt_full_path
def main(model_uri, output_file, artifact_max_level, full_path):
    """
    Recursively list the artifacts of an MLflow model and summary of artifact sizes and other details.
    An MLflow model URI can be 'models:/my-model/123' or 'runs:/123/my-model'.
    """
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    _list(model_uri, output_file, artifact_max_level, full_path)


if __name__ == "__main__":
    main()
