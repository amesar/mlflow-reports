# Databricks notebook source
# MAGIC %md ## List and Query Model Serving Endpoints
# MAGIC * https://docs.databricks.com/api/workspace/servingendpoints
# MAGIC * [api/2.0/serving-endpoints](https://docs.databricks.com/api/workspace/servingendpoints/list)

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe

# COMMAND ----------

from mlflow_reports.client.model_serving_client import ModelServingClient

# COMMAND ----------

client = ModelServingClient()

rsp = client.list_endpoints()
endpoints = rsp["endpoints"]
len(endpoints)

# COMMAND ----------

df = to_dataframe(endpoints)
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("endpoints") 

# COMMAND ----------

# MAGIC %md ##### Summary

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp from endpoints order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as count from endpoints group by creator order by count desc
