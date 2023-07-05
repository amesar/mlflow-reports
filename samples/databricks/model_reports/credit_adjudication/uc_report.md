
MLflow Model: _models:/andre.ml_models.credit_adjudication/1_
=====================================================================

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
|model_uri|models:/andre.ml_models.credit_adjudication/1|
|flavor|mlflow.sklearn|
|flavor_version|1.0.2|
|mlflow_version|2.1.1|
|size_bytes|206,418|
|databricks_runtime|12.2.x-cpu-ml-scala2.12|
|time_created|2023-06-15 23:34:12|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/andre.ml_models.credit_adjudication/1|
|run_uri|runs:/76031d22c5464dd99431e426b939e800/model|
|reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/667c0c81-05ec-4bab-8357-454b1097b217/versions/9c148c5c-0006-40de-92a8-4dcf32105080|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|model|
|databricks_runtime|12.2.x-cpu-ml-scala2.12|
|mlflow_version|2.1.1|
|model_uuid|e38b5fefce844b31be8e371430557cfc|
|run_id|76031d22c5464dd99431e426b939e800|
|utc_time_created|2023-06-15 23:34:12.981982|

### Flavors

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|mlflow.sklearn|
|model_path|model.pkl|
|predict_fn|predict|
|python_version|3.9.5|

#### Flavor 'sklearn'
  

|Name|Value|
| :--- | :--- |
|code|None|
|pickled_model|model.pkl|
|serialization_format|cloudpickle|
|sklearn_version|1.0.2|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|AGE|long|
|CREDIT_AMOUNT|long|
|DURATION|long|
|PURPOSE_domestic appliances|integer|
|PURPOSE_furniture/equipment|integer|
|PURPOSE_vacation/others|integer|
|SEX_male|integer|
|HOUSING_own|integer|
|SAVING_moderate|integer|
|SAVING_no_inf|integer|
|SAVING_quite rich|integer|
|SAVING_rich|integer|
|CHECK_moderate|integer|
|CHECK_no_inf|integer|
|AGE_CAT_Young|integer|

### Outputs
  

|Type name|Type value|
| :--- | :--- |
|double|None|

## Saved input example info
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|andre.ml_models.credit_adjudication|
|creation_timestamp|1688559167943|
|last_updated_timestamp|1688559167943|
|user_id|andre@databricks.com|
|_creation_timestamp|2023-07-05 12:12:48|
|_last_updated_timestamp|2023-07-05 12:12:48|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.ml_models.credit_adjudication|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog/registered-models/get?name=andre.ml_models.credit_adjudication|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
**_<font color="red" size="+1">None found</font>_**
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|andre.ml_models.credit_adjudication|
|version|1|
|creation_timestamp|1688559173393|
|last_updated_timestamp|1688559174750|
|user_id|andre@databricks.com|
|source|dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model|
|run_id|76031d22c5464dd99431e426b939e800|
|run_tracking_server_id|2556758628403379|
|status|READY|
|storage_location|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/667c0c81-05ec-4bab-8357-454b1097b217/versions/9c148c5c-0006-40de-92a8-4dcf32105080|
|_creation_timestamp|2023-07-05 12:12:53|
|_last_updated_timestamp|2023-07-05 12:12:55|
|_reg_model_download_uri|s3://databricks-e2demofieldengwest/b169b504-4c54-49f2-bc3a-adf4b128f36d/models/667c0c81-05ec-4bab-8357-454b1097b217/versions/9c148c5c-0006-40de-92a8-4dcf32105080|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts/model|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com/explore/data/models/andre.ml_models.credit_adjudication/version/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalogmodel-versions/get?name=andre.ml_models.credit_adjudication&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|76031d22c5464dd99431e426b939e800|
|run_uuid|76031d22c5464dd99431e426b939e800|
|experiment_id|bf024d57582f4c8cbf816151cc6e1bac|
|run_name|credit adjudication|
|status|FINISHED|
|start_time|1686872052388|
|end_time|1686872056211|
|artifact_uri|dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac/76031d22c5464dd99431e426b939e800/artifacts|
|lifecycle_stage|active|
|_start_time|2023-06-15 23:34:12|
|_end_time|2023-06-15 23:34:16|
|_duration|3.823|
|_experiment_name|/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/bf024d57582f4c8cbf816151cc6e1bac/runs/76031d22c5464dd99431e426b939e800|
|_api_link|{'mlflow_client': 'https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow', 'uc_client': 'https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog'}/runs/get?run_id=76031d22c5464dd99431e426b939e800|

## Params
  

|Param|Value|
| :--- | :--- |
|base_score|None|
|booster|None|
|callbacks|None|
|colsample_bylevel|None|
|colsample_bynode|None|
|colsample_bytree|None|
|early_stopping_rounds|None|
|enable_categorical|False|
|eval_metric|logloss|
|feature_types|None|
|gamma|None|
|gpu_id|None|
|grow_policy|None|
|importance_type|None|
|interaction_constraints|None|
|learning_rate|None|
|max_bin|None|
|max_cat_threshold|None|
|max_cat_to_onehot|None|
|max_delta_step|None|
|max_depth|None|
|max_leaves|None|
|min_child_weight|None|
|missing|nan|
|monotone_constraints|None|
|n_estimators|100|
|n_jobs|None|
|num_parallel_tree|None|
|objective|binary:logistic|
|predictor|None|
|random_state|None|
|reg_alpha|None|
|reg_lambda|None|
|sampling_method|None|
|scale_pos_weight|None|
|subsample|None|
|tree_method|None|
|use_label_encoder|None|
|validate_parameters|None|
|verbosity|0|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|cv_accuracy|0.7066666666666668|
|cv_f1|0.46731387638541333|
|cv_precision|0.5218130677484225|
|cv_recall|0.4360843347685453|
|ks_pvalue|0.0|
|ks_statistic|1.0|

## Inputs

## Tags

### Git Repo Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.gitRepoCommit|435fa512608b0a87fc33aedfbac2427b0c1d947b|
|mlflow.databricks.gitRepoProvider|gitHub|
|mlflow.databricks.gitRepoReference|dais|
|mlflow.databricks.gitRepoReferenceType|branch|
|mlflow.databricks.gitRepoRelativePath|templates/Credit Adjudication - Example|
|mlflow.databricks.gitRepoStatus|unknown|
|mlflow.databricks.gitRepoUrl|https://github.com/databricks-industry-solutions/fsi-mrm-generation.git|

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|1630835003914618246_5442231573309100337_8e188548453f4c8e9188dda502e74938|
|mlflow.databricks.notebookID|3022585156450040|
|mlflow.databricks.notebookPath|/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0614-194712-2nyzmplk|
|mlflow.databricks.cluster.info|{'cluster_name': 'mrmgen', 'spark_version': '12.2.x-cpu-ml-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'autoscale': {'min_workers': 2, 'max_workers': 20, 'target_workers': 4}}|
|mlflow.databricks.cluster.libraries|{'installable': [], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|
|mlflow.databricks.workspaceID|2556758628403379|
|mlflow.databricks.workspaceURL|e2-demo-west.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'model', 'signature': {'inputs': [{'name': 'AGE', 'type': 'long'}, {'name': 'CREDIT_AMOUNT', 'type': 'long'}, {'name': 'DURATION', 'type': 'long'}, {'name': 'PURPOSE_domestic appliances', 'type': 'integer'}, {'name': 'PURPOSE_furniture/equipment', 'type': 'integer'}, {'name': 'PURPOSE_vacation/others', 'type': 'integer'}, {'name': 'SEX_male', 'type': 'integer'}, {'name': 'HOUSING_own', 'type': 'integer'}, {'name': 'SAVING_moderate', 'type': 'integer'}, {'name': 'SAVING_no_inf', 'type': 'integer'}, {'name': 'SAVING_quite rich', 'type': 'integer'}, {'name': 'SAVING_rich', 'type': 'integer'}, {'name': 'CHECK_moderate', 'type': 'integer'}, {'name': 'CHECK_no_inf', 'type': 'integer'}, {'name': 'AGE_CAT_Young', 'type': 'integer'}], 'outputs': [{'name': 'RISK_EN', 'type': 'double'}]}, 'flavors': {'python_function': {'predict_fn': 'predict', 'model_path': 'model.pkl', 'loader_module': 'mlflow.sklearn', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}, 'python_version': '3.9.5'}, 'sklearn': {'pickled_model': 'model.pkl', 'sklearn_version': '1.0.2', 'serialization_format': 'cloudpickle', 'code': None}}, 'run_id': '76031d22c5464dd99431e426b939e800', 'model_uuid': 'e38b5fefce844b31be8e371430557cfc', 'utc_time_created': '2023-06-15 23:34:12.981982', 'mlflow_version': '2.1.1', 'databricks_runtime': '12.2.x-cpu-ml-scala2.12'}]|
|mlflow.note.content|A 10 fold cross-validation procedure was used to select the best model and hyperparameters across multiple techniques.<br/>Our model selection included XGBoost and K nearest neighbors and selected XGBClassifier as best fit.<br/>This run was evaluated as our best run that maximizes `cross_val_score`.<br/>|
|mlflow.runName|credit adjudication|
|mlflow.user|antoine.amend@databricks.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|Model complexity|MEDIUM|
|Model explainability|MEDIUM|
|Model name|XGBClassifier|

### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0614-194712-2nyzmplk|
|cluster_name|mrmgen|
|spark_version|12.2.x-cpu-ml-scala2.12|
|node_type_id|i3.xlarge|
|driver_node_type_id|i3.xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_count': 0}|
|autoscale|{'min_workers': 2, 'max_workers': 20, 'target_workers': 4}|

#### Cluster Libraries

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|bf024d57582f4c8cbf816151cc6e1bac|
|name|/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example|
|artifact_location|dbfs:/databricks/mlflow-tracking/bf024d57582f4c8cbf816151cc6e1bac|
|lifecycle_stage|active|
|last_update_time|1686872052388|
|creation_time|1686761701458|
|_creation_time|2023-06-14 16:55:01|
|_last_update_time|2023-06-15 23:34:12|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/bf024d57582f4c8cbf816151cc6e1bac|
|_api_link|{'mlflow_client': 'https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow', 'uc_client': 'https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/unity-catalog'}/experiments/get?experiment_id=bf024d57582f4c8cbf816151cc6e1bac|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.experiment.sourceType|REPO_NOTEBOOK|
|mlflow.ownerId|3658755248564160|
|mlflow.experiment.sourceName|/Repos/antoine.amend@databricks.com/mrm-generation/templates/Credit Adjudication - Example|
|mlflow.ownerEmail|antoine.amend@databricks.com|
|mlflow.experiment.sourceId|3022585156450040|

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
    "error": "HTTP status code: 400. Reason: Bad Request URL: https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/bf024d57582f4c8cbf816151cc6e1bac. Params: None. Text: {\"error_code\":\"INVALID_PARAMETER_VALUE\",\"message\":\"For input string: \\\"bf024d57582f4c8cbf816151cc6e1bac\\\"\"}"
  }
}

```