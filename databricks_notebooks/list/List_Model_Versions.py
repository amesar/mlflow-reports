# Databricks notebook source
# MAGIC %md ## List Model Versions
# MAGIC
# MAGIC #### Overview
# MAGIC * List model versions for either the Databricks Workspace (WS) Model Registry or Unity Catalog (UC) Model Registry.
# MAGIC
# MAGIC #### Widgets
# MAGIC * `1. Unity Catalog` - Use Unity Catalog.
# MAGIC * `2. Filter` - `filter_string` argument for for [MlflowClient.search_model_versions](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_model_versions). 
# MAGIC   * Non-UC example: `name like '%klearn%'`.
# MAGIC   * UC: only accepts this filter syntax: `name='andre_catalog.ml_models2.sklearn_wine_best'`.
# MAGIC * `3. Get MLflow model details` - Get MLflow model flavor and size in bytes by reading the run's [MLmodel](https://mlflow.org/docs/latest/models.html?highlight=mlmodel#mlflow-models) file and model artifact(s).
# MAGIC * `4. Get tags and aliases`. Since search_registered_models (for both WS and UC models) does not return tags and aliases (bug), call get_model_version (which does correctly return them) for each returned version.
# MAGIC   * Slows retrieval substantially.
# MAGIC   * https://databricks.atlassian.net/browse/ES-834105
# MAGIC     * UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases
# MAGIC   * https://github.com/mlflow/mlflow/issues/9783
# MAGIC     * MlflowClient.search_model_versions does not return aliases
# MAGIC
# MAGIC #### Sample Performance Benchmarks
# MAGIC
# MAGIC ##### Notes
# MAGIC * Date: 2023-11-29
# MAGIC * Workspace: e2-demo-west
# MAGIC * MLflow version: 2.5.0
# MAGIC * DBR version: 14.1 ML
# MAGIC
# MAGIC ##### Non-UC 
# MAGIC
# MAGIC * Number of versions: 3219
# MAGIC * Ratio: 5.53x or 18% 
# MAGIC
# MAGIC |Tags/Aliases | Seconds | Cell |
# MAGIC |-----|-------|---|
# MAGIC | No | 110 | 1.84 minutes |
# MAGIC | Yes | 597 | 9.95 minutes |
# MAGIC
# MAGIC ##### UC 
# MAGIC
# MAGIC * Number of versions: 1120
# MAGIC * Ratio: 2.26x or 44% 
# MAGIC
# MAGIC |Tags/Aliases | Seconds | Cell |
# MAGIC |-----|-------|---|
# MAGIC | No | 152 | 2.50 minutes |
# MAGIC | Yes | 345 | 5.75 minutes |

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.dropdown("1. Unity Catalog", "no", ["yes", "no"])
dbutils.widgets.text("2. Filter", "")
dbutils.widgets.dropdown("3. Get MLflow model details", "no", ["yes", "no"])
dbutils.widgets.dropdown("4. Get tags and aliases", "no", ["yes", "no"])

unity_catalog = dbutils.widgets.get("1. Unity Catalog") == "yes"
filter = dbutils.widgets.get("2. Filter")
get_model_details = dbutils.widgets.get("3. Get MLflow model details") == "yes"
get_tags_and_aliases = dbutils.widgets.get("4. Get tags and aliases") == "yes"

filter = filter or None

print("unity_catalog:", unity_catalog)
print("filter:", filter)
print("get_model_details:", get_model_details)
print("get_tags_and_aliases:", get_tags_and_aliases)

# COMMAND ----------

# MAGIC %md ### Search model versions

# COMMAND ----------

from mlflow_reports.list import search_model_versions

versions = search_model_versions.search(
    filter = filter, 
    get_tags_and_aliases = get_tags_and_aliases,
    get_model_details = get_model_details,
    unity_catalog = unity_catalog
)
print(f"Model versions: {len(versions)}")
len(versions)

# COMMAND ----------

# MAGIC %md ### Create Spark DataFrame

# COMMAND ----------

df = to_dataframe(versions)

# COMMAND ----------

# MAGIC %md ### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("versions")

# COMMAND ----------

# MAGIC %md ##### Show number of versions per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_versions from versions group by user_id order by num_versions desc

# COMMAND ----------

# MAGIC %md ##### Show number of versions per model

# COMMAND ----------

# MAGIC %sql select name, count(*) as num_versions from versions group by name order by num_versions desc

# COMMAND ----------

# MAGIC %md ##### Sort by `user_id`

# COMMAND ----------

# MAGIC %sql select * from versions order by user_id, name

# COMMAND ----------

# MAGIC %md ##### Sort by latest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Sort by earliest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp

# COMMAND ----------

# MAGIC %md ##### Find all `llama` models

# COMMAND ----------

# MAGIC %sql
# MAGIC select name, version, user_id, creation_timestamp from versions where name like '%%llama%' 
# MAGIC order by creation_timestamp desc
