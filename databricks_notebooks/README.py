# Databricks notebook source
# MAGIC %md ## README - mlflow-reports - Databricks notebooks
# MAGIC
# MAGIC #####  Model reports
# MAGIC * [Detailed_Model_Report]($reports/Detailed_Model_Report) - full report of MLflow model and its related objects.
# MAGIC   *  Run, experiment, registered model, model version and MLflow model objects. 
# MAGIC   * [Samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/model_reports)
# MAGIC
# MAGIC #####  MLflow object detailed (all attributes) dump notebooks.
# MAGIC * [MLflow_Model_Manager]($objects/MLflow_Model_Manager) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/model_reports)
# MAGIC * [Get_MLflow_Model]($objects/Get_MLflow_Model) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/mlflow_models) 
# MAGIC * [Get_Registered_Model]($objects/Get_Registered_Model) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/registered_models)
# MAGIC * [Get_Model_Version]($objects/Get_Model_Version) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/model_versions)
# MAGIC * [Get_Experiment]($objects/Get_Experiment) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/experiments)
# MAGIC * [Get_Run]($objects/Get_Run) - [samples](https://github.com/amesar/mlflow-reports/tree/master/samples/databricks/mlflow_objects/runs)
# MAGIC
# MAGIC ##### MLflow list notebooks
# MAGIC * [List_Registered_Models]($objects/List_Registered_Models)
# MAGIC * [List_Model_Versions]($objects/List_Model_Versions)
# MAGIC
# MAGIC ##### SQL queries for MLflow models and versions tables
# MAGIC * Queries for a Databricks Spark database with tables for models and versions as returned by the MLflow API.
# MAGIC * `select user_id, count(*) as num_models from models group by user_id order by num_models desc`
# MAGIC * [Registered_Model_Queries]($sql_analytics/Registered_Model_Queries)
# MAGIC * [Model_Version_Queries]($sql_analytics/Model_Version_Queries)
# MAGIC * [Create_MLflow_Database]($sql_analytics/Create_MLflow_Database) - Create the `models` and `versions` tables.
# MAGIC
# MAGIC ##### Other
# MAGIC * [Common]($Common)
# MAGIC
# MAGIC ##### Git Repo
# MAGIC * https://github.com/amesar/mlflow-reports
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/databricks_notebooks
# MAGIC
# MAGIC Last updated: 2023-11-23
