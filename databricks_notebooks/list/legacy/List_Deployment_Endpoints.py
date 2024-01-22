# Databricks notebook source
# MAGIC %md ## List Deployment Server Endpoints
# MAGIC * /api/2.0/endpoints
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html#deployments-rest-api

# COMMAND ----------

!pip install -U mlflow_skinny
dbutils.library.restartPython()

# COMMAND ----------

import mlflow
mlflow.__version__

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../../_Common

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

# MAGIC %md ##### Summary by creation_timestamp

# COMMAND ----------

# MAGIC  %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Summary by endpoint_type

# COMMAND ----------

# MAGIC  %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by endpoint_type

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as count from endpoints group by creator order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by endpoint_type

# COMMAND ----------

# MAGIC %sql select endpoint_type, count(*) as count from endpoints group by endpoint_type order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by task

# COMMAND ----------

# MAGIC %sql select task, count(*) as count from endpoints group by task order by count desc
