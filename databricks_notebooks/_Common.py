# Databricks notebook source
def assert_widget(value, name):
    if len(value.rstrip())==0:
        raise RuntimeError(f"ERROR: '{name}' widget is required")

# COMMAND ----------

def mk_local_path(path):
    return path.replace("dbfs:","/dbfs")

# COMMAND ----------

def dump_as_json(dct, output_file=None, sort_keys=None):
    import json
    content = json.dumps(dct, sort_keys=sort_keys, indent=2)
    print(content)
    if output_file:
        output_file = mk_local_path(output_file)
        print(">> output_file:",output_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

# COMMAND ----------

import mlflow

def show_mlflow_uris(msg):
    print(f"{msg}:")
    print("  mlflow.get_tracking_uri:", mlflow.get_tracking_uri())
    print("  mlflow.get_registry_uri:", mlflow.get_registry_uri())

# COMMAND ----------

def activate_unity_catalog(activate):
    if activate:
        mlflow.set_registry_uri("databricks-uc")
        show_mlflow_uris("After Unity Catalog activation")
