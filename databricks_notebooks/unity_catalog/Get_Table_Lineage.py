# Databricks notebook source
# MAGIC %md ### Get Table Lineage
# MAGIC
# MAGIC * Get table lineage for a Unity Catalog table from the Databricks REST API.
# MAGIC * Not documented in Databricks REST API docs
# MAGIC * But example exists in: https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html#retrieve-table-lineage

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("Table", "andre_catalog.fs_wine_uc.wine_features")
table_name = dbutils.widgets.get("Table")
print(f"table_name:", table_name)

# COMMAND ----------

uri = f"{_base_api_uri}/2.0/lineage-tracking/table-lineage"
uri

# COMMAND ----------

rsp = requests.get(uri, headers=_auth_headers, json={"table_name": table_name})
dump_as_json(rsp.json())
