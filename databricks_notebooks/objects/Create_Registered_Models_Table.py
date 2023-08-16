# Databricks notebook source
# MAGIC %md ## Create a table from all registered models
# MAGIC
# MAGIC **Overview**
# MAGIC * Create a table from all registered models.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Table` - Full table name.
# MAGIC * `Table drop` - Drop table before write (because of potential schema conflict on write).
# MAGIC * `Unity Catalog` - Use Unity Catalog.

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

#dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("Table", "")
dbutils.widgets.dropdown("Table drop", "no", ["yes","no"])
dbutils.widgets.dropdown("Unity Catalog", "no", ["yes", "no"])

table_name = dbutils.widgets.get("Table")
drop_table = dbutils.widgets.get("Table drop") == "yes"

unity_catalog = dbutils.widgets.get("Unity Catalog") == "yes"

print("table_name:", table_name)
print("drop_table:", drop_table)
print("unity_catalog:", unity_catalog)

# COMMAND ----------

assert_widget(table_name, "Table")

# COMMAND ----------

# MAGIC %md #### Get all registered models 

# COMMAND ----------

from mlflow_reports.list import search_registered_models

pandas_df = search_registered_models.search(
    unity_catalog = unity_catalog,
    tags_and_aliases_as_string = True
)

# COMMAND ----------

pandas_df

# COMMAND ----------

from pyspark.sql.types import MapType, StringType
from pyspark.sql.functions import from_json

df = spark.createDataFrame(pandas_df)
if "tags" in df.columns:
    df = df.withColumn("tags", from_json(df.tags, MapType(StringType(), StringType())))

display(df)

# COMMAND ----------

# MAGIC %md #### Create table

# COMMAND ----------

if drop_table:
    spark.sql(f"drop table if exists {table_name}")

# COMMAND ----------

df.write.mode("overwrite").saveAsTable(table_name)

# COMMAND ----------

# MAGIC %md #### Describe table

# COMMAND ----------

# MAGIC %sql describe extended ${Table} 

# COMMAND ----------

# MAGIC %sql describe history ${Table} 

# COMMAND ----------

# MAGIC %md #### Query table

# COMMAND ----------

# MAGIC %sql select * from ${Table} order by name

# COMMAND ----------

# MAGIC %sql select user_id, * from ${Table} order by user_id

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from ${Table} group by user_id order by num_models desc
