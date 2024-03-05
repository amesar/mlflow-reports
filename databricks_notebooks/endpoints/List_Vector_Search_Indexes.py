# Databricks notebook source
# MAGIC %md ## List and Query Vector Search Indexes
# MAGIC
# MAGIC * Query all vector search indexes.

# COMMAND ----------

!pip install databricks-vectorsearch
dbutils.library.restartPython() 

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

# MAGIC %md #### Create indexes dataframe

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient
client = VectorSearchClient(disable_notice=True) 

# COMMAND ----------

endpoints = client.list_endpoints()["endpoints"]
indexes = [ client.list_indexes(ep["name"]).get("vector_indexes",[]) for ep in endpoints ]
indexes = [ _idx for _indexes in indexes for _idx in _indexes]
len(indexes)

# COMMAND ----------

if len(indexes) == 0:
    msg = "No indexes exist for any endpoints"
    print(msg)
    dbutils.notebook.exit(msg)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df = to_dataframe(indexes)
df.createOrReplaceTempView("indexes") 
display(df)

# COMMAND ----------

# MAGIC %md ##### Show my indexes

# COMMAND ----------

cmd = f"""
select endpoint_name, name, primary_key, index_type, creator from indexes
where creator='{_user}' order by endpoint_name, name
"""
display(spark.sql(cmd))

# COMMAND ----------

# MAGIC %md ##### Show by endpoint name

# COMMAND ----------

# MAGIC %sql select endpoint_name, name, creator, primary_key, index_type from indexes order by endpoint_name, name

# COMMAND ----------

# MAGIC %md ##### Show by index name

# COMMAND ----------

# MAGIC %sql select name, endpoint_name, creator, primary_key, index_type from indexes order by name, endpoint_name

# COMMAND ----------

# MAGIC %md ##### Show by creator

# COMMAND ----------

# MAGIC %sql select creator, endpoint_name, name, primary_key, index_type from indexes order by creator, endpoint_name, name

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as num_indexes from indexes group by creator order by num_indexes desc

# COMMAND ----------

# MAGIC %md ##### Group by index_type

# COMMAND ----------

# MAGIC %sql select index_type, count(*) as count from indexes group by index_type order by count desc

# COMMAND ----------

# MAGIC %sql select primary_key, count(*) as count from indexes group by primary_key order by count desc
