# Databricks notebook source
# MAGIC %md ### Get Model Serving Endpoint
# MAGIC
# MAGIC Also called "MLflow Deployment" endpoint.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Endpoint name` - endpoint name
# MAGIC * `2. Save JSON as file` - Save endpoint as JSON file
# MAGIC
# MAGIC ##### Documentation
# MAGIC * Databricks
# MAGIC   * [GET api/2.0/serving-endpoints/{name}](https://docs.databricks.com/api/workspace/servingendpoints/get) - REST API
# MAGIC * MLflow
# MAGIC   * [GET api/2.0/serving-endpoints/{name}](https://mlflow.org/docs/latest/llms/deployments/api.html#/default/get_endpoint_api_2_0_endpoints__endpoint_name__get) - REST API

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Endpoint name", "")
dbutils.widgets.text("2. Save JSON as file", "")

endpoint_name = dbutils.widgets.get("1. Endpoint name")
output_file = dbutils.widgets.get("2. Save JSON as file")

print("endpoint_name:", endpoint_name)
print("output_file:", output_file)

# COMMAND ----------

assert_widget(endpoint_name, "1. Endpoint name")

# COMMAND ----------

from mlflow_reports.model_serving import get_endpoint_client
client = get_endpoint_client()
client

# COMMAND ----------

endpoint = client.get_endpoint(endpoint_name)
dump_as_json(endpoint)

# COMMAND ----------

if output_file:
    write_json(output_file, endpoint)
