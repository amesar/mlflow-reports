# Databricks notebook source
# MAGIC %md ### Get Model Serving Endpoint OpenAI Schema
# MAGIC
# MAGIC Get the model signature of a model serving endpoint "entity" (custom models only).
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Endpoint` 
# MAGIC * `2. Entity (model)` == `config.served_entities[0].name`. One of the served entities (model), usually there is just one.
# MAGIC
# MAGIC ##### Endpoint JSON response example
# MAGIC
# MAGIC ```
# MAGIC { 
# MAGIC
# MAGIC }
# MAGIC   ```
# MAGIC
# MAGIC ##### REST API Documentation
# MAGIC * [GET api/2.0/serving-endpoints/{name}/openapi](https://docs.databricks.com/api/workspace/servingendpoints/getopenapi)

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("Endpoint", "sklearn_wine_best")
endpoint_name = dbutils.widgets.get("Endpoint")
print("endpoint_name:    ", endpoint_name)

# COMMAND ----------

assert_widget(endpoint_name, "Endpoint name")

# COMMAND ----------

# MAGIC %md #### Get endpoint's OpenAPI schema

# COMMAND ----------

from mlflow_reports.model_serving import get_endpoint_client
client = get_endpoint_client()
rsp = client.get_endpoint(endpoint_name)
dump_as_json(rsp)

# COMMAND ----------

rsp = client.get_endpoint_openapi_schema(endpoint_name)
dump_as_json(rsp)
