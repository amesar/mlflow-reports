# Databricks notebook source
# MAGIC %md ## Get Feature Tables
# MAGIC * Get JSON API response for all feature tables.
# MAGIC * Calls undocumented Databricks REST endpoint `api/2.0/feature-store/feature-tables/search`.

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

# MAGIC %md #### Call REST API endpoint

# COMMAND ----------

from mlflow_reports.feature_store import get_feature_tables
tables = get_feature_tables.list()
print(f"Found {len(tables)} feature tables")

# COMMAND ----------

# MAGIC %md #### Summary

# COMMAND ----------

for tbl in tables:
    print(tbl.get("name"))

# COMMAND ----------

# MAGIC %md #### Full details

# COMMAND ----------

dump_as_json(tables)
