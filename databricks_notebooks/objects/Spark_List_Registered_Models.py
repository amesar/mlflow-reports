# Databricks notebook source
# MAGIC %md ## Spark List Registered Models
# MAGIC
# MAGIC **Overview**
# MAGIC * List registered models.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * `name like '%klearn%'`
# MAGIC * `2. Datetime as string`
# MAGIC * `3. Unity Catalog`
# MAGIC * `4. Prefix` - Since UC implementation of `search_registered_models` doesn't support `LIKE` in a filter, show only models starting with this prefix.
# MAGIC   * Note this is client-side logic. Or you can just write an SQL query on the Pandas dataframe response.

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Filter", "")
dbutils.widgets.dropdown("2. Datetime as string", "yes", ["yes","no"])
dbutils.widgets.dropdown("3. Unity Catalog", "no", ["yes","no"])
dbutils.widgets.text("4. Prefix", "")

filter = dbutils.widgets.get("1. Filter")
datetime_as_string = dbutils.widgets.get("2. Datetime as string") == "yes"
unity_catalog = dbutils.widgets.get("3. Unity Catalog") == "yes"
prefix = dbutils.widgets.get("4. Prefix")

filter = filter or None
prefix = prefix or None

print("filter:", filter)
print("datetime_as_string:", datetime_as_string)
print("unity_catalog:", unity_catalog)
print("prefix:", prefix)

# COMMAND ----------

from mlflow_reports.client.http_client import get_mlflow_client

if unity_catalog:
    mlflow_utils.use_unity_catalog()
client = get_mlflow_client()
client

# COMMAND ----------

from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator
models = SearchRegisteredModelsIterator(client, filter=filter)
models = list(models)
len(models)

# COMMAND ----------

for m in models:
    m.pop("latest_versions", None)
    print(m)

# COMMAND ----------

for m in models:
    print(m["name"],m.get("tags"))

# COMMAND ----------

# MAGIC %md ### TODO

# COMMAND ----------

df = spark.createDataFrame(pdf)
display(df)

# COMMAND ----------

# MAGIC %md ### Write SQL queries on registered models

# COMMAND ----------

from pyspark.sql.functions import *

df2 = df.select("*").sort("user_id").sort("name")
display(df2)

# COMMAND ----------

df2 = df.select("*").sort(desc("creation_timestamp"))
display(df2)
