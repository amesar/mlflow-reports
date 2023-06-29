# Databricks notebook source
# MAGIC %run ./Common

# COMMAND ----------

# MAGIC %md ## Get run with artifacts
# MAGIC
# MAGIC **Overview**
# MAGIC * Shows run details and optionally lists its artifacts
# MAGIC * Recursively shows all run artifacts up to the specified max level
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Run ID`
# MAGIC * `Artifact max level` - number of artifact levels to show
# MAGIC * `Get raw` - get JSON as received from API request

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

dbutils.widgets.text("1. Run ID", "")
dbutils.widgets.text("2. Artifact max level", "1")
dbutils.widgets.dropdown("3. Get raw", "no", ["yes","no"])

run_id = dbutils.widgets.get("1. Run ID")
artifact_max_level = int(dbutils.widgets.get("2. Artifact max level"))
get_raw = dbutils.widgets.get("3. Get raw") == "yes"


print("run_id:", run_id)
print("artifact_max_level:", artifact_max_level)
print("get_raw:", get_raw)

# COMMAND ----------

assert_widget(run_id, "1. Run ID")

# COMMAND ----------

from mlflow_reports.data import get_run

rsp = get_run.get(run_id,
    artifact_max_level = artifact_max_level,
    get_raw = get_raw
)
dump_as_json(rsp)
