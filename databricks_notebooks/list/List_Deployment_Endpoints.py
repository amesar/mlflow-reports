# Databricks notebook source
# MAGIC %md ## List Deployment Server Endpoints
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html

# COMMAND ----------

# MAGIC %pip install -U mlflow[skinny]>=2.9.2
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe from API call

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

# MAGIC %md ##### Describe

# COMMAND ----------

# MAGIC %sql describe endpoints

# COMMAND ----------

# MAGIC %md ##### Summary

# COMMAND ----------

# MAGIC  %sql select name, creator, creation_timestamp from endpoints order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as count from endpoints group by creator order by count desc
