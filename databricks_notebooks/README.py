# Databricks notebook source
# MAGIC %md ## README - mlflow-reports - Databricks notebooks
# MAGIC
# MAGIC Display details and list MLflow and Databricks endpoints
# MAGIC * MLflow objects: experiments, run, registered models and model versions.
# MAGIC * Databricks endpoints - model serving, vector search endpoints and others.
# MAGIC * Feature tables.
# MAGIC
# MAGIC ##### Git Repo
# MAGIC * https://github.com/amesar/mlflow-reports
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/databricks_notebooks
# MAGIC
# MAGIC #####  Last updated: _2024-05-28_

# COMMAND ----------

# MAGIC %md #### Streamlit MLflow and Databricks API Explorers
# MAGIC
# MAGIC ##### Overview
# MAGIC * Browse MLflow objects and Databricks endpoints as a single pane.
# MAGIC * For listing objects, ability to see both a table view and raw API JSON response.
# MAGIC
# MAGIC ##### Notebooks
# MAGIC * [Streamlit Notebooks README]($streamlit/_README)
# MAGIC * [Streamlit_MLflow_Explorer]($streamlit/Streamlit_MLflow_Explorer) - list and search MLflow objects.
# MAGIC   * Registered models, model versions, experiments and runs.
# MAGIC * [Streamlit_Databricks_Explorer]($streamlit/Streamlit_Databricks_Explorer) - list and search Databricks endpoints.
# MAGIC   * Model serving endpoints, vector search endpoints and vector search indexes.

# COMMAND ----------

# MAGIC %md #### MLflow
# MAGIC
# MAGIC #####  Get MLflow object
# MAGIC * [Get_Model_Version]($objects/Get_Model_Version) with model schema - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/model_versions)
# MAGIC * [Get_Registered_Model]($objects/Get_Registered_Model) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/registered_models)
# MAGIC * [Get_Experiment]($objects/Get_Experiment) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/experiments)
# MAGIC * [Get_Run]($objects/Get_Run) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/runs)
# MAGIC * [Get_Model_Signature]($objects/Get_Model_Signature)
# MAGIC
# MAGIC ##### List MLflow objects
# MAGIC * [List_Registered_Models]($list/List_Registered_Models) - List and query registered models.
# MAGIC * [List_Model_Versions]($list/List_Model_Versions) - List and query model versions.
# MAGIC * [List_Experiments]($list/List_Experiments) - List and query experiments.
# MAGIC
# MAGIC ##### SQL queries for registered models and model versions tables
# MAGIC * Queries for Databricks tables for `models` and `versions` with data returned by the MLflow API.
# MAGIC   * Example:`select user_id, count(*) as num_models from models group by user_id order by num_models desc`
# MAGIC * [Registered_Model_Queries]($sql_analytics/Registered_Model_Queries)
# MAGIC * [Model_Version_Queries]($sql_analytics/Model_Version_Queries)
# MAGIC * [Create_MLflow_Database]($sql_analytics/Create_MLflow_Database) - Create the `models` and `versions` tables.
# MAGIC
# MAGIC ##### MLflow MLmodel
# MAGIC * [Download_MLmodel]($objects/Download_MLmodel) - Download and display a model version's MLmodel artifact.
# MAGIC * [Download_MLmodels]($objects/Download_MLmodels) - Download a list of MLmodel-s.
# MAGIC
# MAGIC ##### Markdown Model report
# MAGIC * [Detailed_Model_Report]($reports/Detailed_Model_Report) - full report for an MLflow model and its related objects
# MAGIC   * Related objects: Run, experiment, registered model, model version and MLflow model objects 
# MAGIC   * Sample entry point: `models:/my_model/123`
# MAGIC   * [Markdown and JSON samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/model_reports)

# COMMAND ----------

# MAGIC %md #### Databricks Endpoints
# MAGIC
# MAGIC ##### Model Serving endpoints aka MLflow deployment endpoints
# MAGIC * [List_Model_Serving_Endpoints]($endpoints/List_Model_Serving_Endpoints) - List and query endpoints.
# MAGIC * [List_Entities_By_Type]($endpoints/List_Entities_By_Type) - List and query all endpoint models/entities broken down by entity type (custom, foundation, etc.).
# MAGIC * [Get_Model_Serving_Endpoint]($endpoints/Get_Model_Serving_Endpoint) 
# MAGIC * [Get_Model_Serving_Endpoint_Signature]($endpoints/Get_Model_Serving_Endpoint_Signature) - Get the model signature of an endpoint entity (custom model only).
# MAGIC
# MAGIC ##### Vector Search endpoints
# MAGIC * [List_Vector_Search_Endpoints]($endpoints/List_Vector_Search_Endpoints) - List and query endpoints.
# MAGIC * [List_Vector_Search_Indexes]($endpoints/List_Vector_Search_Indexes) - List and query all indexes.
# MAGIC * [Get_Vector_Search_Endpoint]($endpoints/Get_Vector_Search_Endpoint) - Get Vector Search endpoint details including its indexes.

# COMMAND ----------

# MAGIC %md #### Feature tables
# MAGIC
# MAGIC * List feature tables
# MAGIC   * [List_Feature_Tables]($feature_store/List_Feature_Tables) - List and query feature tables.
# MAGIC     * Only applies to non-UC features tables created with `FeatureStoreClient`. 
# MAGIC       * Does not apply to UC tables created with `FeatureEngineeringClient`.
# MAGIC     * [List_Feature_Tables_Pandas]($feature_store/List_Feature_Tables_Pandas) - List and query feature tables (Pandas dataframe).
# MAGIC   * [Get_Feature_Tables]($feature_store/Get_Feature_Tables) - Get JSON API response for feature tables.
# MAGIC * [Get_Feature_Table]($feature_store/Get_Feature_Table) - Get feature table details.
# MAGIC

# COMMAND ----------

# MAGIC %md #### Misc
# MAGIC
# MAGIC ##### Unity Catalog notebooks
# MAGIC * [Get_Table]($unity_catalog/Get_Table) - get table details
# MAGIC * [Get_Table_Lineage]($unity_catalog/Get_Table_Lineage) - get table lineage
# MAGIC
# MAGIC ##### Common helper utilities
# MAGIC * [Common]($Common) - [_Common]($_Common)
# MAGIC

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
