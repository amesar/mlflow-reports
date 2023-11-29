# Databricks notebook source
# MAGIC %md ## List Registered Models
# MAGIC
# MAGIC ##### Overview
# MAGIC * List registered models for either the Workspace (WS) Model Registry or Unity Catalog (UC) Model Registry.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * Non-UC example: `name like 'Sklearn%'`
# MAGIC   * UC: Does not accept filter so this field is ignored by the MLflow API.
# MAGIC * `2. Unity Catalog` - Use Unity Catalog.
# MAGIC * `3. Get tags and aliases (UC)`. Since UC search_registered_models does not correctly return tags and aliases, call get_registered_model (which does correctly return them) for every returned model.
# MAGIC   * https://databricks.atlassian.net/browse/ES-834105
# MAGIC     * UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases
# MAGIC   * https://github.com/mlflow/mlflow/issues/9783
# MAGIC     * MlflowClient.search_model_versions does not return aliases

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Filter", "")
dbutils.widgets.dropdown("2. Unity Catalog", "no", ["yes", "no"])
dbutils.widgets.dropdown("3. Get tags and aliases (UC)", "no", ["yes", "no"])

filter = dbutils.widgets.get("1. Filter")
unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"
get_tags_and_aliases = dbutils.widgets.get("3. Get tags and aliases (UC)") == "yes"

filter = filter or None

print("filter:", filter)
print("unity_catalog:", unity_catalog)
print("get_tags_and_aliases:", get_tags_and_aliases)

# COMMAND ----------

# MAGIC %md ### Search registered models 

# COMMAND ----------

from mlflow_reports.list import search_registered_models

models = search_registered_models.search(filter, get_tags_and_aliases, unity_catalog)
len(models)

# COMMAND ----------

# MAGIC %md ### Create Spark DataFrame from list of JSON models

# COMMAND ----------

# Preserve original order of columns

columns = get_columns(models)
columns

# COMMAND ----------

df = spark.read.json(sc.parallelize(models)).select(columns)
display(df)

# COMMAND ----------

# MAGIC %md ### Prep SQL queries

# COMMAND ----------

# MAGIC %md #### Convert columns to desired format

# COMMAND ----------

df2 = adjust_timestamps(df)
display(df2)

# COMMAND ----------

# MAGIC %md #### Set SQL table

# COMMAND ----------

df2.createOrReplaceTempView("models")

# COMMAND ----------

# MAGIC %md ### Some SQL queries for registered models

# COMMAND ----------

# MAGIC %md #### Show number of models per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from models group by user_id order by num_models desc

# COMMAND ----------

# MAGIC %md #### Sort by `user_id`

# COMMAND ----------

# MAGIC %sql select user_id, * from models order by user_id, name

# COMMAND ----------

# MAGIC %md #### Sort by latest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Sort by earliest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp
