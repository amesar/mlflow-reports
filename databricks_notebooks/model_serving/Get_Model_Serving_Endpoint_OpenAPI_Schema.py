# Databricks notebook source
# MAGIC %md ### Get Model Serving Endpoint OpenAPI Schema
# MAGIC
# MAGIC ##### Overview
# MAGIC * Get the OpenAPI schema of a model serving endpoint.
# MAGIC * [GET api/2.0/serving-endpoints/{name}/openapi](https://docs.databricks.com/api/workspace/servingendpoints/getopenapi)
# MAGIC
# MAGIC ##### API JSON response example
# MAGIC
# MAGIC ```
# MAGIC {
# MAGIC   "openapi": "3.1.0",
# MAGIC   "info": {
# MAGIC     "title": "aia-oai-text-embedding",
# MAGIC     "version": "1"
# MAGIC   },
# MAGIC   "servers": [
# MAGIC     {
# MAGIC       "url": "https://e2-demo-field-eng.cloud.databricks.com/serving-endpoints/aia-oai-text-embedding"
# MAGIC     }
# MAGIC   ],
# MAGIC   "paths": {
# MAGIC     "/served-models/text-embedding-ada-002/invocations": {
# MAGIC       "post": {
# MAGIC         "requestBody": {
# MAGIC           "content": {
# MAGIC             "application/json": {
# MAGIC               "schema": {
# MAGIC                 "type": "object",
# MAGIC                 "properties": {
# MAGIC                   "input": {
# MAGIC                     "oneOf": [
# MAGIC                       {
# MAGIC                         "type": "string"
# MAGIC                       },
# MAGIC                       {
# MAGIC                         "type": "array",
# MAGIC                         "items": {
# MAGIC                           "type": "string"
# MAGIC                         }
# MAGIC                       }
# MAGIC                     ]
# MAGIC                   }
# MAGIC                 }
# MAGIC               }
# MAGIC             }
# MAGIC           }
# MAGIC         },
# MAGIC         "responses": {
# MAGIC }
# MAGIC ```

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

# MAGIC %md #### Get OpenAPI schema

# COMMAND ----------

from mlflow_reports.model_serving import get_endpoint_client
client = get_endpoint_client()
rsp = client.get_endpoint_openapi_schema(endpoint_name)
dump_as_json(rsp)
