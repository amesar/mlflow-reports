# Databricks notebook source
# MAGIC %md ## Create MLflow Database
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC Creates a database with two tables:
# MAGIC * `models`: All registered models from calling API endpoint `2.0/mlflow/registered-models/search`
# MAGIC * `versions`: All model verfsions from calling API endpoint `2.0/mlflow/model-versions/search`
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Database` - full path name such as `andre_catalog.mlflow_uc` or `andre_catalog.mlflow_ws`.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Database", "andre_catalog.mlflow_uc")
database_name = dbutils.widgets.get("1. Database")

dbutils.widgets.dropdown("2. Unity Catalog", "yes", ["yes", "no"])
unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"

dbutils.widgets.dropdown("3. Get model tags and aliases", "yes", ["yes", "no"])
get_tags_and_aliases_models = dbutils.widgets.get("3. Get model tags and aliases") == "yes"

dbutils.widgets.dropdown("4. Get version tags and aliases", "yes", ["yes", "no"])
get_tags_and_aliases_versions = dbutils.widgets.get("4. Get version tags and aliases") == "yes"

print("database_name:", database_name)
print("unity_catalog:", unity_catalog)
print("get_tags_and_aliases_models:", get_tags_and_aliases_models)
print("get_tags_and_aliases_versions:", get_tags_and_aliases_versions)

# COMMAND ----------

assert_widget(database_name, "1. Database")

models_table = f"{database_name}.models"
versions_table = f"{database_name}.versions"

print("models_table:  ", models_table)
print("versions_table:", versions_table)

# COMMAND ----------

# MAGIC %md ### Registered models table

# COMMAND ----------

# MAGIC %md ##### Call API

# COMMAND ----------

from mlflow_reports.list import search_registered_models

models = search_registered_models.search(None, get_tags_and_aliases_models, unity_catalog)
len(models)

# COMMAND ----------

df = to_dataframe(models)
display(df)

# COMMAND ----------

# MAGIC %md ##### Write table

# COMMAND ----------

df.write.mode("overwrite").option("mergeSchema", "true").saveAsTable(models_table)

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

versions = search_model_versions.search(
    get_tags_and_aliases = get_tags_and_aliases_versions,
    unity_catalog = unity_catalog
)
print(f"Model versions: {len(versions)}")
len(versions)

# COMMAND ----------

df = to_dataframe(versions)
display(df)

# COMMAND ----------

# MAGIC %md ##### Write table

# COMMAND ----------

df.write.mode("overwrite").option("mergeSchema", "true").saveAsTable(versions_table)

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

# MAGIC %md ##### Show number of models/versions per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from models group by user_id order by num_models desc

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_versions from versions group by user_id order by num_versions desc

# COMMAND ----------

# MAGIC %md ### See query notebooks
# MAGIC
# MAGIC For more queries see 
# MAGIC [Registered_Model_Queries]($Registered_Model_Queries) and [Model_Version_Queries]($Model_Version_Queries) notebooks.
