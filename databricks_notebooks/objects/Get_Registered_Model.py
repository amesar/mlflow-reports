# Databricks notebook source
# MAGIC %md ## Get registered model
# MAGIC **Overview**
# MAGIC * Shows registered model and optionally the runs of the latest versions
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model name` - registered model
# MAGIC * `Get runs` - get runs of the experiment
# MAGIC * `Artifact max level` - number of artifact levels to show
# MAGIC * `Get permissions` - dump run data if showing runs
# MAGIC * `Get raw` - get JSON as received from API request

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Model name", "")
dbutils.widgets.dropdown("2. Get version run", "no", ["yes","no"])
dbutils.widgets.text("3. Artifact max level", "1")
dbutils.widgets.dropdown("4. Get permissions", "yes", ["yes","no"])
dbutils.widgets.dropdown("5. Get raw", "no", ["yes","no"])

model_name = dbutils.widgets.get("1. Model name")
get_run = dbutils.widgets.get("2. Get version run") == "yes"
artifact_max_level = int(dbutils.widgets.get("3. Artifact max level"))
get_permissions = dbutils.widgets.get("4. Get permissions") == "yes"
get_raw = dbutils.widgets.get("5. Get raw") == "yes"

print("model_name:", model_name)
print("get_run:", get_run)
print("artifact_max_level:", artifact_max_level)
print("get_permissions:", get_permissions)
print("get_raw:", get_raw)

# COMMAND ----------

assert_widget(model_name, "1. Model name")

activate_unity_catalog(model_name)

# COMMAND ----------

from mlflow_reports.data import get_registered_model

rsp = get_registered_model.get(model_name,
    get_run = get_run,
    artifact_max_level = artifact_max_level,
    get_raw = get_raw
)
dump_as_json(rsp)
