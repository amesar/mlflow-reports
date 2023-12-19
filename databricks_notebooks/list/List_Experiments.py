# Databricks notebook source
# MAGIC %md ## List and Query Experiments
# MAGIC
# MAGIC #### Overview
# MAGIC * List experiments abnd show some SQL queries.
# MAGIC * Clone this notebook to perform your custom SQL queries.
# MAGIC
# MAGIC #### Widgets
# MAGIC * `1. Filter` - `filter_string` argument for for [MlflowClient.search_experiments](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_experiments).  Examples:
# MAGIC   * `name = 'Sklearn_Wine'`
# MAGIC   * `name like '%Sklearn_Wine%'`
# MAGIC * `2. View type` - Argument to `search_experiments()` - see above.
# MAGIC * `3. Max results` - Argument to `search_experiments()` - see above.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

# MAGIC %md ### Search experiments

# COMMAND ----------

dbutils.widgets.text("1. Filter", "")
filter = dbutils.widgets.get("1. Filter")
filter = filter or None

view_types = [ "ACTIVE", "DELETED_ONLY", "ALL" ]
dbutils.widgets.dropdown("2. View type", view_types[0], view_types)
view_type = dbutils.widgets.get("2. View type")

dbutils.widgets.text("3. Max results", "")
max_results = dbutils.widgets.get("3. Max results")
max_results = int(max_results) if max_results else None

print("filter:", filter)
print("view_type:", view_type)
print("max_results:", max_results)

# COMMAND ----------

from mlflow_reports.list import search_experiments

experiments = search_experiments.search(filter, view_type, max_results)
len(experiments)

# COMMAND ----------

# MAGIC %md ##### Show sample API call result

# COMMAND ----------

if len(experiments) > 0:
    dump_as_json(experiments[0])

# COMMAND ----------

# MAGIC %md ### Create Spark DataFrame

# COMMAND ----------

df = to_dataframe(experiments, "creation_time", "last_update_time")
display(df)

# COMMAND ----------

# MAGIC %md ### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("experiments")

# COMMAND ----------

# MAGIC %md ##### Sort by latest `creation_timestamp` - all columns

# COMMAND ----------

# MAGIC %sql select * from experiments order by creation_time desc

# COMMAND ----------

# MAGIC %md ##### Sort by latest `creation_timestamp`- select columns

# COMMAND ----------

# MAGIC %sql select name, creation_time, lifecycle_stage from experiments order by creation_time desc

# COMMAND ----------

# MAGIC %md #### Repo notebook queries

# COMMAND ----------

# MAGIC %md ##### Group by `lifecycle_stage`

# COMMAND ----------

# MAGIC %sql 
# MAGIC select lifecycle_stage, count(*) as count from experiments 
# MAGIC group by lifecycle_stage order by count desc

# COMMAND ----------

# MAGIC %md ##### Sort by latest `creation_timestamp` - Repo notebooks

# COMMAND ----------

# MAGIC %sql
# MAGIC select name, creation_time, lifecycle_stage from experiments 
# MAGIC where name like '/Repos%' order by creation_time desc

# COMMAND ----------

# MAGIC %sql
# MAGIC select name, creation_time, lifecycle_stage from experiments 
# MAGIC where name like '/Repos/andre.mesar%' 
# MAGIC order by creation_time desc

# COMMAND ----------

# MAGIC %md ##### Try to show deleted Repo experiments
# MAGIC * Note: Apparently they're not tombstoned as 'deleted' in the MLflow database but live somewhere else.

# COMMAND ----------

# MAGIC %sql
# MAGIC select name, creation_time from experiments 
# MAGIC where name like '/Repos%' and lifecycle_stage <> 'active'
# MAGIC order by creation_time desc
