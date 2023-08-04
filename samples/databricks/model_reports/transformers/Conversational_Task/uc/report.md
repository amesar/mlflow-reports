
MLflow Model: _models:/andre.transformer_models.Conversational_Task/1_
==============================================================================

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
|model_uri|models:/andre.transformer_models.Conversational_Task/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|1,653,817,109|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|True|
|time_created|2023-07-31 07:09:23|
|report_time|2023-07-31 20:31:34|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/andre.transformer_models.Conversational_Task/1|
|run_uri|runs:/75521dd2c66749d48c075feec9f19a4d/chatbot|
|reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/40b69ceb-a986-4d08-99db-971274964fc7/versions/e994cef2-0dc9-49d7-ab5d-84ce259243bb|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/f78ce06c2f86422db12e53c10ea4bebb/75521dd2c66749d48c075feec9f19a4d/artifacts/chatbot|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|chatbot|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|255737238a0b461aba1d933c55ce85df|
|run_id|75521dd2c66749d48c075feec9f19a4d|
|utc_time_created|2023-07-31 07:09:23.906110|

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
|name|andre.transformer_models.conversational_task|
|creation_timestamp|1690787423719|
|last_updated_timestamp|1690787423719|
|user_id|andre@mycompany.com|
|_creation_timestamp|2023-07-31 07:10:24|
|_last_updated_timestamp|2023-07-31 07:10:24|
|_is_unity_catalog|True|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.transformer_models.conversational_task|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/registered-models/get?name=andre.transformer_models.conversational_task|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permissions": {},
  "effective_permissions": {}
}

```
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|andre.transformer_models.conversational_task|
|version|1|
|creation_timestamp|1690787438504|
|last_updated_timestamp|1690787461880|
|user_id|andre@mycompany.com|
|source|dbfs:/databricks/mlflow-tracking/f78ce06c2f86422db12e53c10ea4bebb/75521dd2c66749d48c075feec9f19a4d/artifacts/chatbot|
|run_id|75521dd2c66749d48c075feec9f19a4d|
|run_tracking_server_id|2556758628403379|
|status|READY|
|storage_location|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/40b69ceb-a986-4d08-99db-971274964fc7/versions/e994cef2-0dc9-49d7-ab5d-84ce259243bb|
|_creation_timestamp|2023-07-31 07:10:39|
|_last_updated_timestamp|2023-07-31 07:11:02|
|_is_unity_catalog|True|
|_reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/40b69ceb-a986-4d08-99db-971274964fc7/versions/e994cef2-0dc9-49d7-ab5d-84ce259243bb|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/f78ce06c2f86422db12e53c10ea4bebb/75521dd2c66749d48c075feec9f19a4d/artifacts/chatbot|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.transformer_models.conversational_task/version/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/model-versions/get?name=andre.transformer_models.conversational_task&version=1|

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
|run_id|75521dd2c66749d48c075feec9f19a4d|
|run_uuid|75521dd2c66749d48c075feec9f19a4d|
|experiment_id|f78ce06c2f86422db12e53c10ea4bebb|
|run_name|gentle-newt-365|
|status|FINISHED|
|start_time|1690787363215|
|end_time|1690787422645|
|artifact_uri|dbfs:/databricks/mlflow-tracking/f78ce06c2f86422db12e53c10ea4bebb/75521dd2c66749d48c075feec9f19a4d/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-31 07:09:23|
|_end_time|2023-07-31 07:10:23|
|_duration|59.43|
|_experiment_name|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/f78ce06c2f86422db12e53c10ea4bebb/runs/75521dd2c66749d48c075feec9f19a4d|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=75521dd2c66749d48c075feec9f19a4d|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Git Repo Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.gitRepoCommit|6ed94d8331efe7c3fc8fb34673f97375e633b45c|
|mlflow.databricks.gitRepoProvider|gitHub|
|mlflow.databricks.gitRepoReference|master|
|mlflow.databricks.gitRepoReferenceType|branch|
|mlflow.databricks.gitRepoRelativePath|databricks/notebooks/llm_transformers/Conversational_Task|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/amesar/mlflow-examples|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|3707830929714222513_6827362440894771624_job-741100833025984-run-1-action-7787476391880310|
|mlflow.databricks.notebookID|3428923814203733|
|mlflow.databricks.notebookPath|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Conversational_Task|

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
|mlflow.source.name|jobs/741100833025984/run/1|
|mlflow.source.type|JOB|

### Job Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.jobID|741100833025984|
|mlflow.databricks.jobRunID|1|
|mlflow.databricks.jobType|notebook|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'chatbot', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'conversational', 'framework': 'pt', 'source_model_name': 'microsoft/DialoGPT-medium', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'GPT2TokenizerFast', 'pipeline_model_type': 'GPT2LMHeadModel', 'instance_type': 'ConversationalPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '75521dd2c66749d48c075feec9f19a4d', 'model_uuid': '255737238a0b461aba1d933c55ce85df', 'utc_time_created': '2023-07-31 07:09:23.906110', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|gentle-newt-365|
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
|experiment_id|f78ce06c2f86422db12e53c10ea4bebb|
|name|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|artifact_location|dbfs:/databricks/mlflow-tracking/f78ce06c2f86422db12e53c10ea4bebb|
|lifecycle_stage|active|
|last_update_time|1690787578561|
|creation_time|1690725104887|
|_creation_time|2023-07-30 13:51:45|
|_last_update_time|2023-07-31 07:12:59|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/f78ce06c2f86422db12e53c10ea4bebb|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=f78ce06c2f86422db12e53c10ea4bebb|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.experiment.sourceType|REPO_NOTEBOOK|
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experiment.sourceId|3428923814203733|

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
    "error": "{\"http_status_code\": 400, \"uri\": \"https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/f78ce06c2f86422db12e53c10ea4bebb\", \"params\": null, \"response\": \"{\\\"error_code\\\":\\\"INVALID_PARAMETER_VALUE\\\",\\\"message\\\":\\\"For input string: \\\\\\\"f78ce06c2f86422db12e53c10ea4bebb\\\\\\\"\\\"}\"}"
  }
}

```