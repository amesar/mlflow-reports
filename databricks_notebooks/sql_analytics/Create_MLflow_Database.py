# Databricks notebook source
# MAGIC %md ## Create MLflow Database
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC Create a database for registered models and model versions as returned by the MLflow API.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Database` - full path name such as `my_catalog.mlflow_uc`.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("Database", "")
database_name = dbutils.widgets.get("Database")
print("database_name:", database_name)

# COMMAND ----------

assert_widget(database_name, "Database")

is_unity_catalog = len(database_name.split(".")) == 2
models_table = f"{database_name}.models"
versions_table = f"{database_name}.versions"

print("is_unity_catalog:", is_unity_catalog)
print("models_table:", models_table)
print("versions_table:", versions_table)

# COMMAND ----------

# MAGIC %md ### Registered models table

# COMMAND ----------

# MAGIC %md ##### Call API

# COMMAND ----------

from mlflow_reports.list import search_registered_models

pdf = search_registered_models.search(
    unity_catalog = is_unity_catalog,
    tags_and_aliases_as_string = True
)
df = spark.createDataFrame(pdf)

# COMMAND ----------

# MAGIC %md ##### Tweak columns

# COMMAND ----------

from pyspark.sql.functions import *

df = df\
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss")) \
  .withColumn("last_updated_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss"))

if "tags" in df.columns:
    from pyspark.sql.types import MapType, StringType
    from pyspark.sql.functions import from_json
    df = df.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

# COMMAND ----------

# MAGIC %md ##### Show registered models tables

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md ##### Write to table

# COMMAND ----------

spark.sql(f"drop table if exists {models_table}")
df.write.mode("overwrite").saveAsTable(f"{models_table}")

# COMMAND ----------

# MAGIC %md ##### Describe table

# COMMAND ----------

df = spark.sql(f"describe extended {models_table}")
display(df)

# COMMAND ----------

# MAGIC %md ### Model Versions table

# COMMAND ----------

# MAGIC %md ##### Call API

# COMMAND ----------

from mlflow_reports.list import search_model_versions

pdf = search_model_versions.search(
    unity_catalog = is_unity_catalog,
    tags_and_aliases_as_string = True,
    get_model_details = False
)
df_versions = spark.createDataFrame(pdf)

# COMMAND ----------

# MAGIC %md ##### Tweak columns

# COMMAND ----------

df = df_versions

df = df\
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss")) \
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss"))

if "tags" in df.columns:
    df = df.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

# COMMAND ----------

# MAGIC %md ##### Show model versions table
# MAGIC
# MAGIC display(df)

# COMMAND ----------

spark.sql(f"drop table if exists {versions_table}")
df.write.mode("overwrite").saveAsTable(f"{versions_table}")

# COMMAND ----------

# MAGIC %md ##### Describe model versions table

# COMMAND ----------

df = spark.sql(f"describe extended {versions_table}")
display(df)

# COMMAND ----------

# MAGIC %md ### Some SQL queries 

# COMMAND ----------

spark.sql(f"use {database_name}")

# COMMAND ----------

# MAGIC %md ##### Show table count

# COMMAND ----------

# MAGIC %sql select count(*) as num_models from models;

# COMMAND ----------

# MAGIC %sql select count(*) as num_versions from versions;

# COMMAND ----------

# MAGIC %md ##### Show number of models per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from models group by user_id order by num_models desc

# COMMAND ----------

# MAGIC %md ### See next notebook
# MAGIC
# MAGIC TO query tables, see the [SQL_Queries]($SQL_Queries) notebook.
