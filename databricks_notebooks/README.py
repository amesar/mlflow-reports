# Databricks notebook source
# MAGIC %md ## README - mlflow-reports - Databricks notebooks
# MAGIC
# MAGIC #####  Get MLflow object notebooks
# MAGIC * [Get_Model_Version]($objects/Get_Model_Version) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/model_versions)
# MAGIC * [Get_Registered_Model]($objects/Get_Registered_Model) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/registered_models)
# MAGIC * [Get_Experiment]($objects/Get_Experiment) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/experiments)
# MAGIC * [Get_Run]($objects/Get_Run) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/runs)
# MAGIC
# MAGIC ##### List MLflow objects notebooks
# MAGIC * [List_Registered_Models]($list/List_Registered_Models) - List and query registered models.
# MAGIC * [List_Model_Versions]($list/List_Model_Versions) - List and query model versions.
# MAGIC * [List_Experiments]($list/List_Experiments) - List and query experiments.
# MAGIC
# MAGIC ##### Endpoint notebooks
# MAGIC * Model Serving endpoints aka MLflow deployment endpoints
# MAGIC   * [List_Model_Serving_Endpoints]($list/List_Model_Serving_Endpoints) - List and query endpoints.
# MAGIC     * [List_Model_Serving_Endpoint_Entities]($list/List_Model_Serving_Endpoint_Entities) - List and query endpoint entities.
# MAGIC     * [List_Model_Serving_Endpoint_Models]($list/List_Model_Serving_Endpoint_Models) - List and query endpoint models/entities broken down by entity type.
# MAGIC   * [Get_Model_Serving_Endpoint]($objects/Get_Model_Serving_Endpoint) 
# MAGIC * Vector Search endpoints
# MAGIC   * [List_Vector_Search_Endpoints]($list/List_Vector_Search_Endpoints) - List and query Vector Search endpoints.
# MAGIC
# MAGIC ##### MLflow MLmodel notebooks
# MAGIC * [Download_MLmodel]($objects/Download_MLmodel) - Download and display a model version's MLmodel artifact.
# MAGIC * [Download_MLmodels]($objects/Download_MLmodels) - Download a list of MLmodel-s.
# MAGIC
# MAGIC ##### SQL queries for MLflow `models` (registered models) and `versions` (model versions) tables
# MAGIC * Queries for Databricks tables for `models` and `versions` as returned by the MLflow API.
# MAGIC   * Example:`select user_id, count(*) as num_models from models group by user_id order by num_models desc`
# MAGIC * [Registered_Model_Queries]($sql_analytics/Registered_Model_Queries)
# MAGIC * [Model_Version_Queries]($sql_analytics/Model_Version_Queries)
# MAGIC * [Create_MLflow_Database]($sql_analytics/Create_MLflow_Database) - Create the `models` and `versions` tables.
# MAGIC
# MAGIC ##### Feature  table notebooks
# MAGIC
# MAGIC * List feature tables
# MAGIC   * [List_Feature_Tables]($feature_store/List_Feature_Tables) - List and query feature tables.
# MAGIC     * Only applies to non-UC features tables created with `FeatureStoreClient`. 
# MAGIC       * Does not apply to UC tables created with `FeatureEngineeringClient`.
# MAGIC     * [List_Feature_Tables_Pandas]($feature_store/List_Feature_Tables_Pandas) - List and query feature tables (Pandas dataframe).
# MAGIC   * [Get_Feature_Tables]($feature_store/Get_Feature_Tables) - Get JSON API response for feature tables.
# MAGIC * [Get_Feature_Table]($feature_store/Get_Feature_Table) - Get feature table details.
# MAGIC
# MAGIC ##### Unity Catalog notebooks
# MAGIC * [Get_Table]($unity_catalog/Get_Table) - get table details
# MAGIC * [Get_Table_Lineage]($unity_catalog/Get_Table_Lineage) - get table lineage
# MAGIC
# MAGIC #####  Markdown Model report
# MAGIC * [Detailed_Model_Report]($reports/Detailed_Model_Report) - full report for an MLflow model and its related objects
# MAGIC   * Related objects: Run, experiment, registered model, model version and MLflow model objects 
# MAGIC   * Sample entry point: `models:/my_model/123`
# MAGIC   * [Markdown and JSON samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/model_reports)
# MAGIC
# MAGIC ##### Common helper utilities
# MAGIC * [Common]($Common) - [_Common]($_Common)
# MAGIC
# MAGIC
# MAGIC
# MAGIC ##### Git Repo
# MAGIC * https://github.com/amesar/mlflow-reports
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/databricks_notebooks
# MAGIC
# MAGIC #####  Last updated: _2024-02-18_

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Legacy
# MAGIC
# MAGIC ##### List
# MAGIC * [List_Model_Serving_Endpoints]($list/legacy/List_Model_Serving_Endpoints) - List and query model serving endpoints.
# MAGIC * [List_Deployment_Endpoints]($list/legacy/List_Deployment_Endpoints) - List and query deployment endpoints.
# MAGIC * [List_Gateway_Routes]($list/legacy/List_Gateway_Routes) - List and query AI Gateway routes (deprecated).
# MAGIC
# MAGIC
# MAGIC ##### Get
# MAGIC * [Get_MLflow_Model]($objects/Get_MLflow_Model) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/mlflow_models) 
# MAGIC * [MLflow_Model_Manager]($objects/MLflow_Model_Manager) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/model_reports)
