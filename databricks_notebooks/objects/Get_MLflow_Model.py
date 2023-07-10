# Databricks notebook source
# MAGIC %md ## Get MLflow Model
# MAGIC
# MAGIC **Overview**
# MAGIC * Gets the metadata of an MLflow model from the MLmodel file.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model URI` - either the experiment name or the ID
# MAGIC * `Get run` - get run of the experiment
# MAGIC * `Get raw` - get JSON as received from API request
# MAGIC * `Unity Catalog` - use Unity Catalog

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Model URI", "")
dbutils.widgets.dropdown("2. Get run", "no", ["yes","no"])
dbutils.widgets.dropdown("3. Get raw", "no", ["yes","no"])
dbutils.widgets.dropdown("3. Unity Catalog", "no", ["yes","no"])

model_uri = dbutils.widgets.get("1. Model URI")
get_run = dbutils.widgets.get("2. Get run") == "yes"
get_raw = dbutils.widgets.get("3. Get raw") == "yes"
use_uc = dbutils.widgets.get("3. Unity Catalog") == "yes"

print("model_uri:", model_uri)
print("get_run:", get_run)
print("get_raw:", get_raw)
print("use_uc:", use_uc)

# COMMAND ----------

assert_widget(model_uri, "1. Model URI")

activate_unity_catalog(use_uc)

# COMMAND ----------

from mlflow_reports.data import get_mlflow_model

rsp = get_mlflow_model.get(
    model_uri,
    get_run = get_run,
    get_raw = get_raw
)
dump_as_json(rsp)
