# Databricks notebook source
# MAGIC %md ## List and Query Model Serving Endpoints
# MAGIC
# MAGIC List and query "model serving endpoints" aka MLflow "deployment endpoints".
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC You can access model serving endpoints in two different ways:
# MAGIC * Direct call to the Databricks REST endpoint `api/2.0/serving-endpoints`
# MAGIC * Using the `DatabricksDeploymentClient` which under the hood calls the above endpoint. 
# MAGIC
# MAGIC A bit confusing to have two different ways to return the same data. 
# MAGIC
# MAGIC It is not clear whether the contract of `DatabricksDeploymentClient` is guaranteed to stay in sync `api/2.0/serving-endpoints`.
# MAGIC
# MAGIC ##### Databricks API documentation
# MAGIC * `api/2.0/serving-endpoints` - https://docs.databricks.com/api/workspace/servingendpoints
# MAGIC
# MAGIC ##### MLflow mlflow.deployments documentation
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html
# MAGIC * https://mlflow.org/docs/latest/llms/deployments/index.html#deployments-rest-api
# MAGIC
# MAGIC ##### Github
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/mlflow_reports/endpoints

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.dropdown("1. Endpoint client", "DatabricksDeploymentClient", [
                           "DatabricksDeploymentClient", 
                           "Direct call to api/2.0/serving-endpoints"])
dbutils.widgets.dropdown("2. Show JSON", "no", ["yes","no"])
dbutils.widgets.text("3. Save JSON as file", "")

endpoint_client = dbutils.widgets.get("1. Endpoint client") 
call_databricks_model_serving = endpoint_client != "DatabricksDeploymentClient"
show_json = dbutils.widgets.get("2. Show JSON") == "yes"
output_file = dbutils.widgets.get("3. Save JSON as file")

print("endpoint_client:", endpoint_client)
print("call_databricks_model_serving:", call_databricks_model_serving)
print("show_json:", show_json)
print("output_file:", output_file)

# COMMAND ----------

# MAGIC %md #### Get JSON response from API call

# COMMAND ----------

from mlflow_reports.endpoints import get_endpoint_client
client = get_endpoint_client(call_databricks_model_serving)

# COMMAND ----------

endpoints = client.list_endpoints()

# NOTE: Databricks api/2.0/serving-endpoints returns dict and not list as DatabricksDeploymentClient does
if isinstance(endpoints, dict): 
    endpoints = endpoints["endpoints"]
    
len(endpoints)

# COMMAND ----------

if output_file or show_json:
    dump_as_json(endpoints, output_file, silent=not show_json)

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe

# COMMAND ----------

df = to_dataframe(endpoints)
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("endpoints") 

# COMMAND ----------

# MAGIC %md ##### Summary by creation_timestamp

# COMMAND ----------

# MAGIC %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Summary by endpoint_type

# COMMAND ----------

# MAGIC %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by endpoint_type desc

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
