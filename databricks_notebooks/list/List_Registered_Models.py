# Databricks notebook source
# MAGIC %md ## List Registered Models
# MAGIC
# MAGIC ##### Overview
# MAGIC * List registered models for either the Unity Catalog (UC) Model Registry or Workspace (WS) Model Registry.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Unity Catalog` - Use Unity Catalog.
# MAGIC * `2. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * Non-UC example: `name like 'Sklearn%'`
# MAGIC   * UC: Does not accept filter so this field is ignored by the MLflow API.
# MAGIC * `3. Prefix` - UC only. Filter registered models that start with this prefix. Used for Unity Catalog models since the `filter` argument is not supported for UC `search_registered_models()`.
# MAGIC * `4. Get tags and aliases (UC)`. Since UC search_registered_models does not return tags and aliases (bug), we call [MlflowClient.get_registered_model](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_registered_model) (which does correctly return them) for each returned model.
# MAGIC   * Non-UC search_registered_models does return tags.
# MAGIC   * Slows retrieval substantially.
# MAGIC   * https://databricks.atlassian.net/browse/ES-834105
# MAGIC     * UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases
# MAGIC * `5. Save as JSON file`
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md #### Sample UC Performance Benchmarks
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

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.dropdown("1. Unity Catalog", "yes", ["yes", "no"])
dbutils.widgets.text("2. Filter", "")
dbutils.widgets.text("3. Prefix", "")
dbutils.widgets.dropdown("4. Get tags and aliases (UC)", "no", ["yes", "no"])
dbutils.widgets.text("5. Save as JSON file","")

unity_catalog = dbutils.widgets.get("1. Unity Catalog") == "yes"
filter = dbutils.widgets.get("2. Filter")
prefix = dbutils.widgets.get("3. Prefix")
get_tags_and_aliases = dbutils.widgets.get("4. Get tags and aliases (UC)") == "yes"
json_file = dbutils.widgets.get("5. Save as JSON file")

filter = filter or None
prefix = prefix or None

print("unity_catalog:", unity_catalog)
print("filter:", filter)
print("prefix:", prefix)
print("get_tags_and_aliases:", get_tags_and_aliases)
print("json_file:", json_file)
if unity_catalog and filter:
    print("WARNING: Filter is ignored by Unity Catalog search_registered_models()")

# COMMAND ----------

# MAGIC %md ### Search registered models 

# COMMAND ----------

from mlflow_reports.list import search_registered_models

models = search_registered_models.search(filter, prefix, get_tags_and_aliases, unity_catalog)
len(models)

# COMMAND ----------

if json_file:
    write_json(json_file, models)

# COMMAND ----------

# MAGIC %md ### Create Spark DataFrame

# COMMAND ----------

df = to_dataframe(models)
display(df)

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

# COMMAND ----------

# MAGIC %md ##### Find all `llama` models

# COMMAND ----------

# MAGIC %sql 
# MAGIC select name, user_id, creation_timestamp from models where name like '%llama%' 
# MAGIC order by creation_timestamp desc
