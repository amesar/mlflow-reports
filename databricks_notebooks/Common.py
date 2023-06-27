# Databricks notebook source
# MAGIC %pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports

# COMMAND ----------

def assert_widget(value, name):
    if len(value.rstrip())==0:
        raise RuntimeError(f"ERROR: '{name}' widget is required")

# COMMAND ----------

def dump_as_json(dct, sort_keys=None):
    import json
    print(json.dumps(dct, sort_keys=sort_keys, indent=2))
