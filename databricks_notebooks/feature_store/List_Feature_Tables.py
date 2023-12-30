# Databricks notebook source
# MAGIC %md ## List Feature Tables
# MAGIC * Call undocumented Databricks REST endpoint `api/2.0/feature-store/feature-tables/search`.
# MAGIC
# MAGIC
# MAGIC ##### Error
# MAGIC * Spark JSON conversion fails to convert boolean JSON attribute 'is_exported'
# MAGIC
# MAGIC AnalysisException: [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column, variable, or function parameter with name `name` cannot be resolved. Did you mean one of the following? [`_corrupt_record`].;
# MAGIC 'Project ['name, 'creation_timestamp, 'last_updated_timestamp, 'creator_id, 'description, 'primary_keys, 'features, 'data_sources, 'online_stores, 'notebook_producers, 'last_update_user_id, 'id, 'permission_level, 'timestamp_keys, 'is_imported]
# MAGIC +- LogicalRDD [_corrupt_record#63], false

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

# MAGIC %md #### Create feature tables dataframe from API call

# COMMAND ----------

from mlflow_reports.feature_store import search_feature_tables

tables = search_feature_tables.search()
len(tables)

# COMMAND ----------

# Convert boolean "is_imported" field to string to avoid conversion error
_key = "is_imported"
for dct in tables:
    dct[_key] = str(dct[_key] )

# COMMAND ----------

df = to_dataframe(tables)
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("tables") 

# COMMAND ----------

# MAGIC %md ##### Describe

# COMMAND ----------

# MAGIC %sql describe tables

# COMMAND ----------

# MAGIC %md ##### Group by creator_id

# COMMAND ----------

# MAGIC %sql select creator_id, count(*) as count from tables group by creator_id order by count desc

# COMMAND ----------

# MAGIC %md ##### Show by creator_id

# COMMAND ----------

# MAGIC  %sql select name, creator_id, creation_timestamp from tables order by creator_id, creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Show by creation_timestamp

# COMMAND ----------

# MAGIC  %sql select name, creator_id, creation_timestamp from tables order by creation_timestamp desc, creator_id
