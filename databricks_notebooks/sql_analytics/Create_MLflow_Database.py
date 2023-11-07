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

dbutils.widgets.text("1. Database", "")
database_name = dbutils.widgets.get("1. Database")

dbutils.widgets.dropdown("2. Unity Catalog", "no", ["yes", "no"])
is_unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"

dbutils.widgets.dropdown("3. Get registered model again", "no", ["yes", "no"])
get_search_model_again = dbutils.widgets.get("3. Get registered model again") == "yes"

dbutils.widgets.dropdown("4. Get model version again", "no", ["yes", "no"])
get_search_version_again = dbutils.widgets.get("4. Get model version again") == "yes"

print("database_name:", database_name)
print("is_unity_catalog:", is_unity_catalog)
print("get_search_model_again:", get_search_model_again)
print("get_search_version_again:", get_search_version_again)

# COMMAND ----------

assert_widget(database_name, "1. Database")

models_table = f"{database_name}.models"
versions_table = f"{database_name}.versions"

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
    get_search_object_again = get_search_model_again,
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

# MAGIC %md ##### Show enhanced registered models

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md ##### Write table

# COMMAND ----------

spark.sql(f"drop table if exists {models_table}")
df.write.mode("overwrite").saveAsTable(models_table)

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
    get_search_object_again = get_search_version_again,
    tags_and_aliases_as_string = True,
    get_model_details = False
)
df_versions = spark.createDataFrame(pdf)

# COMMAND ----------

# MAGIC %md ##### Tweak columns

# COMMAND ----------

df = df_versions

df = df \
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss")) \
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss"))

if "tags" in df.columns:
    df = df.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

# COMMAND ----------

# MAGIC %md ##### Show enhanced model versions

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md ##### Write table

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
# MAGIC To query tables, see the [SQL_Queries]($SQL_Queries) notebook.
