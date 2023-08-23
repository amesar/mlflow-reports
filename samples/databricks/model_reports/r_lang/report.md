
MLflow Model: _models:/mlflow-quick-start-r/1_
==============================================

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
|model_uri|models:/mlflow-quick-start-r/1|
|flavor|None|
|flavor_version||
|mlflow_version|None|
|size_bytes|295|
|databricks_runtime||
|is_unity_catalog|False|
|time_created|2023-08-19 04:03:42|
|report_time|2023-08-19 16:56:21|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/mlflow-quick-start-r/1|
|run_uri|runs:/6acb70ea93744405ae89444352dbf199/model|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/52187f92b24e4f7e8732f2e486be9e43/models/model|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3350558521995749/6acb70ea93744405ae89444352dbf199/artifacts/model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|utc_time_created|2023-08-19 04:03:42.857877|
|run_id|6acb70ea93744405ae89444352dbf199|
|artifact_path|model|
|model_flavor|crate|
|model_size_bytes|295|

### Flavors

#### Flavor 'crate'
  

|Name|Value|
| :--- | :--- |
|version|0.1.0|
|model|crate.bin|

## Signature
  
**_<font color="red" size="+1">None found</font>_**
## Saved input example info
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|mlflow-quick-start-r|
|creation_timestamp|1692417973320|
|last_updated_timestamp|1692417973632|
|user_id|andre@mycompany.com|
|id|bbb67b13043f4c51822d845332f9bb32|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-08-19 04:06:13|
|_last_updated_timestamp|2023-08-19 04:06:14|
|_is_unity_catalog|False|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/mlflow-quick-start-r|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=mlflow-quick-start-r|

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
    "object_id": "/registered-models/bbb67b13043f4c51822d845332f9bb32",
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
|name|mlflow-quick-start-r|
|version|1|
|creation_timestamp|1692417973632|
|last_updated_timestamp|1692417974646|
|user_id|andre@mycompany.com|
|current_stage|None|
|source|dbfs:/databricks/mlflow-tracking/3350558521995749/6acb70ea93744405ae89444352dbf199/artifacts/model|
|run_id|6acb70ea93744405ae89444352dbf199|
|status|READY|
|_creation_timestamp|2023-08-19 04:06:14|
|_last_updated_timestamp|2023-08-19 04:06:15|
|_is_unity_catalog|False|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/52187f92b24e4f7e8732f2e486be9e43/models/model|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3350558521995749/6acb70ea93744405ae89444352dbf199/artifacts/model|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/mlflow-quick-start-r/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=mlflow-quick-start-r&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|6acb70ea93744405ae89444352dbf199|
|run_uuid|6acb70ea93744405ae89444352dbf199|
|experiment_id|3350558521995749|
|run_name|learned-mare-692|
|status|FINISHED|
|start_time|1692417821720|
|end_time|1692417830324|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3350558521995749/6acb70ea93744405ae89444352dbf199/artifacts|
|lifecycle_stage|active|
|_start_time|2023-08-19 04:03:42|
|_end_time|2023-08-19 04:03:50|
|_duration|8.604|
|_experiment_name|/Users/andre@mycompany.com/mlflow/r_lang/mlflow-quick-start-r|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3350558521995749/runs/6acb70ea93744405ae89444352dbf199|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=6acb70ea93744405ae89444352dbf199|

## Params
  

|Param|Value|
| :--- | :--- |
|mtry|3|
|ntree|100|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|sensitivity|0.860986547085202|
|specificity|0.568807339449541|

## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebookID|3350558521995749|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/r_lang/mlflow-quick-start-r|
|mlflow.databricks.notebookRevisionID|1692417830571|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/r_lang/mlflow-quick-start-r|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'utc_time_created': '2023-08-19 04:03:42.857877', 'run_id': '6acb70ea93744405ae89444352dbf199', 'artifact_path': 'model', 'flavors': {'crate': {'version': '0.1.0', 'model': 'crate.bin'}}}]|
|mlflow.runName|learned-mare-692|
|mlflow.user|andre@mycompany.com|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|3350558521995749|
|name|/Users/andre@mycompany.com/mlflow/r_lang/mlflow-quick-start-r|
|artifact_location|dbfs:/databricks/mlflow-tracking/3350558521995749|
|lifecycle_stage|active|
|last_update_time|1692417821998|
|creation_time|1692417821998|
|_creation_time|2023-08-19 04:03:42|
|_last_update_time|2023-08-19 04:03:42|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3350558521995749|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3350558521995749|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/mlflow/r_lang/mlflow-quick-start-r|
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
    "error": "{\"http_status_code\": 400, \"uri\": \"https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/3350558521995749\", \"params\": null, \"response\": \"{\\\"error_code\\\":\\\"INVALID_PARAMETER_VALUE\\\",\\\"message\\\":\\\"Object 3350558521995749 not a experiment.\\\"}\"}"
  }
}

```