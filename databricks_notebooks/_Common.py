# Databricks notebook source
# Common utilities

# COMMAND ----------

import os
import json
import mlflow

# COMMAND ----------

def assert_widget(value, name):
    if len(value.rstrip())==0:
        raise RuntimeError(f"ERROR: '{name}' widget is required")

# COMMAND ----------

def mk_local_path(path):
    return path.replace("dbfs:","/dbfs")

# COMMAND ----------

def dump_as_json(dct, output_file=None, silent=False, sort_keys=None):
    content = json.dumps(dct, sort_keys=sort_keys, indent=2)
    if not silent:
        print(content)
    if output_file:
        output_file = mk_local_path(output_file)
        print("output_file:",output_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

def dump_obj(obj, title=None):
    title = title if title else type(obj).__name__
    print(title)
    for k,v in obj.__dict__.items():
        print(f"  {k}: {v}")

# COMMAND ----------

def write_json(path, dct):
    print("Output file:", os.path.abspath(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(dct, indent=2)+"\n")

# COMMAND ----------

def show_mlflow_uris(msg):
    print(f"{msg}:")
    print("  mlflow.get_tracking_uri:", mlflow.get_tracking_uri())
    print("  mlflow.get_registry_uri:", mlflow.get_registry_uri())

# COMMAND ----------

def split_model_uri(model_uri):  
    toks = model_uri.split("/")
    return toks[1], toks[2]

# COMMAND ----------


def is_unity_catalog_model(model_name):
    return "." in model_name
    
def activate_unity_catalog(model_name):
    if model_name.startswith("models:/"):
        model_name = split_model_uri(model_name)[0]
    if is_unity_catalog_model(model_name):
        mlflow.set_registry_uri("databricks-uc")
        show_mlflow_uris("After Unity Catalog activation")
    else:
        mlflow.set_registry_uri("databricks")

# COMMAND ----------

def get_columns(lst):
    set_columns, columns = {}, {}
    for dct in lst:
        set_columns = { **columns, **dct }
        if len(dct.keys()) > len(columns):
            columns = dct
    return list(set_columns.keys())

# COMMAND ----------

from pyspark.sql.functions import *

def adjust_timestamp(df, column):
    return df.withColumn(column,from_unixtime(col(column)/1000, "yyyy-MM-dd hh:mm:ss"))

# COMMAND ----------

def to_dataframe(lst, ts_columns = ["creation_timestamp", "last_updated_timestamp"]):
    """ 
    Default '_ts' arguments are for registered models and model versions. 
    For experiments they are: 'creation_time' and 'last_update_time'. :(
    """
    columns = get_columns(lst)
    df = spark.read.json(sc.parallelize(lst))
    diff = set(columns).difference(set(df.columns))
    columns = [ c for c in columns if c not in diff ]
    print(f"Columns: {columns}")
    df = df.select(columns)
    for col in ts_columns:
        if col in columns:
            df = adjust_timestamp(df, col)
    return df

# COMMAND ----------

import os
print("Versions:")
print(f"  MLflow version: {mlflow.__version__}")
print(f"  DBR version: {os.environ.get('DATABRICKS_RUNTIME_VERSION')}")

# COMMAND ----------

def move_column(df, column, index=1):
    columns = df.columns 
    columns.remove(column)
    columns.insert(index, column)
    df = df.select(*columns)
    return df

# COMMAND ----------

def move_column_to_first(pdf, column):
    columns = list(pdf.columns)
    columns.remove(column)
    columns = [ column ] + columns 
    return pdf[columns]

# COMMAND ----------

import requests

context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
_token = context.apiToken().get()
_host_name = context.tags().get("browserHostName").get()
_auth_headers = { "Authorization": f"Bearer {_token}" }
_base_api_uri = f"https://{_host_name}/api"
print(f"Base API URI:", _base_api_uri)

# COMMAND ----------

def display_schema_uri(database_name, schema_name="Schema"):
    if "." in database_name: # is unity catalog model
        catalog, schema = database_name.split(".")
        uri = f"https://{_host_name}/explore/data/{catalog}/{schema}"
        displayHTML(f'<b>{schema_name}:</b> <a href="{uri}">{uri}</a>')
    else:
        pass # TODO

def display_table_uri(table_name):
    if "." in table_name: # is unity catalog model
        catalog, schema, table_name = table_name.split(".")
        uri = f"https://{_host_name}/explore/data/{catalog}/{schema}/{table_name}"
        displayHTML(f'<b>Table:</b> <a href="{uri}">{uri}</a>')
    else:
        pass # TODO

# COMMAND ----------


