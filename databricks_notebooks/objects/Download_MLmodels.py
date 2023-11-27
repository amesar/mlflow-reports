# Databricks notebook source
# MAGIC %md ## Download list of MLmodels
# MAGIC
# MAGIC ##### Widget
# MAGIC * `1. Input file` - contains model URIs to download, e.g. `models:/ml.llm-catalog.mistral-7b/1`.
# MAGIC   * See `sample_model_version_uris.csv`.
# MAGIC * 2. `Output directory` - Directory where MLmodel files will be saved.
# MAGIC   * Each file name will be the full path name of the model plus the version: `ml.llm-catalog.mistral-7b.1.yaml` 

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("1. Input file", "sample_model_uris.csv")
dbutils.widgets.text("2. Output directory", "/tmp/mlmodel_files")

input_file = dbutils.widgets.get("1. Input file")
output_dir = dbutils.widgets.get("2. Output directory")

output_dir = output_dir or None

print("input_file:", input_file)
print("output_dir:", output_dir)

# COMMAND ----------

assert_widget(output_dir, "2. Output directory")

# COMMAND ----------

# MAGIC %md #### Sample model URIs that overrides the input file for convenience

# COMMAND ----------

model_uris = [
    "models:/andre_m.ml_models.sklearn_wine_best/9",
    "models:/marketplace_staging_llama_2_models.models.llama_2_7b_chat_hf/1"
]

# COMMAND ----------

# MAGIC %md #### Read model URI input file if specified

# COMMAND ----------

if input_file:  
    print(f"Reading from '{input_file}'")
    with open(input_file, "r") as f:
        model_uris = f.read().splitlines()

# COMMAND ----------

assert len(model_uris) > 0
activate_unity_catalog(model_uris[0])

model_uris

# COMMAND ----------

import os
import mlflow
from mlflow.artifacts import download_artifacts
from mlflow.exceptions import RestException

def download(model_uri, output_dir):
    print("====================")
    artifact_uri = os.path.join(model_uri, "MLmodel")
    name, version  = split_model_uri(artifact_uri)
    output_path = os.path.join(output_dir, f"{name}.{version}.yaml")
    print("output_path:", output_path)
    try:
        local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=output_dir)
        print("local_path:", local_path)
        os.rename(local_path, output_path)
        return output_path
    except RestException as e:
        print(f"ERROR: {model_uri}: {e}")
        return None

# COMMAND ----------

for model_uri in model_uris:
    download(model_uri, output_dir)

# COMMAND ----------

# MAGIC %md #### Show downloaded files

# COMMAND ----------

os.environ["OUTPUT_DIR"] = output_dir

# COMMAND ----------

# MAGIC %sh echo $OUTPUT_DIR

# COMMAND ----------

# MAGIC %sh ls -l $OUTPUT_DIR

# COMMAND ----------

# MAGIC %sh 
# MAGIC # for convenience 
# MAGIC # rm $OUTPUT_DIR/*
