"""
List the artifacts of an MLflow model.
"""

import os
import click
from mlflow_reports.common.click_options import opt_artifact_uri, opt_output_dir, opt_artifact_max_level
from mlflow_reports.common.dump_utils import dump_as_json
from mlflow_reports.common.io_utils import write_file
from mlflow_reports.common.artifact_utils import list_artifacts
from . click_options import opt_full_path
from . tree_artifacts_utils import artifacts_to_string

def _list(artifact_uri, output_dir, artifact_max_level, full_path):
    artifacts = list_artifacts(artifact_uri, artifact_max_level, full_path)
    dump_as_json(artifacts["summary"], "Artifacts Summary")

    path = os.path.join(output_dir, "artifacts.json")
    write_file(path, artifacts, "json")

    tree = artifacts_to_string(artifacts)
    path = os.path.join(output_dir, "artifacts.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(tree+"\n")
    print("\nArtifacts Tree:")
    print(tree)


@click.command()
@opt_artifact_uri
@opt_output_dir
@opt_artifact_max_level
@opt_full_path
def main(artifact_uri, output_dir, artifact_max_level, full_path):
    """
    Recursively list the artifacts of an MLflow model and summary of artifact sizes and other details.
    An MLflow model URI can be 'models:/my-model/123' or 'runs:/123/my-model'.
    """
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    _list(artifact_uri, output_dir, artifact_max_level, full_path)


if __name__ == "__main__":
    main()
