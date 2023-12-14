# Databricks notebook source
# MAGIC %md ### Run_SQL_Queries

# COMMAND ----------

notebook = "SQL_Queries"

# COMMAND ----------

params = {
    "Database": "andre_catalog.mlflow_ws",
}
dbutils.notebook.run(notebook, 600,  params)

# COMMAND ----------

params = {
    "Database": "andre_catalog.mlflow_uc",
}
dbutils.notebook.run(notebook, 600,  params)
