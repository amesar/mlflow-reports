# Display and List MLflow Objects

## Overview

Python scripts and [Databricks notebooks](databricks_notebooks/README.md) to display and list MLflow objects.

Last updated: _2024-05-20_.

### Commands

#### [Get MLflow object details](#get-mlflow-object-details)
*  [get-run](#get-run) - get run
*  [get-experiment](#get-experiment) - get experiment
*  [get-model-version](#get-model-version) - get model version
*  [get-registered-model](#get-registered-model) - get registered model

#### [List objects](#list-mlflow-objects)
*  [list-registered-models](#list-registered-models) - list registered models
*  [list-model-versions](#list-model-versions) - list model versions

#### MLflow model commands
*  [get-mlflow-model](#get-mlflow-model) - returns the contents of an MLflow model's [MLmodel](samples/databricks/model_reports/credit_adjudication/MLmodel) artifact.
*  [get-mlflow-model-wide](#get-mlflow-model-wide) - same as above plus  with all of the model's  related objects (run, experiment, model version and registered model).


## Get MLflow Object Details

### Get MLflow Model

Returns the contents of an MLflow model's MLmodel artifact.

Sample:
  * [mlflow_model.json](samples/databricks/mlflow_objects/mlflow_models/credit_adjudication.json)
  * [MLmodel](samples/databricks/model_reports/credit_adjudication/MLmodel)

##### Example
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

##### Usage

```
get-mlflow-model --help

Options:
  --model-uri TEXT    Model URI such as 'models:/my-model/123' or
                      'runs:/123/my-model'.  [required]
  --get-run BOOLEAN   Get run.  [default: False]
  --get-raw BOOLEAN   Preserve raw JSON as received from API call.  [default:
                      False]
  --silent BOOLEAN    Do not display to stdout.  [default: False]
  --output-file TEXT  JSON output file.
```

### Get MLflow Model Wide

Returns the contents of an MLflow model's MLmodel artifact along with all its related objects (run, experiment, model version and registered model).

Sample:
  * [MLmodel](samples/databricks/model_reports/credit_adjudication/MLmodel)
  * [credit_adjudication.json](samples/databricks/model_reports/credit_adjudication/report.json)

##### Example
```
get-mlflow-model \
  --model-uri models:/credit_adjudication/3
```

```
{
  "manifest": {
    "model_uri": "models:/credit_adjudication/production",
    "source": "databricks://e2_demo",
    "model_uris": {
      "model_uri": "models:/credit_adjudication/production",
      "run_uri": "runs:/76031d22c5464dd99431e426b939e800/model",
      "reg_model_download_uri": "dbfs:/databricks/mlflow-registry/417e414731e74e03b731fb3a63a3b4e4/models/model",
      "run_model_download_uri": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model"
    },
    "mlflow_version": "2.4.1",
    "timestamp": "2023-07-05 12:39:46"
  },
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
```


##### Usage

```
get-mlflow-model-wide --help

Options:
  --model-uri TEXT           Model URI such as 'models:/my-model/123' or
                             'runs:/123/my-model'.  [required]
  --get-permissions BOOLEAN  Get Databricks permissions.  [default: False]
  --get-raw BOOLEAN          Preserve raw JSON as received from API call.
                             [default: False]
  --silent BOOLEAN           Do not display to stdout.  [default: False]
  --output-file TEXT         JSON output file.
```

## MLflow Object Commands


### Get run

Get run.
* [Sample JSON](samples/databricks/mlflow_objects/runs/credit_adjudication.json).
* Gets info, params, metrics and tags of a run.
* Recursively lists run artifacts up to the specified level.

##### Example

```
get-run \
  --run-id 76031d22c5464dd99431e426b939e800 \
  --artifact-max-level 5
```

```
{
  "run": {
    "info": {
      "run_id": "76031d22c5464dd99431e426b939e800",
      "experiment_id": "bf024d57582f4c8cbf816151cc6e1bac",
      "run_name": "credit adjudication",
      "status": "FINISHED",
      "start_time": 1686872052388,
      "end_time": 1686872056211,
      "lifecycle_stage": "active",
      "_start_time": "2023-06-15 23:34:12",
      "_end_time": "2023-06-15 23:34:16",
      "_duration": 3.823,
. . .
```

##### Usage

```
get-run --help

Options:
  --run-id TEXT                 Run ID  [required]
  --artifact-max-level INTEGER  Number of artifact levels to recurse for run
                                artifacts.  [default: -1]
  --get-raw BOOLEAN             Preserve raw JSON as received from API call.
                                [default: False]
  --silent BOOLEAN              Do not display to stdout.  [default: False]
  --output-file TEXT            JSON output file.
```

### Get Experiment

Get experiment.
* Get experiment details and optionally its permissions and runs.
* [Sample JSON](samples/databricks/mlflow_objects/experiments/credit_adjudication.json).

With experiment ID:
```
get-experiment \
  --experiment-id-or-name bf024d57582f4c8cbf816151cc6e1bac \
  --get-runs \
  --get-permissions
```

With experiment name:
```
get-experiment \
  --experiment-id-or-name "/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example" \
  --get-runs \
  --get-permissions
```

Response:
```
{
  "experiment": {
    "experiment_id": "bf024d57582f4c8cbf816151cc6e1bac",
    "name": "/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example",
    "artifact_location": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac",
    "lifecycle_stage": "active",
    "last_update_time": 1686872052388,
    "creation_time": 1686761701458,
    "tags": {
      "mlflow.experiment.sourceType": "REPO_NOTEBOOK",
      "mlflow.ownerId": 3658755248564160,
      "mlflow.experiment.sourceName": "/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example",
      "mlflow.ownerEmail": "antoine.amend@databricks.com",
      "mlflow.experiment.sourceId": 3022585156450040
    },
    "_creation_time": "2023-06-14 16:55:01",
    "_last_update_time": "2023-06-15 23:34:12",
    "_tracking_uri": "databricks://e2_demo",
    "_web_ui_link": "https://e2-demo-west.cloud.databricks.com#mlflow/experiments/bf024d57582f4c8cbf816151cc6e1bac",
    "_api_link": "https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=bf024d57582f4c8cbf816151cc6e1bac"
  },
  "runs": [
    {
      "run": {
        "info": {
          "run_id": "76031d22c5464dd99431e426b939e800",
          "experiment_id": "bf024d57582f4c8cbf816151cc6e1bac",
          "run_name": "credit adjudication",
          "status": "FINISHED",
          "start_time": 1686872052388,
   . . .
```

##### Usage

```
get-experiment --help

Options:
  --experiment-id-or-name TEXT  Experiment ID or name  [required]
  --get-runs BOOLEAN            Get runs.  [default: False]
  --get-permissions BOOLEAN     Get Databricks permissions.  [default: False]
  --artifact-max-level INTEGER  Number of artifact levels to recurse for run
                                artifacts.  [default: -1]
  --get-raw BOOLEAN             Preserve raw JSON as received from API call.
                                [default: False]
  --silent BOOLEAN              Do not display to stdout.  [default: False]
  --output-file TEXT            JSON output file.
```

### Get Model Version

Get model version.
* Get model version details and optionally its run.


Of interest are the derived enriched attributes:
* _reg_model_download_uri - Download URI for registry MLflow model
* _run_model_download_uri - Download URI for run MLflow model

Workspace Registry version - [sample](samples/databricks/mlflow_objects/model_versions/credit_adjudication.json).

```
get-model-version \
  --registered-model credit_adjudication \
  --version 3
```
```
{
  "model_version": {
    "name": "credit_adjudication",
    "version": "3",
    "creation_timestamp": 1686872066253,
    "last_updated_timestamp": 1686872073462,
    "user_id": "antoine.amend@databricks.com",
    "current_stage": "Production",
    "description": "This version of credit adjudication model was built for the purpose of DAIS summit demo. \nModel was co-developped between EY and Databricks, finding XGBClassifier as best fit model trained against 50 different experiments.\nAll experiments are tracked and available on MLFlow experiment tracker.",
    "source": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model",
    "run_id": "76031d22c5464dd99431e426b939e800",
    "status": "READY",
    "tags": {
      "Model complexity": "MEDIUM",
      "Model explainability": "MEDIUM",
      "Model selection": "HYPEROPT",
      "Model type": "XGBClassifier"
    },
    "_web_ui_link": "https://e2-demo-west.cloud.databricks.com#mlflow/models/credit_adjudication/versions/3",
    "_api_link": "https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=credit_adjudication&version=3",
    "_creation_timestamp": "2023-06-15 23:34:26",
    "_last_updated_timestamp": "2023-06-15 23:34:33",
    "_reg_model_download_uri": "dbfs:/databricks/mlflow-registry/417e414731e74e03b731fb3a63a3b4e4/models/model",
    "_run_model_download_uri": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model"
  },
```

Unity Catalog Registry version [sample](samples/databricks/mlflow_objects/model_versions/uc/credit_adjudication.json).
```
get-model-version \
  --registered-model andre.ml_models.credit_adjudication \
  --version 1
```
```
{
  "model_version": {
    "name": "andre.ml_models2.credit_adjudication",
    "version": "1",
    "creation_timestamp": 1689279694436,
    "last_updated_timestamp": 1689279695182,
    "user_id": "andre@mycompany.com",
    "description": "This version of credit adjudication model was built for the purpose of DAIS summit demo. \nModel was co-developped between EY and Databricks, finding XGBClassifier as best fit model trained against 50 different experiments.\nAll experiments are tracked and available on MLFlow experiment tracker.",
    "source": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model",
    "run_id": "76031d22c5464dd99431e426b939e800",
    "run_tracking_server_id": "2556758628403379",
    "status": "READY",
    "storage_location": "s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/117583dc-67c2-483e-b862-8191b6f38519/versions/5099810b-e591-436a-949d-141d729da9b0",
    "_creation_timestamp": "2023-07-13 20:21:34",
    "_last_updated_timestamp": "2023-07-13 20:21:35",
    "_is_unity_catalog": true,
    "_reg_model_download_uri": "s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/117583dc-67c2-483e-b862-8191b6f38519/versions/5099810b-e591-436a-949d-141d729da9b0",
    "_run_model_download_uri": "dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model",
    "_web_ui_link": "https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.ml_models2.credit_adjudication/version/1",
    "_api_link": "https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/model-versions/get?name=andre.ml_models2.credit_adjudication&version=1"
  }
}
```


##### Usage

```
get-model-version --help

Options:
  --registered-model TEXT       Registered model name.  [required]
  --version TEXT                Model version.  [required]
  --get-expanded BOOLEAN        Get all objects associated with model version
                                [default: False]
  --artifact-max-level INTEGER  Number of artifact levels to recurse for run
                                artifacts.  [default: -1]
  --get-raw BOOLEAN             Preserve raw JSON as received from API call.
                                [default: False]
  --silent BOOLEAN              Do not display to stdout.  [default: False]
  --output-file TEXT            JSON output file.
```

### Get Registered Model

Get registered model details.
* Get registered model and its current version stages. Optionally get the  run for each version.
* [Sample JSON](samples/databricks/mlflow_objects/registered_models/credit_adjudication.json).

```
get-registered-model \
  --registered-model credit_adjudication \
  --get-versions
```
```
{
  "registered_model": {
    "name": "credit_adjudication",
    "creation_timestamp": 1686870883318,
    "last_updated_timestamp": 1686872073462,
    "user_id": "antoine.amend@databricks.com",
    "versions": [
      {
        "name": "credit_adjudication",
        "version": "2",
        "creation_timestamp": 1686871509181,
```

##### Usage

```
get-registered-model --help

Options:
  --registered-model TEXT        Registered model name.  [required]
  --get-run BOOLEAN              Get run.  [default: False]
  --artifact-max-level INTEGER   Number of artifact levels to recurse for run
                                 artifacts.  [default: -1]
  --get-versions BOOLEAN         Get model versions.  [default: False]
  --get-latest-versions BOOLEAN  Get model latest versions.  [default: False]
  --get-permissions BOOLEAN      Get Databricks permissions.  [default: False]
  --get-raw BOOLEAN              Preserve raw JSON as received from API call.
                                 [default: False]
  --silent BOOLEAN               Do not display to stdout.  [default: False]
  --output-file TEXT             JSON output file.
```

### Get Model Serving Endpoint 

Get Databricks model serving endpoint details.

```
get-model-serving-endpoint \
  --endpoint sklearn_wine_best \
  --openapi True \
  --output-file sklearn_wine_best.json
```
```
{
  "name": "sklearn_wine_best",
  "creator": "andre@my-company.com",
  "creation_timestamp": 1706467706000,
  "last_updated_timestamp": 1706467706000,
  "state": {
    "ready": "READY",
    "config_update": "NOT_UPDATING"
  },
  "config": {
    "served_entities": [
      {
        "name": "Sklearn_Wine_best-2",
        "entity_name": "Sklearn_Wine_best",
        "entity_version": "2",
        "workload_size": "Small",
        "scale_to_zero_enabled": true,
        "workload_type": "CPU",
        "state": {
          "deployment": "DEPLOYMENT_READY",
          "deployment_state_message": "Scaled to zero"
        },
        "creator": "andre@my-company.com",
        "creation_timestamp": 1706467706000,
        "_creation_timestamp": "2024-01-28 18:48:26"
      }
    ],
    "traffic_config": {
      "routes": [
        {
          "served_model_name": "Sklearn_Wine_best-2",
```

##### Usage

```
get-model-serving-endpoint --help

Options:
  --endpoint TEXT                 Model serving endpoint name.
  --openapi BOOLEAN               Get endpoint OpenAPI schema and append it to
                                  the output JSON.
  --use-deployment-client BOOLEAN
                                  Databricks only. Use
                                  DatabricksDeploymentClient. Otherwise, make
                                  direct calls to 'api/2.0/serving-endpoints'.
  --get-raw BOOLEAN               Preserve raw JSON as received from API call.
                                  [default: False]
  --output-file TEXT              JSON output file.
  --silent BOOLEAN                Do not display to stdout.  [default: False]
  --expand-model-version [none|version|version-and-signature|version-all]
                                  Model type: version|version-and-
                                  signature|version-all
```


## List Objects

### List Registered Models

List registered models.

```
list-registered-models \
  --columns name,user_id,creation_timestamp

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

##### Usage
```
list-registered-models --help

Options:
  --filter TEXT                   Model filter.
  --get-tags-and-aliases BOOLEAN  Get tags and aliases attribute from
                                  registered model.
  --unity-catalog BOOLEAN         Use Databricks Unity Catalog.
  --prefix TEXT                   Model prefix to show.
  --columns TEXT                  Columns to display. Comma delimited.
  --output-file-base TEXT         File base for JSON and CSV output files. For
                                  example, 'out' will result in 'out.csv' and
                                  'out.json.'  [default: out]
```


### List Model Versions

List model versions.

```
list-model-versions \
  --columns name,version,user_id,creation_timestamp

+-----------------------------------------+-----------+--------------------------+----------------------+
| name                                    |   version | user_id                  | creation_timestamp   |
+-----------------------------------------+-----------+--------------------------+----------------------+
| andre.basic_models.copy_test            |         1 | sagarmatha@mycompany.com | 2023-10-09 20:48:51  |
| andre.basic_models.mini_mlops_pipeline  |         1 | k2@mycompany.com         | 2023-10-06 06:14:27  |
| andre.basic_models.xgboost_wine_best    |         1 | karakoram@mycompany.com  | 2023-08-16 05:34:57  |
| andre.basic_models.sklearn_wine_champ   |         1 | denali@mycompany.com     | 2023-09-19 23:01:56  |
| andre.basic_models.sklearn_wine_champ   |         9 | denali@mycompany.com     | 2023-11-26 20:01:56  |
| andre.basic_models.sklearn_wine_test_fs |         1 | chimborazo@mycompany.com | 2023-08-17 14:55:30  |
| market.llm_models.mistral7b_instruct    |         1 | huascaran@mycompany.com  | 2023-08-16 06:38:53  |
| market.llm_models.codellama-7b          |         1 | denali@mycompany.com     | 2023-08-11 14:38:18  |
+-----------------------------------------+-----------+--------------------------+----------------------+
```

##### Usage
```
list-model-versions  --help

Options:
  --filter TEXT                   Model filter.
  --get-tags-and-aliases BOOLEAN  Get tags and aliases attribute from
                                  registered model.
  --get-model-details BOOLEAN     Get MLflow model flavor and size.
  --unity-catalog BOOLEAN         Use Databricks Unity Catalog.
  --columns TEXT                  Columns to display. Comma delimited.
  --output-file-base TEXT         File base for JSON and CSV output files. For
                                  example, 'out' will result in 'out.csv' and
                                  'out.json.'  [default: out]
  --help                          Show this message and exit.
```


### List Model Serving Endpoints

List Databricks model serving endpoints.

```
list-model-serving-endpoints \
  --columns name,endpoint_type,task,creator,creation_timestamp \
  --output-file-base endpoints
```

```
| name                             | endpoint_type        | task               | creator                 | creation_timestamp   |
|----------------------------------|----------------------|--------------------|-------------------------|----------------------|
| embeddings_proxy_eo              |                      |                    | amelia@mycompany.com    | 2023-11-22 18:36:33  |
| eo_rfp_rag                       |                      |                    | amelia@mycompany.com    | 2023-11-22 19:00:33  |
| databricks-llama-2-70b-chat      | FOUNDATION_MODEL_API | llm/v1/chat        |                         | 2023-11-10 09:53:20  |
| databricks-mixtral-8x7b-instruct | FOUNDATION_MODEL_API | llm/v1/chat        |                         | 2023-11-10 09:53:20  |
| databricks-bge-large-en          | FOUNDATION_MODEL_API | llm/v1/embeddings  |                         | 2023-11-10 09:53:20  |
| databricks-mpt-30b-instruct      | FOUNDATION_MODEL_API | llm/v1/completions |                         | 2023-11-10 09:53:20  |
| databricks-mpt-7b-instruct       | FOUNDATION_MODEL_API | llm/v1/completions |                         | 2023-11-10 09:53:20  |
| openai-completions-endpoint      | EXERNAL_MODEL        | llm/v1/completions | k1.denali@mycompany.com | 2024-05-10 19:03:00  |
```

##### Usage
```
Options:
  --model-type [all|custom|foundation|external]
                                  Model type: all|custom|foundation|external
  --openapi BOOLEAN               Write OpenAPI schema for all endpoints to
                                  file '{output-file-base}_opena[i.json'.
  --columns TEXT                  Columns to display. Comma delimited.
  --output-file-base TEXT         File base for JSON and CSV output files. For
                                  example, 'out' will result in 'out.csv' and
                                  'out.json.'  [default: out]
  --use-deployment-client BOOLEAN
                                  Databricks only. Use
                                  DatabricksDeploymentClient. Otherwise, make
                                  direct calls to 'api/2.0/serving-endpoints'.
  --get-raw BOOLEAN               Preserve raw JSON as received from API call.
                                  [default: False]
  --get-details BOOLEAN           Get details of each listed object.
  --normalize-pandas-df BOOLEAN   Convert JSON list with pd.json_normalize,
                                  otherwise use pd.DataFrame.
```


## Enriched Objects 
XX TODO REMOVE

### Run

| Attribute        | Note                                                           |
|------------------|----------------------------------------------------------------|
| _start_time      | formatted version of start_time                                |
| _end_time        | ibid                                                           |
| _duration        | diffence between start_time and end_time                       |
| _experiment_name | name of the experiment - complements experiment_id attribute |
| _web_ui_link     | Link to the web UI object                                      |
| _api_link        | Link to the API object                                         |

### Experiment

| Attribute        | Note                                                           |
|------------------|----------------------------------------------------------------|
| _creation_time   | formatted version of creation_time                             |
| _last_update_time| _last_update_time                                              |
| _web_ui_link     | Link to the web UI object                                      |
| _api_link        | Link to the API object                                         |

### Model Version

| Attribute        | Note                                                           |
|------------------|----------------------------------------------------------------|
| _creation_timestamp     | formatted version of _creation_timestamp                       |
| _last_updated_timestamp | ibid                                                           |
| _reg_model_download_uri | Download URI of registered model                               |
| _run_model_download_uri | Download URI of run  model                               |
| _web_ui_link            | Link to the web UI object                                      |
| _api_link               | Link to the API object                                         |


### Registered Model

| Attribute        | Note                                                           |
|------------------|----------------------------------------------------------------|
| _creation_timestamp     | formatted version of _creation_timestamp                       |
| _last_updated_timestamp | ibid                                                           |
| _web_ui_link            | Link to the web UI object                                      |
| _api_link               | Link to the API object                                         |


## JSON Response format

The returned format is an "enriched" format of the original raw JSON response.
Enhanced attribute details can be found in the [Enriched Objects](#enriched-objects) section at the end.

The enriched object has the following enhancements:
- Adds enhanced attributes starting with an underscore such as `_start_time`.
- Explodes tags containing a stringified JSON value (such as run tag `mlflow.log-model.history`) into the actual JSON reprentation.

There are two types of enhanced attributes:
* Formatted versions of the original attribute. For example:
  * `"_start_time": "2023-06-15 23:34:12"` represents `"start_time": 1686872052388`.
  * All formatted times are UTC.
* Derived attributes. New attributes of interest such as `_duration` (for Run Info) or `_web_ui_link`.

Each enhanced object returns the target MLflow object as a sub-object of the top-level JSON document.
This is consistent with the MLflow API response format.
For example, the response for a run is:
```
{
  "run": {
    "info": {
      "run_id": "76031d22c5464dd99431e426b939e800",
      "start_time": 1686872052388,
      "_start_time": "2023-06-15 23:34:12" ,
      "_duration": 3.823,
      "_web_ui_link": "https://e2-demo-west.cloud.databricks.com#mlflow/experiments/bf024d57582f4c8cbf816151cc6e1bac/runs/76031d22c5464dd99431e426b939e800",
      "_api_link": "https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=76031d22c5464dd99431e426b939e800"
    },
    }
  }
}
```
