# Databricks notebook source
!pip install -U git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
!pip install -U mlflow_skinny==2.13.0 # NOTE: doesn't honor >= or default version
!pip install starlette
dbutils.library.restartPython()

# COMMAND ----------

import mlflow
print("MLflow version:", mlflow.__version__)

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

# COMMAND ----------

# MAGIC %run ./_Common
