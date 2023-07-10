
MLflow Model: _runs:/7ee5e476cc964a99beec2f4269f8e811/model_
============================================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
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
|model_uri|runs:/7ee5e476cc964a99beec2f4269f8e811/model|
|flavor|mlflow.sklearn|
|flavor_version|1.2.2|
|mlflow_version|2.4.1|
|size_bytes|105,679|
|databricks_runtime|13.2.x-cpu-ml-scala2.12|
|is_unity_catalog||
|time_created|2023-07-08 04:53:25|
|report_time|2023-07-10 16:52:25|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|runs:/7ee5e476cc964a99beec2f4269f8e811/model|
|run_uri|runs:/7ee5e476cc964a99beec2f4269f8e811/model|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/2668333326915882/7ee5e476cc964a99beec2f4269f8e811/artifacts/model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|model|
|databricks_runtime|13.2.x-cpu-ml-scala2.12|
|mlflow_version|2.4.1|
|model_uuid|3d22615565ae4f5f896d3a05072b552f|
|run_id|7ee5e476cc964a99beec2f4269f8e811|
|utc_time_created|2023-07-08 04:53:25.446742|

### Flavors

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|mlflow.sklearn|
|model_path|model.pkl|
|predict_fn|predict|
|python_version|3.10.6|

#### Flavor 'sklearn'
  

|Name|Value|
| :--- | :--- |
|code|None|
|pickled_model|model.pkl|
|serialization_format|cloudpickle|
|sklearn_version|1.2.2|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|fixed_acidity|double|
|volatile_acidity|double|
|citric_acid|double|
|residual_sugar|double|
|chlorides|double|
|free_sulfur_dioxide|double|
|total_sulfur_dioxide|double|
|density|double|
|pH|double|
|sulphates|double|
|alcohol|double|

### Outputs
  

|Type name|Type value|
| :--- | :--- |
|tensor|{'dtype': 'float64', 'shape': [-1]}|

## Saved input example info
  

|Name|Value|
| :--- | :--- |
|artifact_path|input_example.json|
|pandas_orient|split|
|type|dataframe|

# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|7ee5e476cc964a99beec2f4269f8e811|
|run_uuid|7ee5e476cc964a99beec2f4269f8e811|
|experiment_id|2668333326915882|
|run_name|Best_Reference_Run_UC|
|status|FINISHED|
|start_time|1688792000629|
|end_time|1688792019958|
|artifact_uri|dbfs:/databricks/mlflow-tracking/2668333326915882/7ee5e476cc964a99beec2f4269f8e811/artifacts|
|lifecycle_stage|active|
|_start_time|2023-07-08 04:53:21|
|_end_time|2023-07-08 04:53:40|
|_duration|19.329|
|_experiment_name|/Users/andre.mesarovic@databricks.com/experiments/best/Sklearn_Wine_repo_uc|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/2668333326915882/runs/7ee5e476cc964a99beec2f4269f8e811|
|_api_link|https://oregon.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=7ee5e476cc964a99beec2f4269f8e811|

## Params
  

|Param|Value|
| :--- | :--- |
|max_depth|1|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|r2|0.1553172302194683|
|rmse|0.7986004372118107|

## Inputs

## Tags

### Git Repo Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.gitRepoCommit|8bc7a70e5c75acf20c368ee7b463b14a525236b4|
|mlflow.databricks.gitRepoProvider|gitHub|
|mlflow.databricks.gitRepoReference|master|
|mlflow.databricks.gitRepoReferenceType|branch|
|mlflow.databricks.gitRepoRelativePath|databricks/notebooks/basic/Sklearn_Wine|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/amesar/mlflow-examples|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|6785241734622852263_7667615984189449245_2df0651ed9d14281be1e96075526d35d|
|mlflow.databricks.notebookID|3336498746241054|
|mlflow.databricks.notebookPath|/Repos/andre.mesarovic@databricks.com/public-mlflow-examples/databricks/notebooks/basic/Sklearn_Wine|
|mlflow.databricks.notebookRevisionID|1688792020378|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0414-154233-qm0df4rx|
|mlflow.databricks.cluster.info|{'cluster_name': 'andre_ML_13.1', 'spark_version': '13.2.x-cpu-ml-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'num_workers': 1}|
|mlflow.databricks.cluster.libraries|{'installable': [{'jar': 'dbfs:/home/andre.mesarovic@databricks.com/lib/jars/PrintArgs.jar'}, {'whl': 'dbfs:/home/andre.mesarovic@databricks.com/work/jobs/sklearn_wine/mlflow_sklearn_wine-0.0.1-py3-none-any.whl'}], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|
|mlflow.databricks.workspaceID|2556758628403379|
|mlflow.databricks.workspaceURL|e2-demo-west.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Repos/andre.mesarovic@databricks.com/public-mlflow-examples/databricks/notebooks/basic/Sklearn_Wine|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'model', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'double', 'name': 'fixed_acidity'}, {'type': 'double', 'name': 'volatile_acidity'}, {'type': 'double', 'name': 'citric_acid'}, {'type': 'double', 'name': 'residual_sugar'}, {'type': 'double', 'name': 'chlorides'}, {'type': 'double', 'name': 'free_sulfur_dioxide'}, {'type': 'double', 'name': 'total_sulfur_dioxide'}, {'type': 'double', 'name': 'density'}, {'type': 'double', 'name': 'pH'}, {'type': 'double', 'name': 'sulphates'}, {'type': 'double', 'name': 'alcohol'}], 'outputs': [{'type': 'tensor', 'tensor-spec': {'dtype': 'float64', 'shape': [-1]}}]}, 'flavors': {'python_function': {'predict_fn': 'predict', 'model_path': 'model.pkl', 'loader_module': 'mlflow.sklearn', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}, 'python_version': '3.10.6'}, 'sklearn': {'pickled_model': 'model.pkl', 'sklearn_version': '1.2.2', 'serialization_format': 'cloudpickle', 'code': None}}, 'run_id': '7ee5e476cc964a99beec2f4269f8e811', 'model_uuid': '3d22615565ae4f5f896d3a05072b552f', 'utc_time_created': '2023-07-08 04:53:25.446742', 'mlflow_version': '2.4.1', 'databricks_runtime': '13.2.x-cpu-ml-scala2.12'}]|
|mlflow.runName|Best_Reference_Run_UC|
|mlflow.user|andre.mesarovic@databricks.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|algorithm|<class 'sklearn.tree._classes.DecisionTreeRegressor'>|
|data_source|andre_catalog.ml_data.winequality_white|
|input_example|True|
|log_input|True|
|run_name|Best_Reference_Run_UC|
|save_signature|True|
|sparkDatasourceInfo|[{'path': 's3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/tables/fb9f1fbf-156a-4a91-8ea3-4a8e58d7b1bf', 'version': '0', 'format': 'delta'}]|
|timestamp|2023-07-08 04:53:16|
|version.DATABRICKS_RUNTIME_VERSION|13.2|
|version.mlflow|2.4.1|
|version.python|3.10.6|
|version.sklearn|1.2.2|

### Exploded Tags

#### Spark Datasources
  

|Format|Version|Path|
| :--- | :--- | :--- |
|delta|0|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/tables/fb9f1fbf-156a-4a91-8ea3-4a8e58d7b1bf|

#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0414-154233-qm0df4rx|
|cluster_name|andre_ML_13.1|
|spark_version|13.2.x-cpu-ml-scala2.12|
|node_type_id|i3.xlarge|
|driver_node_type_id|i3.xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_count': 0}|
|num_workers|1|

#### Cluster Libraries

##### Installable Libraries
  

|Name|Value|
| :--- | :--- |
|jar|dbfs:/home/andre.mesarovic@databricks.com/lib/jars/PrintArgs.jar|
|whl|dbfs:/home/andre.mesarovic@databricks.com/work/jobs/sklearn_wine/mlflow_sklearn_wine-0.0.1-py3-none-any.whl|

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|2668333326915882|
|name|/Users/andre.mesarovic@databricks.com/experiments/best/Sklearn_Wine_repo_uc|
|artifact_location|dbfs:/databricks/mlflow-tracking/2668333326915882|
|lifecycle_stage|active|
|last_update_time|1688792000629|
|creation_time|1688789864922|
|_creation_time|2023-07-08 04:17:45|
|_last_update_time|2023-07-08 04:53:21|
|_tracking_uri|databricks|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/2668333326915882|
|_api_link|https://oregon.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=2668333326915882|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre.mesarovic@databricks.com/experiments/best/Sklearn_Wine_repo_uc|
|mlflow.ownerEmail|andre.mesarovic@databricks.com|
|mlflow.experimentType|MLFLOW_EXPERIMENT|

### User Tags
  

|Key|Value|
| :--- | :--- |
|timestamp|2023-07-08 04:53:16|
|version_mlflow|2.4.1|

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
    "object_id": "/experiments/2668333326915882",
    "object_type": "mlflowExperiment",
    "access_control_list": [
      {
        "user_name": "andre.mesarovic@databricks.com",
        "display_name": "Andre Mesarovic",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/directories/767933989557963"
            ]
          }
        ]
      },
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "feifei-service-principal-e2-demo-west-ws-do-not-delete",
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
      }
    ]
  }
}

```