# Databricks notebook source
!pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
!pip install mlflow_skinny==2.10.1 # NOTE: doesn't honor >= or default version
dbutils.library.restartPython()

# COMMAND ----------

import mlflow
print("MLflow version:", mlflow.__version__)

# COMMAND ----------

# MAGIC %run ./_Common

# COMMAND ----------

from mlflow_reports.common.iterators import SearchRegisteredModelsIterator
from mlflow_reports.common.iterators import SearchModelVersionsIterator

def list_model_versions(max_versions=None):
    versions = []
    for m in SearchRegisteredModelsIterator(client):
        versions += list(SearchModelVersionsIterator(client, filter=f"name='{m.name}'"))
        if max_versions and len(versions) > max_versions:
            break
    return versions
