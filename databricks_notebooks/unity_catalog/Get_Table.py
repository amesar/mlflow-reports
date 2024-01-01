# Databricks notebook source
# MAGIC %md ### Get Table
# MAGIC
# MAGIC * Get table details for a Unity Catalog table from the Databricks REST API.
# MAGIC * But example exists in: https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html#retrieve-table-lineage

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("Table", "andre_catalog.fs_wine_uc.wine_features")
table_name = dbutils.widgets.get("Table")
print(f"table_name:", table_name)

# COMMAND ----------

from mlflow_reports.uc.get_table import get
rsp = get(table_name)
dump_as_json(rsp)
