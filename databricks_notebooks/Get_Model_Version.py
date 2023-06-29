# Databricks notebook source
# MAGIC %md ## Get model version
# MAGIC **Overview**
# MAGIC * Shows model version details and optionally its run
# MAGIC * Recursively shows all run artifacts up to the specified max level
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Registered model` - either the experiment name or the ID
# MAGIC * `Get run` - get run of the experiment
# MAGIC * `Artifact max level` - number of artifact levels to show
# MAGIC * `Get raw` - get JSON as received from API request

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

dbutils.widgets.text("1. Registered model", "")
dbutils.widgets.text("2. Version", "")
dbutils.widgets.dropdown("3. Get run", "no", ["yes","no"])
dbutils.widgets.text("4. Artifact max level", "1")
dbutils.widgets.dropdown("5. Get raw", "no", ["yes","no"])

reg_model_name = dbutils.widgets.get("1. Registered model")
version = dbutils.widgets.get("2. Version")
get_run = dbutils.widgets.get("3. Get run") == "yes"
artifact_max_level = int(dbutils.widgets.get("4. Artifact max level"))
get_raw = dbutils.widgets.get("5. Get raw") == "yes"

print("reg_model_name:", reg_model_name)
print("version:", version)
print("get_run:", get_run)
print("artifact_max_level:", artifact_max_level)
print("get_raw:", get_raw)

# COMMAND ----------

assert_widget(reg_model_name, "1. Registered model")
assert_widget(version, "2. Version")

# COMMAND ----------

from mlflow_reports.data import get_model_version

rsp = get_model_version.get(reg_model_name, version,
    get_run = get_run,
    artifact_max_level = artifact_max_level,
    get_raw = get_raw
)
dump_as_json(rsp)
