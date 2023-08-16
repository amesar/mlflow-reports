# Databricks notebook source
# MAGIC %md ## List Model Versions
# MAGIC
# MAGIC **Overview**
# MAGIC * List model versions.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_model_versions](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_model_versions). 
# MAGIC   * Non-UC example: `name like '%klearn%'`
# MAGIC   * UC: only accepts this filter syntax: `name='andre_catalog.ml_models2.tmp`
# MAGIC * `2. Unity Catalog` - Use Unity Catalog.
# MAGIC * `3. Get tags and aliases` 
# MAGIC * `4. Get model details` - Get MLflow model flavor and size in bytes.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Filter", "")
dbutils.widgets.dropdown("2. Unity Catalog", "no", ["yes", "no"])
dbutils.widgets.dropdown("3. Get MLflow model details", "no", ["yes", "no"])

filter = dbutils.widgets.get("1. Filter")
unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"
get_model_details = dbutils.widgets.get("3. Get MLflow model details") == "yes"

filter = filter or None

print("filter:", filter)
print("unity_catalog:", unity_catalog)
print("get_model_details:", get_model_details)

# COMMAND ----------

# MAGIC %md ### Search model versions

# COMMAND ----------

from mlflow_reports.list import search_model_versions

pandas_df = search_model_versions.search(
    filter = filter, 
    unity_catalog = unity_catalog,
    get_model_details = get_model_details
)

# COMMAND ----------

# MAGIC %md ### Display Pandas DataFrame

# COMMAND ----------

pandas_df

# COMMAND ----------

# MAGIC %md ### Display as Spark DataFrame

# COMMAND ----------

df = spark.createDataFrame(pandas_df)
display(df)

# COMMAND ----------

# MAGIC %md ### Some SQL queries for registered models

# COMMAND ----------

# MAGIC %md #### Select desired columns and convert to desired format

# COMMAND ----------


columns = [ "name", "version", "user_id", "creation_timestamp" ]

if "model_flavor" in df.columns and "model_size" in df.columns:
    columns.append("model_flavor")
    columns.append("model_size")
    
if "tags" in df.columns:
    columns.append("tags")
if "aliases" in df.columns:
    columns.append("aliases")

columns

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import MapType, StringType

df2 = df.select(columns) \
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss"))

if "tags" in columns:
    df2 = df2.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

display(df2)

# COMMAND ----------

# MAGIC %md #### Set SQL table

# COMMAND ----------

df2.createOrReplaceTempView("versions")

# COMMAND ----------

# MAGIC %md #### Show number of versions per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_versions from versions group by user_id order by num_versions desc

# COMMAND ----------

# MAGIC %md #### Show number of versions per model

# COMMAND ----------

# MAGIC %sql select name, count(*) as num_versions from versions group by name order by num_versions desc

# COMMAND ----------

# MAGIC %md #### Sort by `user_id`

# COMMAND ----------

# MAGIC %sql select * from versions order by user_id, name

# COMMAND ----------

# MAGIC %md #### Sort by latest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Sort by earliest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp
