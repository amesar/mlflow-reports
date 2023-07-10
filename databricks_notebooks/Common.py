# Databricks notebook source
# MAGIC %pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports

# COMMAND ----------

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
    #print("  mlflowClient.tracking_uri:", client.tracking_uri)
    #print("  mlflowClient.registry_uri:", client._registry_uri)

# COMMAND ----------

def activate_unity_catalog(activate):
    if activate:
        mlflow.set_registry_uri("databricks-uc")
        show_mlflow_uris("After Unity Catalog activation")
    #else:
        #show_mlflow_uris("No Unity Catalog activation")
