# Databricks notebook source
# MAGIC %md ### Get Endpoint - `Model Serving` aka `MLflow Deployment` Endpoint
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Endpoint name` - endpoint name

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Endpoint name", "")
endpoint_name = dbutils.widgets.get("1. Endpoint name")
print("endpoint_name:", endpoint_name)

# COMMAND ----------

assert_widget(endpoint_name, "1. Endpoint name")

# COMMAND ----------

from mlflow_reports.endpoints import get_endpoint_client
client = get_endpoint_client()
client

# COMMAND ----------

endpoint = client.get_endpoint(endpoint_name)
dump_as_json(endpoint)
