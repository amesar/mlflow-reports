# Databricks notebook source
# MAGIC %md ### Download the MLmodel artifact of a model version
# MAGIC
# MAGIC Downloads the MLmodel file of the "cached" registry MLflow model, not from the runs's MLflow model.
# MAGIC
# MAGIC ```
# MAGIC ├── model
# MAGIC │   ├── MLmodel
# MAGIC │   ├── conda.yaml
# MAGIC │   ├── input_example.json
# MAGIC │   ├── model.pkl
# MAGIC │   ├── python_env.yaml
# MAGIC │   └── requirements.txt
# MAGIC ```

# COMMAND ----------

# MAGIC %run ../_Common

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

assert_widget(model_name, "1. Model name")
assert_widget(version, "2. Model version")

# COMMAND ----------

activate_unity_catalog(model_name)
artifact_uri = f"models:/{model_name}/{version}/MLmodel"
artifact_uri

# COMMAND ----------

import mlflow
from mlflow.artifacts import download_artifacts
local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=output_dir)
local_path

# COMMAND ----------

with open(local_path, "r") as f:
    mlmodel = f.read()
print(mlmodel)
