
MLflow Model: _models:/AutoML_Wine_2023_05_21/production_
=========================================================

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
|model_uri|models:/AutoML_Wine_2023_05_21/production|
|flavor|mlflow.sklearn|
|flavor_version|1.1.1|
|mlflow_version|2.3.1|
|size_bytes|48,377|
|databricks_runtime||
|time_created|2023-05-21 18:38:57|
|report_time|2023-07-06 04:02:16|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/AutoML_Wine_2023_05_21/production|
|run_uri|runs:/5249e62f29a244ecb86126951ab1db99/model|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/54c5eca441e2494bbe5284ec12202d3a/models/model|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/536189130327910/5249e62f29a244ecb86126951ab1db99/artifacts/model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|model|
|mlflow_version|2.3.1|
|model_uuid|c04504c9820642b0bec2cdc5bb4728bd|
|run_id|5249e62f29a244ecb86126951ab1db99|
|utc_time_created|2023-05-21 18:38:57.262370|

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
|sklearn_version|1.1.1|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|fixed acidity|double|
|volatile acidity|double|
|citric acid|double|
|residual sugar|double|
|chlorides|double|
|free sulfur dioxide|double|
|total sulfur dioxide|double|
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

# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|AutoML_Wine_2023_05_21|
|creation_timestamp|1688280673949|
|last_updated_timestamp|1688280860424|
|user_id|andre@mycompany.com|
|id|8ee59f96ec7e44f1af766542c79435fe|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-07-02 06:51:14|
|_last_updated_timestamp|2023-07-02 06:54:20|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/AutoML_Wine_2023_05_21|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=AutoML_Wine_2023_05_21|

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
    "object_id": "/registered-models/8ee59f96ec7e44f1af766542c79435fe",
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
        "display_name": "feifei-service-principal-e2-demo-west-ws-do-not-delete",
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
|name|AutoML_Wine_2023_05_21|
|version|1|
|creation_timestamp|1688280674258|
|last_updated_timestamp|1688280860424|
|user_id|andre@mycompany.com|
|current_stage|Production|
|source|dbfs:/databricks/mlflow-tracking/536189130327910/5249e62f29a244ecb86126951ab1db99/artifacts/model|
|run_id|5249e62f29a244ecb86126951ab1db99|
|status|READY|
|_creation_timestamp|2023-07-02 06:51:14|
|_last_updated_timestamp|2023-07-02 06:54:20|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/54c5eca441e2494bbe5284ec12202d3a/models/model|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/536189130327910/5249e62f29a244ecb86126951ab1db99/artifacts/model|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/AutoML_Wine_2023_05_21/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=AutoML_Wine_2023_05_21&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|5249e62f29a244ecb86126951ab1db99|
|run_uuid|5249e62f29a244ecb86126951ab1db99|
|experiment_id|536189130327910|
|run_name|legendary-ray-459|
|status|FINISHED|
|start_time|1684694336103|
|end_time|1684694344038|
|artifact_uri|dbfs:/databricks/mlflow-tracking/536189130327910/5249e62f29a244ecb86126951ab1db99/artifacts|
|lifecycle_stage|active|
|_start_time|2023-05-21 18:38:56|
|_end_time|2023-05-21 18:39:04|
|_duration|7.935|
|_experiment_name|/Users/andre@mycompany.com/experiments/automl/AutoML_Wine_2023_05_21_a|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/536189130327910/runs/5249e62f29a244ecb86126951ab1db99|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=5249e62f29a244ecb86126951ab1db99|

## Params
  

|Param|Value|
| :--- | :--- |
|column_selector|ColumnSelector(cols=['alcohol', 'density', 'fixed acidity', 'residual sugar',<br/>                     'sulphates', 'volatile acidity', 'citric acid',<br/>                     'free sulfur dioxide', 'pH', 'chlorides',<br/>                     'total sulfur dioxide'])|
|column_selector__cols|['alcohol', 'density', 'fixed acidity', 'residual sugar', 'sulphates', 'volatile acidity', 'citric acid', 'free sulfur dioxide', 'pH', 'chlorides', 'total sulfur dioxide']|
|memory|None|
|preprocessor|ColumnTransformer(remainder='passthrough', sparse_threshold=0,<br/>                  transformers=[('numerical',<br/>                                 Pipeline(steps=[('converter',<br/>                                                  FunctionTransformer(func=<function <lambda> at 0x7f3779c3dab0>)),<br/>                                                 ('imputers',<br/>                                                  ColumnTransformer(transformers=[('impute_mean',<br/>                                                 ...|
|preprocessor__n_jobs|None|
|preprocessor__numerical|Pipeline(steps=[('converter',<br/>                 FunctionTransformer(func=<function <lambda> at 0x7f3779c3dab0>)),<br/>                ('imputers',<br/>                 ColumnTransformer(transformers=[('impute_mean',<br/>                                                  SimpleImputer(),<br/>                                                  ['alcohol', 'chlorides',<br/>                                                   'citric acid', 'density',<br/>                                                   'fixed acidity',<br/>   ...|
|preprocessor__numerical__converter|FunctionTransformer(func=<function <lambda> at 0x7f3779c3dab0>)|
|preprocessor__numerical__converter__accept_sparse|False|
|preprocessor__numerical__converter__check_inverse|True|
|preprocessor__numerical__converter__feature_names_out|None|
|preprocessor__numerical__converter__func|<function <lambda> at 0x7f3779c3dab0>|
|preprocessor__numerical__converter__inv_kw_args|None|
|preprocessor__numerical__converter__inverse_func|None|
|preprocessor__numerical__converter__kw_args|None|
|preprocessor__numerical__converter__validate|False|
|preprocessor__numerical__imputers|ColumnTransformer(transformers=[('impute_mean', SimpleImputer(),<br/>                                 ['alcohol', 'chlorides', 'citric acid',<br/>                                  'density', 'fixed acidity',<br/>                                  'free sulfur dioxide', 'pH', 'residual sugar',<br/>                                  'sulphates', 'total sulfur dioxide',<br/>                                  'volatile acidity'])])|
|preprocessor__numerical__imputers__impute_mean|SimpleImputer()|
|preprocessor__numerical__imputers__impute_mean__add_indicator|False|
|preprocessor__numerical__imputers__impute_mean__copy|True|
|preprocessor__numerical__imputers__impute_mean__fill_value|None|
|preprocessor__numerical__imputers__impute_mean__missing_values|nan|
|preprocessor__numerical__imputers__impute_mean__strategy|mean|
|preprocessor__numerical__imputers__impute_mean__verbose|deprecated|
|preprocessor__numerical__imputers__n_jobs|None|
|preprocessor__numerical__imputers__remainder|drop|
|preprocessor__numerical__imputers__sparse_threshold|0.3|
|preprocessor__numerical__imputers__transformer_weights|None|
|preprocessor__numerical__imputers__transformers|[('impute_mean', SimpleImputer(), ['alcohol', 'chlorides', 'citric acid', 'density', 'fixed acidity', 'free sulfur dioxide', 'pH', 'residual sugar', 'sulphates', 'total sulfur dioxide', 'volatile acidity'])]|
|preprocessor__numerical__imputers__verbose|False|
|preprocessor__numerical__imputers__verbose_feature_names_out|True|
|preprocessor__numerical__memory|None|
|preprocessor__numerical__standardizer|StandardScaler()|
|preprocessor__numerical__standardizer__copy|True|
|preprocessor__numerical__standardizer__with_mean|True|
|preprocessor__numerical__standardizer__with_std|True|
|preprocessor__numerical__steps|[('converter', FunctionTransformer(func=<function <lambda> at 0x7f3779c3dab0>)), ('imputers', ColumnTransformer(transformers=[('impute_mean', SimpleImputer(),<br/>                                 ['alcohol', 'chlorides', 'citric acid',<br/>                                  'density', 'fixed acidity',<br/>                                  'free sulfur dioxide', 'pH', 'residual sugar',<br/>                                  'sulphates', 'total sulfur dioxide',<br/>                                  'volatile acidity...|
|preprocessor__numerical__verbose|False|
|preprocessor__remainder|passthrough|
|preprocessor__sparse_threshold|0|
|preprocessor__transformer_weights|None|
|preprocessor__transformers|[('numerical', Pipeline(steps=[('converter',<br/>                 FunctionTransformer(func=<function <lambda> at 0x7f3779c3dab0>)),<br/>                ('imputers',<br/>                 ColumnTransformer(transformers=[('impute_mean',<br/>                                                  SimpleImputer(),<br/>                                                  ['alcohol', 'chlorides',<br/>                                                   'citric acid', 'density',<br/>                                                   'fixe...|
|preprocessor__verbose|False|
|preprocessor__verbose_feature_names_out|True|
|regressor|LGBMRegressor(colsample_bytree=0.7777905133862134, lambda_l1=2.610389982397478,<br/>              lambda_l2=0.9298812609436371, learning_rate=0.27177322704504847,<br/>              max_bin=170, max_depth=11, min_child_samples=116, n_estimators=24,<br/>              num_leaves=158, random_state=835198998,<br/>              subsample=0.7160184639493279)|
|regressor__boosting_type|gbdt|
|regressor__class_weight|None|
|regressor__colsample_bytree|0.7777905133862134|
|regressor__importance_type|split|
|regressor__lambda_l1|2.610389982397478|
|regressor__lambda_l2|0.9298812609436371|
|regressor__learning_rate|0.27177322704504847|
|regressor__max_bin|170|
|regressor__max_depth|11|
|regressor__min_child_samples|116|
|regressor__min_child_weight|0.001|
|regressor__min_split_gain|0.0|
|regressor__n_estimators|24|
|regressor__n_jobs|-1|
|regressor__num_leaves|158|
|regressor__objective|None|
|regressor__random_state|835198998|
|regressor__reg_alpha|0.0|
|regressor__reg_lambda|0.0|
|regressor__silent|warn|
|regressor__subsample|0.7160184639493279|
|regressor__subsample_for_bin|200000|
|regressor__subsample_freq|0|
|steps|[('column_selector', ColumnSelector(cols=['alcohol', 'density', 'fixed acidity', 'residual sugar',<br/>                     'sulphates', 'volatile acidity', 'citric acid',<br/>                     'free sulfur dioxide', 'pH', 'chlorides',<br/>                     'total sulfur dioxide'])), ('preprocessor', ColumnTransformer(remainder='passthrough', sparse_threshold=0,<br/>                  transformers=[('numerical',<br/>                                 Pipeline(steps=[('converter',<br/>                             ...|
|verbose|False|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|test_example_count|996.0|
|test_max_error|3.074402894637739|
|test_mean_absolute_error|0.5134546573457012|
|test_mean_absolute_percentage_error|0.09059602865307287|
|test_mean_on_target|5.899598393574297|
|test_mean_squared_error|0.43817150609937155|
|test_r2_score|0.4390214018818217|
|test_root_mean_squared_error|0.6619452440341056|
|test_score|0.4390214018818217|
|test_sum_on_target|5876.0|
|training_example_count|2937.0|
|training_max_error|3.396381889882912|
|training_mean_absolute_error|0.47978896802293824|
|training_mean_absolute_percentage_error|0.08489937476073763|
|training_mean_on_target|5.865509022812393|
|training_mean_squared_error|0.39236534342405316|
|training_r2_score|0.5079257048031887|
|training_root_mean_squared_error|0.6263907274409904|
|training_score|0.5079257048031887|
|training_sum_on_target|17227.0|
|val_example_count|920.0|
|val_max_error|3.045958339807912|
|val_mean_absolute_error|0.5394772338588673|
|val_mean_absolute_percentage_error|0.09395823663026384|
|val_mean_on_target|5.890217391304348|
|val_mean_squared_error|0.4867401457148646|
|val_r2_score|0.3490432462871078|
|val_root_mean_squared_error|0.6976676470317831|
|val_score|0.3490432462871078|
|val_sum_on_target|5419.0|

## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebookID|536189130328609|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|Notebook: LightGBMRegressor|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.datasets|[{'name': '527bce1909134eed0d0b93e60603cd77', 'hash': '527bce1909134eed0d0b93e60603cd77', 'model': '31e23e54e5bb4ddd8d1ddf5da55ddecb'}, {'name': '435c410d4f55bbcec3ebe66e02487765', 'hash': '435c410d4f55bbcec3ebe66e02487765', 'model': '31e23e54e5bb4ddd8d1ddf5da55ddecb'}, {'name': '69270c4dfa097d87466461501c0b8322', 'hash': '69270c4dfa097d87466461501c0b8322', 'model': '31e23e54e5bb4ddd8d1ddf5da55ddecb'}]|
|mlflow.log-model.history|[{'artifact_path': 'model', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'name': 'fixed acidity', 'type': 'double'}, {'name': 'volatile acidity', 'type': 'double'}, {'name': 'citric acid', 'type': 'double'}, {'name': 'residual sugar', 'type': 'double'}, {'name': 'chlorides', 'type': 'double'}, {'name': 'free sulfur dioxide', 'type': 'double'}, {'name': 'total sulfur dioxide', 'type': 'double'}, {'name': 'density', 'type': 'double'}, {'name': 'pH', 'type': 'double'}, {'name': 'sulphates', 'type': 'double'}, {'name': 'alcohol', 'type': 'double'}], 'outputs': [{'type': 'tensor', 'tensor-spec': {'dtype': 'float64', 'shape': [-1]}}]}, 'flavors': {'python_function': {'predict_fn': 'predict', 'model_path': 'model.pkl', 'loader_module': 'mlflow.sklearn', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}, 'python_version': '3.10.6'}, 'sklearn': {'pickled_model': 'model.pkl', 'sklearn_version': '1.1.1', 'serialization_format': 'cloudpickle', 'code': None}}, 'run_id': '5249e62f29a244ecb86126951ab1db99', 'model_uuid': 'c04504c9820642b0bec2cdc5bb4728bd', 'utc_time_created': '2023-05-21 18:38:57.262370', 'mlflow_version': '2.3.1'}]|
|mlflow.runName|legendary-ray-459|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|estimator_class|sklearn.pipeline.Pipeline|
|estimator_name|Pipeline|
|model_type|lightgbm_regressor|

### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|536189130327910|
|name|/Users/andre@mycompany.com/experiments/automl/AutoML_Wine_2023_05_21_a|
|artifact_location|dbfs:/databricks/mlflow-tracking/536189130327910|
|lifecycle_stage|active|
|last_update_time|1684694380002|
|creation_time|1684694060380|
|_creation_time|2023-05-21 18:34:20|
|_last_update_time|2023-05-21 18:39:40|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/536189130327910|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=536189130327910|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/experiments/automl/AutoML_Wine_2023_05_21_a|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experimentType|MLFLOW_EXPERIMENT|

### User Tags
  

|Key|Value|
| :--- | :--- |
|_databricks_automl|True|
|_databricks_automl.alerts.high_correlation_cols|{'version': 1, 'severity': 'low', 'affected': {'values': [{'id': 'alcohol', 'type': None}, {'id': 'chlorides', 'type': None}, {'id': 'density', 'type': None}, {'id': 'free sulfur dioxide', 'type': None}, {'id': 'residual sugar', 'type': None}], 'others': 1}}|
|_databricks_automl.best_trial_notebook_id|536189130328609|
|_databricks_automl.compute_mode|CLASSIC|
|_databricks_automl.data_dir|None|
|_databricks_automl.end_time|1684694380|
|_databricks_automl.evaluation_metric|val_root_mean_squared_error|
|_databricks_automl.evaluation_metric_order_by_asc|True|
|_databricks_automl.exploration_notebook_id|536189130327927|
|_databricks_automl.job_run_id|196379917|
|_databricks_automl.max_trials|10000|
|_databricks_automl.problem_type|regression|
|_databricks_automl.source_gui|False|
|_databricks_automl.start_time|1684694075|
|_databricks_automl.state|SUCCESS|
|_databricks_automl.table_name|global_temp.automl_86e5f35f_b868_4986_9118_aaa43d5ee6d9|
|_databricks_automl.target_col|quality|
|_databricks_automl.timeout_minutes|5|

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
    "object_id": "/experiments/536189130327910",
    "object_type": "mlflowExperiment",
    "access_control_list": [
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