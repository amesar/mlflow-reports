# Databricks notebook source
# MAGIC %md ## List Feature Tables (Pandas)
# MAGIC * Call undocumented Databricks REST endpoint `api/2.0/feature-store/feature-tables/search`.
# MAGIC * We use Pandas dataframe since Spark dataframe JSON conversion fails on boolean attribute.
# MAGIC
# MAGIC #### Widgets
# MAGIC * `Rows` - show only this number of first rows.
# MAGIC
# MAGIC #### Error
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

dbutils.widgets.text("Rows", "")
num_rows = dbutils.widgets.get("Rows")
if num_rows:
    num_rows = int(num_rows) 
print(f"num_rows:", num_rows)

# COMMAND ----------

# MAGIC %md #### Create dataframe from API call

# COMMAND ----------

from mlflow_reports.feature_store import search_feature_tables
df = search_feature_tables.search_as_pandas_df()
df.shape

# COMMAND ----------

if num_rows:
    df = df.head(num_rows)
df

# COMMAND ----------

# MAGIC %md #### Summary

# COMMAND ----------

df2 = df[["name", "creator_id", "creation_timestamp"]]
df2

# COMMAND ----------

# MAGIC %md #### Group by `creator_id`

# COMMAND ----------

group = df.groupby(['creator_id']).size()
df2 = group.to_frame(name='count').reset_index()
df2.sort_values(by=["count"], inplace=True, ascending=False)
df2

# COMMAND ----------

# MAGIC %md #### Show by `creator_id`

# COMMAND ----------

df.sort_values(by = ["creator_id", "creation_timestamp"], inplace=True, ascending= [True, False])
df2 = move_column_to_first(df, "creator_id")
df2

# COMMAND ----------

# MAGIC %md #### Show by `creation_timestamp`

# COMMAND ----------

df.sort_values(by=["creation_timestamp"], inplace=True, ascending=False)
df
