"""
Get the signature of an MLflow model.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.mlflow_model.mlflow_model_utils import get_model_info
from mlflow_reports.common.click_options import opt_model_uri, opt_output_file
from mlflow_reports.common.dump_utils import dump_as_json

def get(model_uri):
    mlmodel = get_model_info(model_uri)
    dump_as_json(mlmodel, "MLmodel")
    return mlmodel.get("signature")


@click.command()
@opt_model_uri
@opt_output_file
def main(model_uri, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    signature = get(model_uri)
    dump_as_json(signature)
    if output_file:
        io_utils.write_file(output_file, signature)

if __name__ == "__main__":
    main()
