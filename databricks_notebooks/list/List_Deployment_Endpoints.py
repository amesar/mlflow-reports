# Databricks notebook source
# MAGIC %md ## List Deployment Server Endpoints
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html

# COMMAND ----------

# MAGIC %pip install mlflow[skinny]
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe

# COMMAND ----------

from mlflow.deployments import get_deploy_client
client = get_deploy_client("databricks")
client

# COMMAND ----------

endpoints = client.list_endpoints()
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

# MAGIC %sql select name, creator, creation_timestamp, endpoint_type from endpoints order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Group by endpoint_type

# COMMAND ----------

# MAGIC %sql select endpoint_type, count(*) as count from endpoints group by endpoint_type order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as count from endpoints group by creator order by count desc
