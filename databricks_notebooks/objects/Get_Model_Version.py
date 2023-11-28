# Databricks notebook source
# MAGIC %md ## Get model version
# MAGIC **Overview**
# MAGIC * Shows model version details and optionally all its related objects
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model name` - model name
# MAGIC * `Version` - model version
# MAGIC * `Expanded view` - Get all objects associated with the model version - run, experiment, registered model and MLmodel
# MAGIC * `Artifact max level` - number of artifact levels to show for the run
# MAGIC * `Get raw` - show JSON objects as returned from API request

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Model name", "")
dbutils.widgets.text("2. Version", "")
dbutils.widgets.dropdown("3. Expanded view", "no", ["yes","no"])
dbutils.widgets.text("4. Artifact max level", "1")
dbutils.widgets.dropdown("5. Get raw", "no", ["yes","no"])

model_name = dbutils.widgets.get("1. Model name")
version = dbutils.widgets.get("2. Version")
get_expanded = dbutils.widgets.get("3. Expanded view") == "yes"
artifact_max_level = int(dbutils.widgets.get("4. Artifact max level"))
get_raw = dbutils.widgets.get("5. Get raw") == "yes"

print("model_name:", model_name)
print("version:", version)
print("get_expanded:", get_expanded)
print("artifact_max_level:", artifact_max_level)
print("get_raw:", get_raw)

# COMMAND ----------

assert_widget(model_name, "1. Model name")
assert_widget(version, "2. Version")

activate_unity_catalog(model_name)

# COMMAND ----------

from mlflow_reports.data import get_model_version

vr = get_model_version.get(model_name, version,
    get_expanded = get_expanded,
    artifact_max_level = artifact_max_level,
    get_raw = get_raw
)

# COMMAND ----------

dump_as_json(vr)
