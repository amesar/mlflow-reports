# Databricks notebook source
# MAGIC %md ## Get experiment with all its runs
# MAGIC
# MAGIC **Overview**
# MAGIC * Shows experiment details and optionally its runs
# MAGIC * Recursively shows all run artifacts up to the specified max level
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Experiment ID or name` - either the experiment name or the ID
# MAGIC * `Get runs` - get runs of the experiment
# MAGIC * `Artifact max level` - number of artifact levels to show
# MAGIC * `Get permissions` - Get permissions
# MAGIC * `Get raw` - get JSON as received from API request

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Experiment ID or name", "")
dbutils.widgets.dropdown("2. Get runs", "no", ["yes","no"])
dbutils.widgets.text("3. Artifact max level", "1")
dbutils.widgets.dropdown("4. Get permissions", "yes", ["yes","no"])
dbutils.widgets.dropdown("5. Get raw", "no", ["yes","no"])

experiment_id_or_name = dbutils.widgets.get("1. Experiment ID or name")
get_runs = dbutils.widgets.get("2. Get runs") == "yes"
artifact_max_level = int(dbutils.widgets.get("3. Artifact max level"))
get_permissions = dbutils.widgets.get("4. Get permissions") == "yes"
get_raw = dbutils.widgets.get("5. Get raw") == "yes"

print("experiment_id_or_name:", experiment_id_or_name)
print("get_runs:", get_runs)
print("artifact_max_level:", artifact_max_level)
print("get_permissions:", get_permissions)
print("get_raw:", get_raw)

# COMMAND ----------

assert_widget(experiment_id_or_name, "1. Experiment ID or name")

# COMMAND ----------

from mlflow_reports.data import get_experiment

rsp = get_experiment.get(experiment_id_or_name,
    get_runs = get_runs,
    artifact_max_level = artifact_max_level,
    get_permissions = get_permissions,
    get_raw = get_raw
)
dump_as_json(rsp)
