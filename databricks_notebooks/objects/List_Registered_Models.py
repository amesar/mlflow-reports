# Databricks notebook source
# MAGIC %md ## List Registered Models
# MAGIC
# MAGIC ##### Overview
# MAGIC * List registered models for either the Workspace (WS) Model Registry or Unity Catalog (UC) Model Registry.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Unity Catalog` - Use Unity Catalog.
# MAGIC * `2. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * Non-UC example: `name like 'Sklearn%'`
# MAGIC   * UC: Does not accept filter so this field is ignored by the MLflow API.
# MAGIC * `3. Get tags and aliases (UC)`. Since UC search_registered_models does not return tags and aliases (bug), call get_registered_model (which does correctly return them) for each returned model.
# MAGIC   * Non-UC search_registered_models does return tags.
# MAGIC   * Slows retrieval substantially.
# MAGIC   * https://databricks.atlassian.net/browse/ES-834105
# MAGIC     * UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases
# MAGIC
# MAGIC ##### UC Performance Benchmarks
# MAGIC
# MAGIC Notes:
# MAGIC * Date: 2023-11-29
# MAGIC * Workspace: e2-demo-west
# MAGIC * MLflow version: 2.5.0
# MAGIC * DBR version: 14.1 ML
# MAGIC
# MAGIC Overview:
# MAGIC * Number of models: 480
# MAGIC * Ratio: 24x or 4.17%
# MAGIC
# MAGIC |Tags/Aliases | Seconds | Cell |
# MAGIC |-----|-------|---|
# MAGIC | No | 4  | 4 seconds |
# MAGIC | Yes | 96 | 1.60 minutes |
# MAGIC

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.dropdown("1. Unity Catalog", "no", ["yes", "no"])
dbutils.widgets.text("2. Filter", "")
dbutils.widgets.dropdown("3. Get tags and aliases (UC)", "no", ["yes", "no"])

unity_catalog = dbutils.widgets.get("1. Unity Catalog") == "yes"
filter = dbutils.widgets.get("2. Filter")
get_tags_and_aliases = dbutils.widgets.get("3. Get tags and aliases (UC)") == "yes"

filter = filter or None

print("unity_catalog:", unity_catalog)
print("filter:", filter)
print("get_tags_and_aliases:", get_tags_and_aliases)
if unity_catalog and filter:
    print("WARNING: Filter is not supported by Unity Catalog search_registered_models()")

# COMMAND ----------

# MAGIC %md ### Search registered models 

# COMMAND ----------

from mlflow_reports.list import search_registered_models

models = search_registered_models.search(filter, get_tags_and_aliases, unity_catalog)
len(models)

# COMMAND ----------

# MAGIC %md ### Create Spark DataFrame

# COMMAND ----------

df = to_dataframe(models)

# COMMAND ----------

# MAGIC %md ### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("models")

# COMMAND ----------

# MAGIC %md ##### Show number of models per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from models group by user_id order by num_models desc

# COMMAND ----------

# MAGIC %md ##### Sort by `user_id`

# COMMAND ----------

# MAGIC %sql select user_id, * from models order by user_id, name

# COMMAND ----------

# MAGIC %md ##### Sort by latest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Sort by earliest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp
