# Databricks notebook source
# MAGIC %md ## List Databricks Endpoints
# MAGIC
# MAGIC * Last and search registered models, model versions, experiments and runs.
# MAGIC * Script: [../../mlflow_reports/streamlit/list_databricks_endpoints.py]($../../mlflow_reports/streamlit/list_databricks_endpoints.py)
# MAGIC * Note: git raw path does not work yet.

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------


script_paths = mk_script_paths("list_databricks_endpoints.py")

# COMMAND ----------

#dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.dropdown("Script path", "local", ["local","github"])
script_path = dbutils.widgets.get("Script path")

print("script_path:", script_path)
script_path = script_paths[script_path]
print("script_path:", script_path)

# COMMAND ----------

from dbtunnel import dbtunnel
dbtunnel.streamlit(script_path).run()
