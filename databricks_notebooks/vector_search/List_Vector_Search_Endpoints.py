# Databricks notebook source
# MAGIC %md ## List and Query Vector Search Endpoints
# MAGIC * https://docs.databricks.com/en/generative-ai/vector-search.html
# MAGIC * [Vector Search Public Preview API](https://docs.google.com/document/d/1czSOKwnHQG99cYdCk2NbX4dxbRYoDvoKNQdj2RevVL0/edit)

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

!pip install databricks-vectorsearch
dbutils.library.restartPython() 

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient
client = VectorSearchClient(disable_notice=True) 

# COMMAND ----------

endpoints = client.list_endpoints()
endpoints = endpoints["endpoints"]
len(endpoints)

# COMMAND ----------

df = to_dataframe(endpoints)
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("endpoints") 

# COMMAND ----------

# MAGIC %md ##### Show my endpoints

# COMMAND ----------

cmd = f"""
select name, creator, creation_timestamp, num_indexes from endpoints
where creator='{_user}' order by creation_timestamp desc, name
"""
display(spark.sql(cmd))

# COMMAND ----------

# MAGIC %md ##### Show by creation_timestamp

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp, num_indexes from endpoints order by creation_timestamp desc, name

# COMMAND ----------

# MAGIC %md ##### Show by `num_indexes`

# COMMAND ----------

# MAGIC %sql select name, num_indexes, creator, creation_timestamp from endpoints order by num_indexes desc, name

# COMMAND ----------

# MAGIC %md ##### Group by `endpoint_type`

# COMMAND ----------

# MAGIC %sql select endpoint_type, count(*) as count from endpoints group by endpoint_type order by count desc
