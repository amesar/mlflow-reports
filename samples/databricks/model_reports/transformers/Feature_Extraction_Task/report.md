
MLflow Model: _models:/Feature_Extraction_Task/1_
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
|model_uri|models:/Feature_Extraction_Task/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|134,465,452|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|False|
|time_created|2023-07-31 04:55:26|
|report_time|2023-08-19 17:03:47|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/Feature_Extraction_Task/1|
|run_uri|runs:/5de307d98c754906afb624e844466888/sentence_transformer|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/7cfba6f56b3146e6ba53cff27c987eef/models/sentence_transformer|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/e6efd004206b4ce995a9ddcf11e27bc6/5de307d98c754906afb624e844466888/artifacts/sentence_transformer|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|sentence_transformer|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|e4c6edac10ff4bd1aa9dae3ba70cd89c|
|run_id|5de307d98c754906afb624e844466888|
|utc_time_created|2023-07-31 04:55:26.552063|
|model_flavor|transformers|
|model_size_bytes|134465452|

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
|instance_type|FeatureExtractionPipeline|
|model_binary|model|
|pipeline_model_type|BertModel|
|source_model_name|sentence-transformers/all-MiniLM-L12-v2|
|task|feature-extraction|
|tokenizer_type|BertTokenizerFast|
|transformers_version|4.28.1|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|None|string|

### Outputs
  

|Type name|Type value|
| :--- | :--- |
|tensor|{'dtype': 'float64', 'shape': [-1]}|

## Saved input example info
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|Feature_Extraction_Task|
|creation_timestamp|1690779338810|
|last_updated_timestamp|1690835093079|
|user_id|andre@mycompany.com|
|id|0f388c33f4114f94973640fb3baca0d8|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-07-31 04:55:39|
|_last_updated_timestamp|2023-07-31 20:24:53|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Feature_Extraction_Task|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=Feature_Extraction_Task|

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
    "object_id": "/registered-models/0f388c33f4114f94973640fb3baca0d8",
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
|name|Feature_Extraction_Task|
|version|1|
|creation_timestamp|1690779338999|
|last_updated_timestamp|1690779344980|
|user_id|andre@mycompany.com|
|current_stage|None|
|source|dbfs:/databricks/mlflow-tracking/e6efd004206b4ce995a9ddcf11e27bc6/5de307d98c754906afb624e844466888/artifacts/sentence_transformer|
|run_id|5de307d98c754906afb624e844466888|
|status|READY|
|_creation_timestamp|2023-07-31 04:55:39|
|_last_updated_timestamp|2023-07-31 04:55:45|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/7cfba6f56b3146e6ba53cff27c987eef/models/sentence_transformer|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/e6efd004206b4ce995a9ddcf11e27bc6/5de307d98c754906afb624e844466888/artifacts/sentence_transformer|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Feature_Extraction_Task/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=Feature_Extraction_Task&version=1|

## Tags
  

|Name|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['tokenizer']|
|hf_framework|pt|
|hf_instance_type|FeatureExtractionPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|BertModel|
|hf_source_model_name|sentence-transformers/all-MiniLM-L12-v2|
|hf_task|feature-extraction|
|hf_tokenizer_type|BertTokenizerFast|
|hf_transformers_version|4.28.1|

# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|5de307d98c754906afb624e844466888|
|run_uuid|5de307d98c754906afb624e844466888|
|experiment_id|e6efd004206b4ce995a9ddcf11e27bc6|
|run_name|auspicious-bug-281|
|status|FINISHED|
|start_time|1690779325951|
|end_time|1690779337858|
|artifact_uri|dbfs:/databricks/mlflow-tracking/e6efd004206b4ce995a9ddcf11e27bc6/5de307d98c754906afb624e844466888/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-31 04:55:26|
|_end_time|2023-07-31 04:55:38|
|_duration|11.907|
|_experiment_name|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/transformers/Feature_Extraction_Task|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/e6efd004206b4ce995a9ddcf11e27bc6/runs/5de307d98c754906afb624e844466888|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=5de307d98c754906afb624e844466888|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Git Repo Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.gitRepoCommit|b359ae5b4cc89f303fb5ec6441ab5aa738863a0e|
|mlflow.databricks.gitRepoProvider|gitHub|
|mlflow.databricks.gitRepoReference|master|
|mlflow.databricks.gitRepoReferenceType|branch|
|mlflow.databricks.gitRepoRelativePath|databricks/notebooks/llm_transformers/Feature_Extraction_Task|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/amesar/mlflow-examples|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|7559472645153523559_6982783053250151105_051272f341214836b31ae73f1b98e8fb|
|mlflow.databricks.notebookID|3428923814203611|
|mlflow.databricks.notebookPath|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Feature_Extraction_Task|

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
|mlflow.source.name|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/llm_transformers/Feature_Extraction_Task|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'sentence_transformer', 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'name': 'double', 'type': 'tensor', 'tensor-spec': {'dtype': 'float64', 'shape': [-1]}}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'feature-extraction', 'framework': 'pt', 'source_model_name': 'sentence-transformers/all-MiniLM-L12-v2', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'BertTokenizerFast', 'pipeline_model_type': 'BertModel', 'instance_type': 'FeatureExtractionPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '5de307d98c754906afb624e844466888', 'model_uuid': 'e4c6edac10ff4bd1aa9dae3ba70cd89c', 'utc_time_created': '2023-07-31 04:55:26.552063', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|auspicious-bug-281|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|hf_code|None|
|hf_components|['tokenizer']|
|hf_framework|pt|
|hf_instance_type|FeatureExtractionPipeline|
|hf_model_binary|model|
|hf_pipeline_model_type|BertModel|
|hf_source_model_name|sentence-transformers/all-MiniLM-L12-v2|
|hf_task|feature-extraction|
|hf_tokenizer_type|BertTokenizerFast|
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
|experiment_id|e6efd004206b4ce995a9ddcf11e27bc6|
|name|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/transformers/Feature_Extraction_Task|
|artifact_location|dbfs:/databricks/mlflow-tracking/e6efd004206b4ce995a9ddcf11e27bc6|
|lifecycle_stage|active|
|last_update_time|1690779325951|
|creation_time|1690697118386|
|_creation_time|2023-07-30 06:05:18|
|_last_update_time|2023-07-31 04:55:26|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/e6efd004206b4ce995a9ddcf11e27bc6|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=e6efd004206b4ce995a9ddcf11e27bc6|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.experiment.sourceType|REPO_NOTEBOOK|
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Repos/andre@mycompany.com/mlflow-examples/databricks/notebooks/transformers/Feature_Extraction_Task|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experiment.sourceId|3428923814203611|

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
    "error": "{\"http_status_code\": 400, \"uri\": \"https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/e6efd004206b4ce995a9ddcf11e27bc6\", \"params\": null, \"response\": \"{\\\"error_code\\\":\\\"INVALID_PARAMETER_VALUE\\\",\\\"message\\\":\\\"For input string: \\\\\\\"e6efd004206b4ce995a9ddcf11e27bc6\\\\\\\"\\\"}\"}"
  }
}

```