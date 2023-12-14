# Databricks notebook source
# MAGIC %md ### Run_SQL_Queries

# COMMAND ----------

notebook = "Create_MLflow_Database"

# COMMAND ----------

# 12.55 min
params = {
    "1. Database": "andre_catalog.mlflow_ws",
    "2. Unity Catalog": "no",
    "3. Get registered model again": "yes",
    "4. Get model version again": "yes"
}
dbutils.notebook.run(notebook, 3000,  params)

# COMMAND ----------

params = {
    "1. Database": "andre_catalog.mlflow_uc",
    "2. Unity Catalog": "yes",
    "3. Get registered model again": "yes",
    "4. Get model version again": "yes"
}
dbutils.notebook.run(notebook, 3000,  params)
