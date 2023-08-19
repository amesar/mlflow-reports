
MLflow Model: _models:/Speech_Recognition_Task/1_
=================================================

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
|model_uri|models:/Speech_Recognition_Task/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|154,431,670|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|False|
|time_created|2023-07-31 20:25:36|
|report_time|2023-08-19 17:06:21|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/Speech_Recognition_Task/1|
|run_uri|runs:/5bc578aaf3b94f1f86646e9c8d85a11f/whisper_transcriber|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/6285c530ffc347a8b4b32615a932fd73/models/whisper_transcriber|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/5bc578aaf3b94f1f86646e9c8d85a11f/artifacts/whisper_transcriber|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|whisper_transcriber|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|b2dbba1d6e424b9397dad2f2bfb8d038|
|run_id|5bc578aaf3b94f1f86646e9c8d85a11f|
|utc_time_created|2023-07-31 20:25:36.531639|
|model_flavor|transformers|
|model_size_bytes|154431670|

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
|components|['feature_extractor', 'tokenizer']|
|feature_extractor_type|WhisperFeatureExtractor|
|framework|pt|
|instance_type|AutomaticSpeechRecognitionPipeline|
|model_binary|model|
|pipeline_model_type|WhisperForConditionalGeneration|
|source_model_name|openai/whisper-tiny|
|task|automatic-speech-recognition|
|tokenizer_type|WhisperTokenizer|
|transformers_version|4.28.1|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|None|binary|

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
|name|Speech_Recognition_Task|
|creation_timestamp|1690835170575|
|last_updated_timestamp|1690835170746|
|user_id|andre@mycompany.com|
|id|393e8184e3874bfca9c8be335b99e775|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-07-31 20:26:11|
|_last_updated_timestamp|2023-07-31 20:26:11|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Speech_Recognition_Task|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=Speech_Recognition_Task|

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
    "object_id": "/registered-models/393e8184e3874bfca9c8be335b99e775",
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
|name|Speech_Recognition_Task|
|version|1|
|creation_timestamp|1690835170746|
|last_updated_timestamp|1690835177631|
|user_id|andre@mycompany.com|
|current_stage|None|
|source|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/5bc578aaf3b94f1f86646e9c8d85a11f/artifacts/whisper_transcriber|
|run_id|5bc578aaf3b94f1f86646e9c8d85a11f|
|status|READY|
|_creation_timestamp|2023-07-31 20:26:11|
|_last_updated_timestamp|2023-07-31 20:26:18|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/6285c530ffc347a8b4b32615a932fd73/models/whisper_transcriber|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/5bc578aaf3b94f1f86646e9c8d85a11f/artifacts/whisper_transcriber|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Speech_Recognition_Task/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=Speech_Recognition_Task&version=1|

## Tags
  

|Name|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['feature_extractor', 'tokenizer']|
|hf_feature_extractor_type|WhisperFeatureExtractor|
|hf_framework|pt|
|hf_instance_type|AutomaticSpeechRecognitionPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|WhisperForConditionalGeneration|
|hf_source_model_name|openai/whisper-tiny|
|hf_task|automatic-speech-recognition|
|hf_tokenizer_type|WhisperTokenizer|
|hf_transformers_version|4.28.1|

# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|5bc578aaf3b94f1f86646e9c8d85a11f|
|run_uuid|5bc578aaf3b94f1f86646e9c8d85a11f|
|experiment_id|7f1bb46d81ec48a7b627ad762ece5091|
|run_name|omniscient-fish-410|
|status|FINISHED|
|start_time|1690835135484|
|end_time|1690835169629|
|artifact_uri|dbfs:/databricks/mlflow-tracking/7f1bb46d81ec48a7b627ad762ece5091/5bc578aaf3b94f1f86646e9c8d85a11f/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-31 20:25:35|
|_end_time|2023-07-31 20:26:10|
|_duration|34.145|
|_experiment_name|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Run_Task_Notebooks|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/7f1bb46d81ec48a7b627ad762ece5091/runs/5bc578aaf3b94f1f86646e9c8d85a11f|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=5bc578aaf3b94f1f86646e9c8d85a11f|

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
|mlflow.databricks.gitRepoRelativePath|databricks/notebooks/llm_transformers/Speech_Recognition_Task|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/amesar/mlflow-examples|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|5950047518571775697_6483093319262820068_job-952373867448831-run-1-action-2249574689999573|
|mlflow.databricks.notebookID|3428923814211678|
|mlflow.databricks.notebookPath|/Repos/andre@mycompany.com/public-mlflow-examples/databricks/notebooks/llm_transformers/Speech_Recognition_Task|

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
|mlflow.source.name|jobs/952373867448831/run/1|
|mlflow.source.type|JOB|

### Job Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.jobID|952373867448831|
|mlflow.databricks.jobRunID|1|
|mlflow.databricks.jobType|notebook|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'whisper_transcriber', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'binary'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'feature_extractor_type': 'WhisperFeatureExtractor', 'task': 'automatic-speech-recognition', 'framework': 'pt', 'source_model_name': 'openai/whisper-tiny', 'components': ['feature_extractor', 'tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'WhisperTokenizer', 'pipeline_model_type': 'WhisperForConditionalGeneration', 'instance_type': 'AutomaticSpeechRecognitionPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '5bc578aaf3b94f1f86646e9c8d85a11f', 'model_uuid': 'b2dbba1d6e424b9397dad2f2bfb8d038', 'utc_time_created': '2023-07-31 20:25:36.531639', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|omniscient-fish-410|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['feature_extractor', 'tokenizer']|
|hf_feature_extractor_type|WhisperFeatureExtractor|
|hf_framework|pt|
|hf_instance_type|AutomaticSpeechRecognitionPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|WhisperForConditionalGeneration|
|hf_source_model_name|openai/whisper-tiny|
|hf_task|automatic-speech-recognition|
|hf_tokenizer_type|WhisperTokenizer|
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