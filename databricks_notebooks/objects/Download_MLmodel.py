# Databricks notebook source
# MAGIC %md ## Download MLmodel artifact for model version

# COMMAND ----------

dbutils.widgets.text("1. Model name", "")
dbutils.widgets.text("2. Model version", "")
dbutils.widgets.text("3. Output directory", "")

model_name = dbutils.widgets.get("1. Model name")
version = dbutils.widgets.get("2. Model version")
output_dir = dbutils.widgets.get("3. Output directory")

output_dir = output_dir or None

print("model_name:", model_name)
print("version:", version)
print("output_dir:", output_dir)

# COMMAND ----------

def assert_widget(value, name):
    if len(value.rstrip())==0:
        raise RuntimeError(f"ERROR: '{name}' widget is required")
assert_widget(model_name, "1. Model name")
assert_widget(model_name, "2. Model version")

# COMMAND ----------

import mlflow
mlflow.set_registry_uri("databricks-uc")
artifact_uri = f"models:/{model_name}/{version}/MLmodel"
artifact_uri

# COMMAND ----------

from mlflow.artifacts import download_artifacts
local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=output_dir)
local_path

# COMMAND ----------

with open(local_path, "r") as f:
    mlmodel = f.read()
print(mlmodel)
