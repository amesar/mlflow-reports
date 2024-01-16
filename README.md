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
+----------------------------------|----------------------|--------------------|-----------------------------------|----------------------+
| name                             | endpoint_type        | task               | creator                           | creation_timestamp   |
+----------------------------------|----------------------|--------------------|-----------------------------------|----------------------+
| embeddings_proxy_eo              |                      |                    | amelia.young-singer@mycompany.com | 2023-11-22 18:36:33  |
| eo_rfp_rag                       |                      |                    | amelia.young-singer@mycompany.com | 2023-11-22 19:00:33  |
| databricks-llama-2-70b-chat      | FOUNDATION_MODEL_API | llm/v1/chat        |                                   | 2023-11-10 09:53:20  |
| databricks-mixtral-8x7b-instruct | FOUNDATION_MODEL_API | llm/v1/chat        |                                   | 2023-11-10 09:53:20  |
| databricks-bge-large-en          | FOUNDATION_MODEL_API | llm/v1/embeddings  |                                   | 2023-11-10 09:53:20  |
| databricks-mpt-30b-instruct      | FOUNDATION_MODEL_API | llm/v1/completions |                                   | 2023-11-10 09:53:20  |
| databricks-mpt-7b-instruct       | FOUNDATION_MODEL_API | llm/v1/completions |                                   | 2023-11-10 09:53:20  |
+----------------------------------|----------------------|--------------------|-----------------------------------|----------------------+
```

#### Last updated: 2024-01-15
