
MLflow Model: _models:/hugging-face-transformers-batch-nlp/production_
======================================================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
* [Registered Model](#registered-model)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)
* [Registered Model Version](#registered-model-version)
	* [Details](#details)
	* [Tags](#tags)
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
|model_uri|models:/hugging-face-transformers-batch-nlp/production|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.4.1|
|size_bytes|1,637,529,598|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|time_created|2023-06-12 20:47:29|
|report_time|2023-07-06 05:14:34|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/hugging-face-transformers-batch-nlp/production|
|run_uri|runs:/38c0395ef5694d6aae3766cf3e1731e9/pipeline|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/e2855a52ab164fc08bdbac7407498e9e/models/pipeline|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3336498746253572/38c0395ef5694d6aae3766cf3e1731e9/artifacts/pipeline|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|pipeline|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.4.1|
|model_uuid|0d4a99f1bfe643aab0076b14d6361193|
|run_id|38c0395ef5694d6aae3766cf3e1731e9|
|utc_time_created|2023-06-12 20:47:29.862183|

### Flavors

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|mlflow.transformers|
|model_binary|model|
|python_version|3.10.6|

#### Flavor 'transformers'
  

|Name|Value|
| :--- | :--- |
|code|None|
|components|['tokenizer']|
|framework|pt|
|instance_type|SummarizationPipeline|
|model_binary|model|
|pipeline_model_type|BartForConditionalGeneration|
|source_model_name|sshleifer/distilbart-cnn-12-6|
|task|summarization|
|tokenizer_type|BartTokenizerFast|
|transformers_version|4.28.1|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|None|string|

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

# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|hugging-face-transformers-batch-nlp|
|creation_timestamp|1686617557318|
|last_updated_timestamp|1686620082200|
|user_id|andre@mycompany.com|
|id|d29dd50e93124958a9baea4e70cbe4a5|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-06-13 00:52:37|
|_last_updated_timestamp|2023-06-13 01:34:42|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/hugging-face-transformers-batch-nlp|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=hugging-face-transformers-batch-nlp|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the details of the registered model and its model versions, and use the model versions."
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view and edit the details of a registered model and its model versions (except stage changes), and add new model versions."
    },
    {
      "permission_level": "CAN_MANAGE_STAGING_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between non-Production stages."
    },
    {
      "permission_level": "CAN_MANAGE_PRODUCTION_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between any stages."
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can manage permissions on, view all details of, and perform all actions on the registered model and its model versions."
    }
  ],
  "permissions": {
    "object_id": "/registered-models/d29dd50e93124958a9baea4e70cbe4a5",
    "object_type": "registered-model",
    "access_control_list": [
      {
        "group_name": "admins",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "group_name": "users",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "service-principal-e2-demo-west-ws-do-not-delete",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "user_name": "andre@mycompany.com",
        "display_name": "Andre",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": false
          }
        ]
      }
    ]
  }
}

```
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|hugging-face-transformers-batch-nlp|
|version|1|
|creation_timestamp|1686617557588|
|last_updated_timestamp|1686620082200|
|user_id|andre@mycompany.com|
|current_stage|Production|
|source|dbfs:/databricks/mlflow-tracking/3336498746253572/38c0395ef5694d6aae3766cf3e1731e9/artifacts/pipeline|
|run_id|38c0395ef5694d6aae3766cf3e1731e9|
|status|READY|
|_creation_timestamp|2023-06-13 00:52:38|
|_last_updated_timestamp|2023-06-13 01:34:42|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/e2855a52ab164fc08bdbac7407498e9e/models/pipeline|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3336498746253572/38c0395ef5694d6aae3766cf3e1731e9/artifacts/pipeline|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/hugging-face-transformers-batch-nlp/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=hugging-face-transformers-batch-nlp&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|38c0395ef5694d6aae3766cf3e1731e9|
|run_uuid|38c0395ef5694d6aae3766cf3e1731e9|
|experiment_id|3336498746253572|
|run_name|placid-bee-827|
|status|FINISHED|
|start_time|1686602849523|
|end_time|1686602916915|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3336498746253572/38c0395ef5694d6aae3766cf3e1731e9/artifacts|
|lifecycle_stage|active|
|_start_time|2023-06-12 20:47:30|
|_end_time|2023-06-12 20:48:37|
|_duration|67.392|
|_experiment_name|/Users/andre@mycompany.com/mlflow/LLM/hugging-face-transformers-batch-nlp|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3336498746253572/runs/38c0395ef5694d6aae3766cf3e1731e9|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=38c0395ef5694d6aae3766cf3e1731e9|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|4809640544888678053_9017383041795826674_1f9049ebbdf34df8999de112725e62c9|
|mlflow.databricks.notebookID|3336498746253572|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/transformers/hugging-face-transformers-batch-nlp|
|mlflow.databricks.notebookRevisionID|1686602917274|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0414-154233-qm0df4rx|
|mlflow.databricks.cluster.info|{'cluster_name': 'andre_ML_13.1', 'spark_version': '13.1.x-cpu-ml-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'num_workers': 1}|
|mlflow.databricks.cluster.libraries|{'installable': [{'jar': 'dbfs:/home/andre@mycompany.com/lib/jars/PrintArgs.jar'}, {'whl': 'dbfs:/home/andre@mycompany.com/work/jobs/sklearn_wine/mlflow_sklearn_wine-0.0.1-py3-none-any.whl'}], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|
|mlflow.databricks.workspaceID|2556758628403379|
|mlflow.databricks.workspaceURL|e2-demo-west.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/transformers/hugging-face-transformers-batch-nlp|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'pipeline', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'summarization', 'framework': 'pt', 'source_model_name': 'sshleifer/distilbart-cnn-12-6', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'BartTokenizerFast', 'pipeline_model_type': 'BartForConditionalGeneration', 'instance_type': 'SummarizationPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '38c0395ef5694d6aae3766cf3e1731e9', 'model_uuid': '0d4a99f1bfe643aab0076b14d6361193', 'utc_time_created': '2023-06-12 20:47:29.862183', 'mlflow_version': '2.4.1', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|placid-bee-827|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|sparkDatasourceInfo|[{'path': 'dbfs:/databricks-datasets/wikipedia-datasets/data-001/en_wikipedia/articles-only-parquet', 'format': 'parquet'}]|

### Exploded Tags

#### Spark Datasources
  

|Format|Version|Path|
| :--- | :--- | :--- |
|parquet||dbfs:/databricks-datasets/wikipedia-datasets/data-001/en_wikipedia/articles-only-parquet|

#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0414-154233-qm0df4rx|
|cluster_name|andre_ML_13.1|
|spark_version|13.1.x-cpu-ml-scala2.12|
|node_type_id|i3.xlarge|
|driver_node_type_id|i3.xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_count': 0}|
|num_workers|1|

#### Cluster Libraries

##### Installable Libraries
  

|Name|Value|
| :--- | :--- |
|jar|dbfs:/home/andre@mycompany.com/lib/jars/PrintArgs.jar|
|whl|dbfs:/home/andre@mycompany.com/work/jobs/sklearn_wine/mlflow_sklearn_wine-0.0.1-py3-none-any.whl|

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|3336498746253572|
|name|/Users/andre@mycompany.com/mlflow/LLM/hugging-face-transformers-batch-nlp|
|artifact_location|dbfs:/databricks/mlflow-tracking/3336498746253572|
|lifecycle_stage|active|
|last_update_time|1686602849523|
|creation_time|1686598571971|
|_creation_time|2023-06-12 19:36:12|
|_last_update_time|2023-06-12 20:47:30|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3336498746253572|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3336498746253572|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/mlflow/LLM/hugging-face-transformers-batch-nlp|
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
    "error": "HTTP status code: 400. Reason: Bad Request URL: https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/3336498746253572. Params: None. Text: {\"error_code\":\"INVALID_PARAMETER_VALUE\",\"message\":\"Object 3336498746253572 not a experiment.\"}"
  }
}

```