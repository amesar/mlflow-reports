
MLflow Model: _models:/t5_small_summarizer/1_
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
|model_uri|models:/t5_small_summarizer/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|245,300,813|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|False|
|time_created|2023-07-29 11:23:49|
|report_time|2023-07-29 12:19:01|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/t5_small_summarizer/1|
|run_uri|runs:/2e37e1d004504a748283af4fb735723b/summarizer|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/0761a8ad85bc4fa4bc5d0df6a50cef78/models/summarizer|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/2e37e1d004504a748283af4fb735723b/artifacts/summarizer|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|summarizer|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|76d16d0dc03b421ab31e261d40a39661|
|run_id|2e37e1d004504a748283af4fb735723b|
|utc_time_created|2023-07-29 11:23:49.640803|
|model_flavor|transformers|
|model_size_bytes|245300813|

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
|pipeline_model_type|T5ForConditionalGeneration|
|source_model_name|t5-small|
|task|summarization|
|tokenizer_type|T5TokenizerFast|
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
|name|t5_small_summarizer|
|creation_timestamp|1690631742133|
|last_updated_timestamp|1690633115550|
|user_id|andre@mycompany.com|
|id|d0404c166aa54097b6b6e86678781dca|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-07-29 11:55:42|
|_last_updated_timestamp|2023-07-29 12:18:36|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/t5_small_summarizer|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=t5_small_summarizer|

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
    "object_id": "/registered-models/d0404c166aa54097b6b6e86678781dca",
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
|name|t5_small_summarizer|
|version|1|
|creation_timestamp|1690631742365|
|last_updated_timestamp|1690633115550|
|user_id|andre@mycompany.com|
|current_stage|None|
|source|dbfs:/databricks/mlflow-tracking/3428923814202924/2e37e1d004504a748283af4fb735723b/artifacts/summarizer|
|run_id|2e37e1d004504a748283af4fb735723b|
|status|READY|
|_creation_timestamp|2023-07-29 11:55:42|
|_last_updated_timestamp|2023-07-29 12:18:36|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/0761a8ad85bc4fa4bc5d0df6a50cef78/models/summarizer|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/2e37e1d004504a748283af4fb735723b/artifacts/summarizer|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/t5_small_summarizer/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=t5_small_summarizer&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|2e37e1d004504a748283af4fb735723b|
|run_uuid|2e37e1d004504a748283af4fb735723b|
|experiment_id|3428923814202924|
|run_name|amazing-pug-568|
|status|FINISHED|
|start_time|1690629826431|
|end_time|1690629841637|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/2e37e1d004504a748283af4fb735723b/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-29 11:23:46|
|_end_time|2023-07-29 11:24:02|
|_duration|15.206|
|_experiment_name|/Users/andre@mycompany.com/LLM 06 - MLflow experiment|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3428923814202924/runs/2e37e1d004504a748283af4fb735723b|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=2e37e1d004504a748283af4fb735723b|

## Params
  

|Param|Value|
| :--- | :--- |
|do_sample|True|
|hf_model_name|t5-small|
|max_length|40|
|min_length|20|
|truncation|True|

## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|4630745098729794893_7466316912331952313_be31d33f260942aa83004a34f34cbceb|
|mlflow.databricks.notebookID|3428923814202230|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/LLM/training/large-language-models/LLM 06 - LLMOps/LLM 06 - LLMOps|
|mlflow.databricks.notebookRevisionID|1690629841771|

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
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/LLM/training/large-language-models/LLM 06 - LLMOps/LLM 06 - LLMOps|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'summarizer', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'summarization', 'framework': 'pt', 'source_model_name': 't5-small', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'T5TokenizerFast', 'pipeline_model_type': 'T5ForConditionalGeneration', 'instance_type': 'SummarizationPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '2e37e1d004504a748283af4fb735723b', 'model_uuid': '76d16d0dc03b421ab31e261d40a39661', 'utc_time_created': '2023-07-29 11:23:49.640803', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|amazing-pug-568|
|mlflow.user|andre@mycompany.com|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
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
|experiment_id|3428923814202924|
|name|/Users/andre@mycompany.com/LLM 06 - MLflow experiment|
|artifact_location|dbfs:/databricks/mlflow-tracking/3428923814202924|
|lifecycle_stage|active|
|last_update_time|1690632055402|
|creation_time|1690629825998|
|_creation_time|2023-07-29 11:23:46|
|_last_update_time|2023-07-29 12:00:55|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3428923814202924|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3428923814202924|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/LLM 06 - MLflow experiment|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experimentType|MLFLOW_EXPERIMENT|

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
    "object_id": "/experiments/3428923814202924",
    "object_type": "mlflowExperiment",
    "access_control_list": [
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "service-principal-e2-demo-west-ws-do-not-delete",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/directories/"
            ]
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
              "/directories/"
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
            "inherited": true,
            "inherited_from_object": [
              "/directories/767933989557963"
            ]
          }
        ]
      }
    ]
  }
}

```