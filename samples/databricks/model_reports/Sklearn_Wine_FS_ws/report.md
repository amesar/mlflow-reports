
MLflow Model: _models:/Sklearn_Wine_FS_ws/production_
=====================================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
* [Raw Model - Feature Store](#raw-model---feature-store)
	* [Details](#details)
	* [Flavors](#flavors)
	* [Feature Spec](#feature-spec)
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
|model_uri|models:/Sklearn_Wine_FS_ws/production|
|flavor|databricks.feature_store.mlflow_model|
|flavor_version||
|mlflow_version|2.4.0|
|size_bytes|29,211|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|time_created|2023-06-07 04:05:46|
|report_time|2023-07-06 04:10:49|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/Sklearn_Wine_FS_ws/production|
|run_uri|runs:/464405b7866b44f49ef191fb85fbb9c0/fs-model|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/5e376f92cf304fd6a6629b30c19d99b9/models/fs-model|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3022585156485563/464405b7866b44f49ef191fb85fbb9c0/artifacts/fs-model|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|fs-model|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.4.0|
|model_uuid|156c2abf5ad9451e8385a7df9312416d|
|run_id|464405b7866b44f49ef191fb85fbb9c0|
|utc_time_created|2023-06-07 04:05:46.020494|

### Flavors

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|data|data/feature_store|
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|databricks.feature_store.mlflow_model|
|python_version|3.10.6|

## Signature
  
**_<font color="red" size="+1">None found</font>_**
## Saved input example info
  
**_<font color="red" size="+1">None found</font>_**
# Raw Model - Feature Store

## Details
  

|Name|Value|
| :--- | :--- |
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.4.0|
|model_uuid|9630e657d17e45babf4bc685cf0828de|
|utc_time_created|2023-06-07 04:05:42.977891|

## Flavors

### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|mlflow.sklearn|
|model_path|model.pkl|
|predict_fn|predict|
|python_version|3.10.6|

### Flavor 'sklearn'
  

|Name|Value|
| :--- | :--- |
|code|None|
|pickled_model|model.pkl|
|serialization_format|cloudpickle|
|sklearn_version|1.2.2|

## Feature Spec
  
```
{
  "input_columns": [
    {
      "real_time_measurement": {
        "source": "training_data"
      }
    },
    {
      "alcohol": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "alcohol",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "chlorides": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "chlorides",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "citric_acid": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "citric_acid",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "density": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "density",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "fixed_acidity": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "fixed_acidity",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "free_sulfur_dioxide": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "free_sulfur_dioxide",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "pH": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "pH",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "residual_sugar": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "residual_sugar",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "sulphates": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "sulphates",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "total_sulfur_dioxide": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "total_sulfur_dioxide",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    },
    {
      "volatile_acidity": {
        "table_name": "andre_fs_wine.wine_features",
        "feature_name": "volatile_acidity",
        "lookup_key": [
          "wine_id"
        ],
        "source": "feature_store"
      }
    }
  ],
  "workspace_id": 2556758628403379,
  "feature_store_client_version": "0.12.0",
  "input_tables": [
    {
      "andre_fs_wine.wine_features": {
        "table_id": "cbf338b0fb5244909fa8f78252c07b20"
      }
    }
  ],
  "serialization_version": 6
}

```
# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|Sklearn_Wine_FS_ws|
|creation_timestamp|1686110900942|
|last_updated_timestamp|1688210607861|
|user_id|andre@mycompany.com|
|id|d738f78b4186497e9fdb58baacc22ea9|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-06-07 04:08:21|
|_last_updated_timestamp|2023-07-01 11:23:28|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Sklearn_Wine_FS_ws|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=Sklearn_Wine_FS_ws|

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
    "object_id": "/registered-models/d738f78b4186497e9fdb58baacc22ea9",
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
|name|Sklearn_Wine_FS_ws|
|version|1|
|creation_timestamp|1686110901211|
|last_updated_timestamp|1688210607861|
|user_id|andre@mycompany.com|
|current_stage|Production|
|source|dbfs:/databricks/mlflow-tracking/3022585156485563/464405b7866b44f49ef191fb85fbb9c0/artifacts/fs-model|
|run_id|464405b7866b44f49ef191fb85fbb9c0|
|status|READY|
|_creation_timestamp|2023-06-07 04:08:21|
|_last_updated_timestamp|2023-07-01 11:23:28|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/5e376f92cf304fd6a6629b30c19d99b9/models/fs-model|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3022585156485563/464405b7866b44f49ef191fb85fbb9c0/artifacts/fs-model|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/Sklearn_Wine_FS_ws/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=Sklearn_Wine_FS_ws&version=1|

## Tags
  

|Name|Value|
| :--- | :--- |
|info|my FS workspace experiment|

# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|464405b7866b44f49ef191fb85fbb9c0|
|run_uuid|464405b7866b44f49ef191fb85fbb9c0|
|experiment_id|3022585156485563|
|run_name|crawling-goat-570|
|status|FINISHED|
|start_time|1686110741216|
|end_time|1686110747957|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3022585156485563/464405b7866b44f49ef191fb85fbb9c0/artifacts|
|lifecycle_stage|active|
|_start_time|2023-06-07 04:05:41|
|_end_time|2023-06-07 04:05:48|
|_duration|6.741|
|_experiment_name|/Users/andre@mycompany.com/experiments/Sklearn_Wine_FS_ws|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3022585156485563/runs/464405b7866b44f49ef191fb85fbb9c0|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=464405b7866b44f49ef191fb85fbb9c0|

## Params
  

|Param|Value|
| :--- | :--- |
|bootstrap|True|
|ccp_alpha|0.0|
|criterion|squared_error|
|max_depth|3|
|max_features|1.0|
|max_leaf_nodes|None|
|max_samples|None|
|min_impurity_decrease|0.0|
|min_samples_leaf|1|
|min_samples_split|2|
|min_weight_fraction_leaf|0.0|
|n_estimators|20|
|n_jobs|None|
|oob_score|False|
|random_state|42|
|verbose|0|
|warm_start|False|

## Metrics
  

|Metric|Value|
| :--- | :--- |
|mean_squared_error_X_test|0.5503835246159617|
|r2_score_X_test|0.289344589379501|
|test_mse|0.5503835246159617|
|test_r2_score|0.289344589379501|
|training_mean_absolute_error|0.5811756733612624|
|training_mean_squared_error|0.544009401235841|
|training_r2_score|0.30823973901147106|
|training_root_mean_squared_error|0.737569929725881|
|training_score|0.30823973901147106|

## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|7862010846746489700_8576419968538388899_32ce3d20937f433e95ed6ccc27dc86ee|
|mlflow.databricks.notebookID|3022585156450267|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/Feature_Store/work_02/Sklearn_Wine_FS|
|mlflow.databricks.notebookRevisionID|1686110748091|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0414-154233-qm0df4rx|
|mlflow.databricks.cluster.info|{'cluster_name': 'andre_ML_13.1', 'spark_version': '13.1.x-cpu-ml-scala2.12', 'node_type_id': 'i3.xlarge', 'driver_node_type_id': 'i3.xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_count': 0}, 'num_workers': 1}|
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
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/Feature_Store/work_02/Sklearn_Wine_FS|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'fs-model', 'flavors': {'python_function': {'loader_module': 'databricks.feature_store.mlflow_model', 'python_version': '3.10.6', 'data': 'data/feature_store', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}}, 'run_id': '464405b7866b44f49ef191fb85fbb9c0', 'model_uuid': '156c2abf5ad9451e8385a7df9312416d', 'utc_time_created': '2023-06-07 04:05:46.020494', 'mlflow_version': '2.4.0', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.runName|crawling-goat-570|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|estimator_class|sklearn.ensemble._forest.RandomForestRegressor|
|estimator_name|RandomForestRegressor|
|info|my FS workspace experiment run|
|sparkDatasourceInfo|[{'path': 'dbfs:/databricks-datasets/wine-quality/winequality-white.csv', 'format': 'text'}, {'path': 'dbfs:/databricks-datasets/wine-quality/winequality-white.csv', 'format': 'csv'}, {'path': 'dbfs:/user/hive/warehouse/andre_fs_wine.db/wine_features', 'version': '1', 'format': 'delta'}]|

### Exploded Tags

#### Spark Datasources
  

|Format|Version|Path|
| :--- | :--- | :--- |
|text||dbfs:/databricks-datasets/wine-quality/winequality-white.csv|
|csv||dbfs:/databricks-datasets/wine-quality/winequality-white.csv|
|delta|1|dbfs:/user/hive/warehouse/andre_fs_wine.db/wine_features|

#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0414-154233-qm0df4rx|
|cluster_name|andre_ML_13.1|
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
|experiment_id|3022585156485563|
|name|/Users/andre@mycompany.com/experiments/Sklearn_Wine_FS_ws|
|artifact_location|dbfs:/databricks/mlflow-tracking/3022585156485563|
|lifecycle_stage|active|
|last_update_time|1686110741216|
|creation_time|1686110707590|
|_creation_time|2023-06-07 04:05:08|
|_last_update_time|2023-06-07 04:05:41|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3022585156485563|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3022585156485563|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.note.content|my FS workspace experiment|
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/experiments/Sklearn_Wine_FS_ws|
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
    "object_id": "/experiments/3022585156485563",
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