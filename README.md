# Mlflow Reports

Solution  accelerator for MLflow model reports and displaying MLflow objects.

Two types of tools:
* [Model reports](README_model_reports.md) - solution  accelerator to display all details of an MLflow model in markdown.
* [MLflow object retrieval](README_objects.md) - returns JSON representation of MLflow object details.

[Databricks notebooks](databricks_notebooks/README.md) versions of the scripts also available.

Databricks Unity Catalog models are also supported (WIP).

See extensive [JSON and markdown samples](samples/databricks/README.md).

## Quick start

```
pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports

```

**MLflow Model Report**
```
model-report \
  --model-uri models:/credit_adjudication/production \
  --output-file model_report.md \
  --output-data-file model_report.json
```

See a sample [model_report.md](samples/databricks/model_reports/credit_adjudication/report.md).

**MLflow Object Retrieval**
```
get-mlflow-model \
  --model-uri models:/credit_adjudication/3
```
```
{         
  "mlflow_model": {
    "artifact_path": "model",
    "databricks_runtime": "12.2.x-cpu-ml-scala2.12",
    "flavors": {
      "python_function": {
        "env": {
          "conda": "conda.yaml",
          "virtualenv": "python_env.yaml"
        },
        "loader_module": "mlflow.sklearn",
        "model_path": "model.pkl",
        "predict_fn": "predict",
        "python_version": "3.9.5"
      },
      "sklearn": {
        "code": null,
        "pickled_model": "model.pkl",
        "serialization_format": "cloudpickle",
        "sklearn_version": "1.0.2"
      }
    },
```


## Setup 

Standard stuff.

##### Step 1. Create a virtual environment.
```
python -m venv mlflow-reports
source mlflow-reports/bin/activate
```

##### Step 2. pip install

pip install from github
```
pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
```

or pip install in editable mode
```
git clone https://github.com/amesar/mlflow-reports
cd mlflow-reports
pip install -e .
```

##### Step 3. Enable Unity Catalog model registry if desired

```
export MLFLOW_REGISTRY_URI=databricks-uc
```
