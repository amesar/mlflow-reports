# Databricks notebook source
# MAGIC %md ## MLflow Model Manager
# MAGIC
# MAGIC **Overview**
# MAGIC * Gets the expanded view of an MLflow model from the MLmodel file. An "expanded view" contains all the key objects associated with an MLflow model.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model URI` - either the experiment name or the ID
# MAGIC * `Get run` - get run of the experiment
# MAGIC * `Get raw` - get JSON as received from API request
# MAGIC * `Unity Catalog` - use Unity Catalog

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Model URI", "")
dbutils.widgets.dropdown("2. Get permissions", "yes", ["yes","no"])
dbutils.widgets.dropdown("3. Get raw", "no", ["yes","no"])
dbutils.widgets.dropdown("4. Unity Catalog", "no", ["yes","no"])

model_uri = dbutils.widgets.get("1. Model URI")
get_permissions = dbutils.widgets.get("2. Get permissions") == "yes"
get_raw = dbutils.widgets.get("3. Get raw") == "yes"
use_uc = dbutils.widgets.get("4. Unity Catalog") == "yes"

print("model_uri:", model_uri)
print("permissions:", get_permissions)
print("get_raw:", get_raw)
print("use_uc:", use_uc)

# COMMAND ----------

assert_widget(model_uri, "1. Model URI")

activate_unity_catalog(use_uc)

# COMMAND ----------

# MAGIC %md #### Get the MLfow model info

# COMMAND ----------

from mlflow_reports.mlflow_model import mlflow_model_manager

rsp = mlflow_model_manager.get(
    model_uri,
    get_permissions = get_permissions,
    get_raw = get_raw
)
dump_as_json(rsp)

# COMMAND ----------

# MAGIC %md #### Show the different URIs for the model

# COMMAND ----------

uris = rsp["manifest"]["model_uris"]
data = [ [k,v] for k,v in uris.items() ]
df = pd.DataFrame(data, columns = ["URI type", "URI"])
display(df)
