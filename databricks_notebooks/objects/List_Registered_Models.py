# Databricks notebook source
# MAGIC %md ## List Registered Models
# MAGIC
# MAGIC **Overview**
# MAGIC * List registered models.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). 
# MAGIC   * `name like '%klearn%'`
# MAGIC * `2. Unity Catalog` - Use Unity Catalog.
# MAGIC * `3. Prefix` - Since UC implementation of `search_registered_models` doesn't support `LIKE` in a filter, show only models starting with this prefix.
# MAGIC   * Note this is client-side logic. 
# MAGIC   * You can just write an SQL query on the Pandas dataframe response as in example below.
# MAGIC * `4. Datetime as string` - Since Spark doesn't honor Pandas datetime second rounding, for human readibility return as formatted string with rounded seconds
# MAGIC * `5. Get tags and aliases` 
# MAGIC * `6. Tags and aliases as string` - Return as string and not Pandas datetime

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Filter", "")
dbutils.widgets.dropdown("2. Unity Catalog", "no", ["yes", "no"])
dbutils.widgets.text("3. Prefix (for UC)", "")
dbutils.widgets.dropdown("4. Datetime as string", "yes", ["yes", "no"])
dbutils.widgets.dropdown("5. Get tags and aliases", "no", ["yes", "no"])
dbutils.widgets.dropdown("6. Tags and aliases as string", "no", ["yes", "no"])

filter = dbutils.widgets.get("1. Filter")
unity_catalog = dbutils.widgets.get("2. Unity Catalog") == "yes"
prefix = dbutils.widgets.get("3. Prefix (for UC)")
datetime_as_string = dbutils.widgets.get("4. Datetime as string") == "yes"
get_tags_and_aliases = dbutils.widgets.get("5. Get tags and aliases") == "yes"
tags_and_aliases_as_string = dbutils.widgets.get("6. Tags and aliases as string") == "yes"

filter = filter or None
prefix = prefix or None

print("filter:", filter)
print("unity_catalog:", unity_catalog)
print("prefix:", prefix)
print("datetime_as_string:", datetime_as_string)
print("get_tags_and_aliases:", get_tags_and_aliases)
print("tags_and_aliases_as_string:", tags_and_aliases_as_string)

# COMMAND ----------

# MAGIC %md ### Search registered models 

# COMMAND ----------

from mlflow_reports.list.search_api import search_registered_models

pandas_df = search_registered_models(
    filter=filter, 
    datetime_as_string = datetime_as_string,
    unity_catalog = unity_catalog,
    prefix = prefix,
    get_tags_and_aliases = True,
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

df.createOrReplaceTempView("models")

# COMMAND ----------

# MAGIC %md #### Sort by `user_id`

# COMMAND ----------

# MAGIC %sql select * from models order by user_id, name

# COMMAND ----------

# MAGIC %md #### Sort by latest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Sort by earliest `creation_timestamp`

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp
