# Databricks notebook source
# MAGIC %md ## List Registered Models
# MAGIC
# MAGIC **Overview**
# MAGIC * List registered models for either the Databricks Workspace (WS) Model Registry or Unity Catalog (UC) Model Registry.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * Non-UC example: `name like '%klearn%'`
# MAGIC   * UC: Does not accept filter so is ignored by the MLflow API.
# MAGIC * `2. Unity Catalog` - Use Unity Catalog.
# MAGIC * `3. Get registered model again`. Since UC search_registered_models does not correctly return tags and aliases, call get_registered_model (which does correctly return them) for every returned model.
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
dbutils.widgets.dropdown("3. Get registered model again", "no", ["yes", "no"])

filter = dbutils.widgets.get("1. Filter")
unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"
get_search_object_again = dbutils.widgets.get("3. Get registered model again") == "yes"

filter = filter or None

print("filter:", filter)
print("unity_catalog:", unity_catalog)
print("get_search_object_again:", get_search_object_again)

# COMMAND ----------

# MAGIC %md ### Search registered models 

# COMMAND ----------

from mlflow_reports.list import search_registered_models

pandas_df = search_registered_models.search(
    filter = filter, 
    get_search_object_again = get_search_object_again,
    unity_catalog = unity_catalog,
    tags_and_aliases_as_string = True
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

# MAGIC %md #### Convert columns to desired format

# COMMAND ----------

from pyspark.sql.functions import *

df2 = df\
  .withColumn("creation_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss")) \
  .withColumn("last_updated_timestamp",date_format("creation_timestamp", "yyyy-MM-dd hh:mm:ss"))

if "tags" in df.columns:
    from pyspark.sql.types import MapType, StringType
    from pyspark.sql.functions import from_json
    df2 = df2.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

display(df2)

# COMMAND ----------

# MAGIC %md #### Set SQL table

# COMMAND ----------

df2.createOrReplaceTempView("models")

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
