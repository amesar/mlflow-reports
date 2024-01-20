# MLflow Reports


Tools to display and list details of MLflow objects in JSON, CSV and Markdown format.

Two types of Python scripts:
* [MLflow objects](README_objects.md) - display and list MLflow objects (runs, experiments, models, versions, etc.) in JSON or CSV format.
* [Model reports](README_model_reports.md) - displays an MLflow model and its related objects in Markdown format.

Tools come in two formats:
* Regular Python scripts (see above links)
* [Databricks notebooks](databricks_notebooks/README.md)

Notes:
* See lots of [JSON and Markdown samples](samples/databricks/README.md).
* Databricks Unity Catalog models are also supported.
* The README documentation lags the actual implementation.

## Quick start

### Setup
```
python -m venv mlflow-reports
source mlflow-reports/bin/activate
```
```
pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
```

```
# Optional - if you want Unity Catalog models
export MLFLOW_REGISTRY_URI=databricks-uc
```

### Get model version details

For full JSON output, see [samples](samples/databricks/mlflow_objects/model_versions/Sklearn_Wine_best),
for example [uc_model_version.json](samples/databricks/mlflow_objects/model_versions/Sklearn_Wine_best/uc_model_version.json).

```
get-model-version \
  --registered-model andre.ml_models.sklearn_wine_best \
  --version 1 \
  --get-expanded True \
  --output-file model_version.json
```

```
{
  "model_version": {
    "name": "andre.ml_models.sklearn_wine_best",
    "version": "4",
    "creation_timestamp": 1703291776610,
    "last_updated_timestamp": 1703292274182,
    "user_id": "andre@mycompany.com",
    "_creation_timestamp": "2023-12-23 00:36:17",
    "_last_updated_timestamp": "2023-12-23 00:44:34",
    . . .
  },
  "mlflow_model": {
    "artifact_path": "model",
    "databricks_runtime": "14.1.x-cpu-ml-scala2.12",
    "flavors": {
      "python_function": {
      .  .  .
  },
  "registered_model": {
    "name": "andre.ml_models.sklearn_wine_best",
    "creation_timestamp": 1691761329476,
    "last_updated_timestamp": 1703863881768,
    "user_id": "andre@mycompany.com",
    "description": "Best sklearn_wine registered model",
    "aliases": [
      {
        "alias": "champ",
        "version": "7"
      },
    . . .
  },
  "run": {
    "info": {
      "run_id": "8217f29c1e5f4488a8fddaf9245d33bb",
      "run_uuid": "8217f29c1e5f4488a8fddaf9245d33bb",
      "experiment_id": 2668333326915882,
      "run_name": "white 2023-12-22",
    . . .
  },
  "experiment": {
    "experiment": {
      "experiment_id": 2668333326915882,
      "name": "/Users/andre@mycompany.com/experiments/best/Sklearn_Wine_repo_uc",
      "artifact_location": "dbfs:/databricks/mlflow-tracking/2668333326915882",
    "permissions": {
      "permission_levels": [
    . . .
  }
}
```

### List registered models

See examples
[registered_models.txt](samples/databricks/mlflow_objects/registered_models/registered_models.txt)
and
[registered_models.csv](samples/databricks/mlflow_objects/registered_models/registered_models.csv)

```
list-registered-models \
  --output-csv-file models.csv \
  --columns name,user_id,creation_timestamp
```

```
+-----------------------------------------+--------------------------+----------------------+
| name                                    | user_id                  | creation_timestamp   |
+-----------------------------------------+--------------------------+----------------------+
| andre.basic_models.copy_test            | sagarmatha@mycompany.com | 2023-10-09 20:48:51  |
| andre.basic_models.mini_mlops_pipeline  | k2@mycompany.com         | 2023-10-06 06:14:27  |
| andre.basic_models.xgboost_wine_best    | karakoram@mycompany.com  | 2023-08-16 05:34:57  |
| andre.basic_models.sklearn_wine_champ   | denali@mycompany.com     | 2023-09-19 23:01:56  |
| andre.basic_models.sklearn_wine_test_fs | chimborazo@mycompany.com | 2023-08-17 14:55:30  |
| market.llm_models.mistral7b_instruct    | huascaran@mycompany.com  | 2023-08-16 06:38:53  |
| market.llm_models.codellama-7b          | denali@mycompany.com     | 2023-08-11 14:38:18  |
+-----------------------------------------+--------------------------+----------------------+

```

#### Last updated: 2024-01-20
