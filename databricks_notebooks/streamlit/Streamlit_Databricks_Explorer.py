# Databricks notebook source
# MAGIC %md ## Streamlit Databricks API Explorer
# MAGIC
# MAGIC * List and get details for registered models, model versions, experiments and runs.
# MAGIC * Script: [../../mlflow_reports/streamlit/databricks_explorer.py]($../../mlflow_reports/streamlit/databricks_explorer.py)
# MAGIC * Note: Using git raw path seems not to work yet.

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

script_paths = mk_script_paths("databricks_explorer.py")

# COMMAND ----------

dbutils.widgets.dropdown("Script path", "local", ["local","github"])
script_path = dbutils.widgets.get("Script path")

print("script_path:", script_path)
script_path = script_paths[script_path]
print("script_path:", script_path)

# COMMAND ----------

from dbtunnel import dbtunnel
dbtunnel.streamlit(script_path).run()
