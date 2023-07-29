
MLflow Model: _models:/andre.llm_models.t5_small_summarizer/1_
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
|model_uri|models:/andre.llm_models.t5_small_summarizer/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.5.0|
|size_bytes|245,300,813|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|is_unity_catalog|True|
|time_created|2023-07-29 12:00:58|
|report_time|2023-07-29 12:46:01|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/andre.llm_models.t5_small_summarizer/1|
|run_uri|runs:/6ce2a1c4e1b745db95305345a393a98f/summarizer|
|reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/f1cd858a-df0e-46cd-bdd9-91708f1141b4/versions/825349d2-2ee1-41ce-9d21-da5256a0798c|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/6ce2a1c4e1b745db95305345a393a98f/artifacts/summarizer|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|summarizer|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.5.0|
|model_uuid|2b7a645dc76048d7b02cf6749a3f3417|
|run_id|6ce2a1c4e1b745db95305345a393a98f|
|utc_time_created|2023-07-29 12:00:58.466606|
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
|name|andre.llm_models.t5_small_summarizer|
|creation_timestamp|1690634711672|
|last_updated_timestamp|1690634711672|
|user_id|andre@mycompany.com|
|_creation_timestamp|2023-07-29 12:45:12|
|_last_updated_timestamp|2023-07-29 12:45:12|
|_is_unity_catalog|True|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.llm_models.t5_small_summarizer|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/registered-models/get?name=andre.llm_models.t5_small_summarizer|

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
|name|andre.llm_models.t5_small_summarizer|
|version|1|
|creation_timestamp|1690634721446|
|last_updated_timestamp|1690634726547|
|user_id|andre@mycompany.com|
|source|dbfs:/databricks/mlflow-tracking/3428923814202924/6ce2a1c4e1b745db95305345a393a98f/artifacts/summarizer|
|run_id|6ce2a1c4e1b745db95305345a393a98f|
|run_tracking_server_id|2556758628403379|
|status|READY|
|storage_location|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/f1cd858a-df0e-46cd-bdd9-91708f1141b4/versions/825349d2-2ee1-41ce-9d21-da5256a0798c|
|_creation_timestamp|2023-07-29 12:45:21|
|_last_updated_timestamp|2023-07-29 12:45:27|
|_is_unity_catalog|True|
|_reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/f1cd858a-df0e-46cd-bdd9-91708f1141b4/versions/825349d2-2ee1-41ce-9d21-da5256a0798c|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/6ce2a1c4e1b745db95305345a393a98f/artifacts/summarizer|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.llm_models.t5_small_summarizer/version/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/model-versions/get?name=andre.llm_models.t5_small_summarizer&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|6ce2a1c4e1b745db95305345a393a98f|
|run_uuid|6ce2a1c4e1b745db95305345a393a98f|
|experiment_id|3428923814202924|
|run_name|clean-goat-783|
|status|FINISHED|
|start_time|1690632055402|
|end_time|1690632071387|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3428923814202924/6ce2a1c4e1b745db95305345a393a98f/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-29 12:00:55|
|_end_time|2023-07-29 12:01:11|
|_duration|15.985|
|_experiment_name|/Users/andre@mycompany.com/LLM 06 - MLflow experiment|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3428923814202924/runs/6ce2a1c4e1b745db95305345a393a98f|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=6ce2a1c4e1b745db95305345a393a98f|

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
|mlflow.databricks.notebook.commandID|4421608333402563903_5600671050348862294_af54e14fdc794737ad25f674bab52982|
|mlflow.databricks.notebookID|3428923814202944|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/LLM/training/large-language-models/LLM 06 - LLMOps/LLM 06 - LLMOps - UC|
|mlflow.databricks.notebookRevisionID|1690632071650|

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
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/LLM/training/large-language-models/LLM 06 - LLMOps/LLM 06 - LLMOps - UC|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'summarizer', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'model_binary': 'model', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'summarization', 'framework': 'pt', 'source_model_name': 't5-small', 'components': ['tokenizer'], 'code': None, 'model_binary': 'model', 'tokenizer_type': 'T5TokenizerFast', 'pipeline_model_type': 'T5ForConditionalGeneration', 'instance_type': 'SummarizationPipeline', 'transformers_version': '4.28.1'}}, 'run_id': '6ce2a1c4e1b745db95305345a393a98f', 'model_uuid': '2b7a645dc76048d7b02cf6749a3f3417', 'utc_time_created': '2023-07-29 12:00:58.466606', 'mlflow_version': '2.5.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|clean-goat-783|
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