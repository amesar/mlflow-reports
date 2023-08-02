
MLflow Model: _models:/Conversational_Task/6_
=============================================

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
|model_uri|models:/Conversational_Task/6|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|1,653,817,109|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|False|
|time_created|2023-07-31 20:22:38|
|report_time|2023-08-02 08:52:06|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/Conversational_Task/6|
|run_uri|runs:/eb31972425fc4fd19fa6c30a30a53f5c/chatbot|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/148bd63ab3364fa986aa74c8cd6c1383/models/chatbot|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/eb31972425fc4fd19fa6c30a30a53f5c/artifacts/chatbot|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|chatbot|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|8fb957e95f094ca287187544b2e07088|
|run_id|eb31972425fc4fd19fa6c30a30a53f5c|
|utc_time_created|2023-07-31 20:22:38.046197|

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
|instance_type|ConversationalPipeline|
|model_binary|model|
|pipeline_model_type|GPT2LMHeadModel|
|source_model_name|microsoft/DialoGPT-medium|
|task|conversational|
|tokenizer_type|GPT2TokenizerFast|
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
|name|Conversational_Task|
|creation_timestamp|1690751148165|
|last_updated_timestamp|1690834984390|
|user_id|andre@mycompany.com|
|id|baeb4ab1e44248ac9c9a06953e8b6ba4|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-07-30 21:05:48|
|_last_updated_timestamp|2023-07-31 20:23:04|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Conversational_Task|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=Conversational_Task|

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
    "object_id": "/registered-models/baeb4ab1e44248ac9c9a06953e8b6ba4",
    "object_type": "registered-model",
    "access_control_list": [
      {
        "user_name": "andre@mycompany.com",
        "display_name": "Andre",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": false
          }
        ]
      },
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
      }
    ]
  }
}

```
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|Conversational_Task|
|version|6|
|creation_timestamp|1690834984390|
|last_updated_timestamp|1690835028924|
|user_id|andre@mycompany.com|
|current_stage|None|
|source|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/eb31972425fc4fd19fa6c30a30a53f5c/artifacts/chatbot|
|run_id|eb31972425fc4fd19fa6c30a30a53f5c|
|status|READY|
|_creation_timestamp|2023-07-31 20:23:04|
|_last_updated_timestamp|2023-07-31 20:23:49|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/148bd63ab3364fa986aa74c8cd6c1383/models/chatbot|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/eb31972425fc4fd19fa6c30a30a53f5c/artifacts/chatbot|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Conversational_Task/versions/6|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=Conversational_Task&version=6|

## Tags
  

|Name|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['tokenizer']|
|hf_framework|pt|
|hf_instance_type|ConversationalPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|GPT2LMHeadModel|
|hf_source_model_name|microsoft/DialoGPT-medium|
|hf_task|conversational|
|hf_tokenizer_type|GPT2TokenizerFast|
|hf_transformers_version|4.28.1|

# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|eb31972425fc4fd19fa6c30a30a53f5c|
|run_uuid|eb31972425fc4fd19fa6c30a30a53f5c|
|experiment_id|7f1bb46d81ec48a7b627ad762ece5091|
|run_name|sassy-yak-535|
|status|FINISHED|
|start_time|1690834957453|
|end_time|1690834982817|
|artifact_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/eb31972425fc4fd19fa6c30a30a53f5c/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-31 20:22:37|
|_end_time|2023-07-31 20:23:03|
|_duration|25.364|
|_experiment_name|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/7f1bb46d81ec48a7b627ad762ece5091/runs/eb31972425fc4fd19fa6c30a30a53f5c|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=eb31972425fc4fd19fa6c30a30a53f5c|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Git Repo Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.gitRepoCommit|2d731bf2807e4d5a60d3c5716f804924cb2b6595|
|mlflow.databricks.gitRepoProvider|gitHub|
|mlflow.databricks.gitRepoReference|master|
|mlflow.databricks.gitRepoReferenceType|branch|
|mlflow.databricks.gitRepoRelativePath|databricks/notebooks/llm_transformers/Conversational_Task|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/amesar/mlflow-examples|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|4690959327746967301_6375313457873527453_job-25390808787695-run-1-action-6402759384767584|
|mlflow.databricks.notebookID|3428923814211678|
|mlflow.databricks.notebookPath|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Conversational_Task|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0414-154233-qm0df4rx|
|mlflow.databricks.cluster.info|{'cluster_name': 'andre_ML_13.2', 'spark_version': '13.1.x-cpu-ml-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'num_workers': 1}|
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
|mlflow.source.name|jobs/25390808787695/run/1|
|mlflow.source.type|JOB|

### Job Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.jobID|25390808787695|
|mlflow.databricks.jobRunID|1|
|mlflow.databricks.jobType|notebook|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'chatbot', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'conversational', 'framework': 'pt', 'source_model_name': 'microsoft/DialoGPT-medium', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'GPT2TokenizerFast', 'pipeline_model_type': 'GPT2LMHeadModel', 'instance_type': 'ConversationalPipeline', 'transformers_version': '4.28.1'}}, 'run_id': 'eb31972425fc4fd19fa6c30a30a53f5c', 'model_uuid': '8fb957e95f094ca287187544b2e07088', 'utc_time_created': '2023-07-31 20:22:38.046197', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|sassy-yak-535|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['tokenizer']|
|hf_framework|pt|
|hf_instance_type|ConversationalPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|GPT2LMHeadModel|
|hf_source_model_name|microsoft/DialoGPT-medium|
|hf_task|conversational|
|hf_tokenizer_type|GPT2TokenizerFast|
|hf_transformers_version|4.28.1|

### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0414-154233-qm0df4rx|
|cluster_name|andre_ML_13.2|
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
|experiment_id|7f1bb46d81ec48a7b627ad762ece5091|
|name|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|artifact_location|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091|
|lifecycle_stage|active|
|last_update_time|1690835135484|
|creation_time|1690834775450|
|_creation_time|2023-07-31 20:19:35|
|_last_update_time|2023-07-31 20:25:35|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/7f1bb46d81ec48a7b627ad762ece5091|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=7f1bb46d81ec48a7b627ad762ece5091|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.experiment.sourceType|REPO_NOTEBOOK|
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experiment.sourceId|3428923814211678|

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
    "error": "{\"http_status_code\": 400, \"uri\": \"https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/7f1bb46d81ec48a7b627ad762ece5091\", \"params\": null, \"response\": \"{\\\"error_code\\\":\\\"INVALID_PARAMETER_VALUE\\\",\\\"message\\\":\\\"For input string: \\\\\\\"7f1bb46d81ec48a7b627ad762ece5091\\\\\\\"\\\"}\"}"
  }
}

```