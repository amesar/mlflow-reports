
MLflow Model: _models:/andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model/1_
====================================================================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
* [Registered Model Version](#registered-model-version)
	* [Details](#details)
	* [Tags](#tags)
* [Registered Model](#registered-model)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)
* [Run](#run)
	* [Info](#info)
	* [Params](#params)
	* [Metrics](#metrics)
	* [Inputs](#inputs)
	* [Tags](#tags)
* [Experiment](#experiment)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)

# Model Overview
  
<b><font size="+1">MLflow Model</font></b>  

|Name|Value|
| :--- | :--- |
|model_uri|models:/andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model/1|
|flavor|mlflow.langchain|
|flavor_version|0.1.5|
|mlflow_version|2.10.1|
|size_bytes|4,933|
|databricks_runtime|14.3.x-scala2.12|
|is_unity_catalog|True|
|time_created|2024-04-03 22:31:47|
|report_time|2024-04-06 13:05:53|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model/1|
|run_uri|runs:/18dc31e683ef49cca8c9145c8bd7ad4d/chain|
|reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/6c58bfab-a25d-4d1b-853c-31e7da7aff63/versions/e4e6a4b5-94b7-4bb1-838e-f3e90e9cb795|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/4049278270812513/18dc31e683ef49cca8c9145c8bd7ad4d/artifacts/chain|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|chain|
|databricks_runtime|14.3.x-scala2.12|
|mlflow_version|2.10.1|
|model_size_bytes|4933|
|model_uuid|45beacdfafe04f9f813ee9927e6332a9|
|run_id|18dc31e683ef49cca8c9145c8bd7ad4d|
|utc_time_created|2024-04-03 22:31:47.053117|
|model_flavor|langchain|

### Flavors

#### Flavor 'langchain'
  

|Name|Value|
| :--- | :--- |
|code|None|
|langchain_version|0.1.5|
|loader_arg|retriever|
|loader_fn|loader_fn.pkl|
|model_data|model.yaml|
|model_load|base_load|
|model_type|RetrievalQA|

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_arg|retriever|
|loader_fn|loader_fn.pkl|
|loader_module|mlflow.langchain|
|model_data|model.yaml|
|model_load|base_load|
|python_version|3.10.12|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|query|string|

### Outputs
  

|Type name|Type value|
| :--- | :--- |
|string|None|

## Saved input example info
  

|Name|Value|
| :--- | :--- |
|artifact_path|input_example.json|
|pandas_orient|split|
|type|dataframe|

# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model|
|version|1|
|creation_timestamp|1712183509293|
|last_updated_timestamp|1712183510541|
|user_id|andre@mycompany.com|
|source|dbfs:/databricks/mlflow-tracking/4049278270812513/18dc31e683ef49cca8c9145c8bd7ad4d/artifacts/chain|
|run_id|18dc31e683ef49cca8c9145c8bd7ad4d|
|run_tracking_server_id|1444828305810485|
|status|READY|
|storage_location|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/6c58bfab-a25d-4d1b-853c-31e7da7aff63/versions/e4e6a4b5-94b7-4bb1-838e-f3e90e9cb795|
|_creation_timestamp|2024-04-03 22:31:49|
|_last_updated_timestamp|2024-04-03 22:31:51|
|_is_unity_catalog|True|
|_reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/6c58bfab-a25d-4d1b-853c-31e7da7aff63/versions/e4e6a4b5-94b7-4bb1-838e-f3e90e9cb795|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/4049278270812513/18dc31e683ef49cca8c9145c8bd7ad4d/artifacts/chain|
|_web_ui_link|https://e2-demo-field-eng.cloud.databricks.com/explore/data/models/andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model/version/1|
|_api_link|https://e2-demo-field-eng.cloud.databricks.com/api/2.0/mlflow/unity-catalog/model-versions/get?name=andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model|
|creation_timestamp|1712183508966|
|last_updated_timestamp|1712183509298|
|user_id|andre@mycompany.com|
|_creation_timestamp|2024-04-03 22:31:49|
|_last_updated_timestamp|2024-04-03 22:31:49|
|_is_unity_catalog|True|
|_web_ui_link|https://e2-demo-field-eng.cloud.databricks.com/explore/data/models/andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model|
|_api_link|https://e2-demo-field-eng.cloud.databricks.com/api/2.0/mlflow/unity-catalog/registered-models/get?name=andre.rag_chatbot_2024_04_03.dbdemos_chatbot_model|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permissions": {},
  "effective_permissions": {
    "privilege_assignments": [
      {
        "principal": "account users",
        "privileges": [
          {
            "privilege": "ALL_PRIVILEGES",
            "inherited_from_type": "CATALOG",
            "inherited_from_name": "andre"
          }
        ]
      },
      {
        "principal": "global_read_test",
        "privileges": [
          {
            "privilege": "EXECUTE",
            "inherited_from_type": "CATALOG",
            "inherited_from_name": "andre"
          }
        ]
      }
    ]
  }
}

```
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|18dc31e683ef49cca8c9145c8bd7ad4d|
|run_uuid|18dc31e683ef49cca8c9145c8bd7ad4d|
|experiment_id|4049278270812513|
|run_name|dbdemos_chatbot_rag|
|status|FINISHED|
|start_time|1712183505897|
|end_time|1712183510598|
|artifact_uri|dbfs:/databricks/mlflow-tracking/4049278270812513/18dc31e683ef49cca8c9145c8bd7ad4d/artifacts|
|lifecycle_stage|active|
|_start_time|2024-04-03 22:31:46|
|_end_time|2024-04-03 22:31:51|
|_duration|4.701|
|_experiment_name|/Users/andre@mycompany.com/dbdemos/llm-rag-chatbot/01-quickstart/02-Deploy-RAG-Chatbot-Model|
|_web_ui_link|https://e2-demo-field-eng.cloud.databricks.com#mlflow/experiments/4049278270812513/runs/18dc31e683ef49cca8c9145c8bd7ad4d|
|_api_link|https://e2-demo-field-eng.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=18dc31e683ef49cca8c9145c8bd7ad4d|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|8341251633097086004_5809708659006606177_fe02547f98234e1facb6bb16427ba393|
|mlflow.databricks.notebookID|4049278270812513|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/dbdemos/llm-rag-chatbot/01-quickstart/02-Deploy-RAG-Chatbot-Model|
|mlflow.databricks.notebookRevisionID|1712183510905|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0403-213426-y1oo3e26|
|mlflow.databricks.cluster.info|{'cluster_name': 'dbdemos-llm-rag-chatbot-andre', 'spark_version': '14.3.x-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'autoscale': {'min_workers': 2, 'max_workers': 4, 'target_workers': 2}}|
|mlflow.databricks.cluster.libraries|{'installable': [], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://denali.staging.mycompany.com|
|mlflow.databricks.workspaceID|1444828305810485|
|mlflow.databricks.workspaceURL|e2-demo-field-eng.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Users/andre@mycompany.com/dbdemos/llm-rag-chatbot/01-quickstart/02-Deploy-RAG-Chatbot-Model|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'chain', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string', 'name': 'query', 'required': True}], 'outputs': [{'type': 'string', 'required': True}], 'params': None}, 'flavors': {'python_function': {'model_load': 'base_load', 'model_data': 'model.yaml', 'loader_arg': 'retriever', 'loader_module': 'mlflow.langchain', 'loader_fn': 'loader_fn.pkl', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}, 'python_version': '3.10.12'}, 'langchain': {'model_load': 'base_load', 'langchain_version': '0.1.5', 'model_data': 'model.yaml', 'loader_arg': 'retriever', 'code': None, 'model_type': 'RetrievalQA', 'loader_fn': 'loader_fn.pkl'}}, 'run_id': '18dc31e683ef49cca8c9145c8bd7ad4d', 'model_uuid': '45beacdfafe04f9f813ee9927e6332a9', 'model_size_bytes': 3648, 'utc_time_created': '2024-04-03 22:31:47.053117', 'mlflow_version': '2.10.1', 'databricks_runtime': '14.3.x-scala2.12'}]|
|mlflow.runName|dbdemos_chatbot_rag|
|mlflow.user|andre@mycompany.com|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0403-213426-y1oo3e26|
|cluster_name|dbdemos-llm-rag-chatbot-andre|
|spark_version|14.3.x-scala2.12|
|node_type_id|i3.xlarge|
|driver_node_type_id|i3.xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_count': 0}|
|autoscale|{'min_workers': 2, 'max_workers': 4, 'target_workers': 2}|

#### Cluster Libraries

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|4049278270812513|
|name|/Users/andre@mycompany.com/dbdemos/llm-rag-chatbot/01-quickstart/02-Deploy-RAG-Chatbot-Model|
|artifact_location|dbfs:/databricks/mlflow-tracking/4049278270812513|
|lifecycle_stage|active|
|last_update_time|1712183506096|
|creation_time|1712183506096|
|_creation_time|2024-04-03 22:31:46|
|_last_update_time|2024-04-03 22:31:46|
|_tracking_uri|databricks://e2_demo_fieldeng|
|_web_ui_link|https://e2-demo-field-eng.cloud.databricks.com#mlflow/experiments/4049278270812513|
|_api_link|https://e2-demo-field-eng.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=4049278270812513|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/dbdemos/llm-rag-chatbot/01-quickstart/02-Deploy-RAG-Chatbot-Model|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experimentType|NOTEBOOK|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the experiment"
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view, log runs, and edit the experiment"
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can view, log runs, edit, delete, and change permissions of the experiment"
    }
  ],
  "permissions": {
    "error": {
      "message": "Databricks permissions API call failed",
      "MlflowReportsException": {
        "http_status_code": 400,
        "uri": "https://e2-demo-field-eng.cloud.databricks.com/api/2.0/permissions/experiments/4049278270812513",
        "response": {
          "error_code": "INVALID_PARAMETER_VALUE",
          "message": "Object 4049278270812513 not a experiment."
        }
      }
    }
  }
}

```