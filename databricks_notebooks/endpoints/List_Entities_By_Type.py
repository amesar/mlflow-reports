# Databricks notebook source
# MAGIC %md ## List all model serving entities (models) by type
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC * List and query the different types of model/entity types - custom, foundation, external etc.
# MAGIC * Entities are found at `endpoint["config"]["served_entities"]`
# MAGIC * Since entities are polymorphic, each entity type has its own fields as well as common ones.
# MAGIC * To create these entity views, we rely on [mlflow_reports/endpoints/list_entities_by_type.py](https://github.com/amesar/mlflow-reports/blob/master/mlflow_reports/endpoints/list_entities_by_type.py).
# MAGIC
# MAGIC ##### Github
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/mlflow_reports/endpoints

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.dropdown("1. Show JSON", "no", ["yes","no"])
dbutils.widgets.text("2. Save JSON as file", "")

show_json = dbutils.widgets.get("1. Show JSON") == "yes"
output_file = dbutils.widgets.get("2. Save JSON as file")

print("show_json:", show_json)
print("output_file:", output_file)

# COMMAND ----------

# MAGIC %md #### Get endpoints from API

# COMMAND ----------

from mlflow_reports.endpoints import get_endpoints
endpoints = get_endpoints()
len(endpoints)

# COMMAND ----------

if output_file or show_json:
    dump_as_json(endpoints, output_file, silent=not show_json)

# COMMAND ----------

# MAGIC %md #### Endpoint queries

# COMMAND ----------

ts_columns = [ "creation_timestamp", "last_updated_timestamp"]
df = to_dataframe(endpoints, ts_columns)
df.createOrReplaceTempView("endpoints") 
display(df)

# COMMAND ----------

# MAGIC %sql select endpoint_type, count(*) as count from endpoints group by endpoint_type order by count desc

# COMMAND ----------

# MAGIC %md #### Import endpoint type table builder functions

# COMMAND ----------

from mlflow_reports.endpoints.list_entities_by_type import (
    mk_custom_models, 
    mk_foundation_models, 
    mk_external_models, 
    mk_pending_models
)

# COMMAND ----------

# MAGIC %md #### Custom models
# MAGIC
# MAGIC ##### Sample JSON
# MAGIC ```
# MAGIC   "served_models": [
# MAGIC     {
# MAGIC       "name": "sklearn_wine_best-7",
# MAGIC       "model_name": "andre_catalog.ml_models2.sklearn_wine_best",
# MAGIC       "model_version": "7"
# MAGIC     }
# MAGIC   ],
# MAGIC   "served_entities": [
# MAGIC     {
# MAGIC       "name": "sklearn_wine_best-7",
# MAGIC       "entity_name": "andre_catalog.ml_models2.sklearn_wine_best",
# MAGIC       "entity_version": "7"
# MAGIC     }
# MAGIC   ]
# MAGIC ````

# COMMAND ----------

models = mk_custom_models(endpoints)
ts_columns = [ "ep_creation_timestamp", "ep_last_updated_timestamp"]
df = to_dataframe(models, ts_columns)
df = df.drop("ep_state").drop("ep_last_updated_timestamp")
df.createOrReplaceTempView("custom_models") 
display(df)

# COMMAND ----------

# MAGIC %sql select ep_name as endpoint, model_name, model_version from custom_models order by ep_name desc

# COMMAND ----------

# MAGIC %md #### Foundation models
# MAGIC
# MAGIC * Note there is no `creator` attribute in the entity.
# MAGIC
# MAGIC Sample JSON:
# MAGIC ```
# MAGIC       "served_entities": [
# MAGIC         {
# MAGIC           "name": "databricks-llama-2-70b-chat",
# MAGIC           "type": "FOUNDATION_MODEL",
# MAGIC           "foundation_model": {
# MAGIC             "name": "llama-2-70b-chat",
# MAGIC             "display_name": "Llama 2 70B Chat",
# MAGIC             "docs": "https://docs.databricks.com/machine-learning/foundation-models/supported-models.html#llama2-70b",
# MAGIC             "description": "A state-of-the-art 70B parameter language model with a context length of 4096 tokens, trained by Meta. The model was pretrained on 2T tokens of text and fine-tuned for dialog use cases leveraging over 1 million human annotations. Llama 2 is licensed under the LLAMA 2 Community License, Copyright \u00a9 Meta Platforms, Inc. All Rights Reserved. Customers are responsible for ensuring compliance with applicable model licenses.",
# MAGIC             "price": "28.571"
# MAGIC           } 
# MAGIC         }
# MAGIC ```

# COMMAND ----------

models = mk_foundation_models(endpoints)
df = to_dataframe(models, ts_columns)
df = df.drop("ep_state").drop("ep_last_updated_timestamp")
df.createOrReplaceTempView("foundation_models") 
display(df)

# COMMAND ----------

# MAGIC %sql select ep_name, fm_name, fm_price from foundation_models order by fm_price desc

# COMMAND ----------

# MAGIC %md #### External models
# MAGIC
# MAGIC ##### Sample JSON
# MAGIC ```
# MAGIC   "served_entities": [
# MAGIC     {   
# MAGIC       "name": "gpt-35-turbo",
# MAGIC       "type": "EXTERNAL_MODEL",
# MAGIC       "external_model": {
# MAGIC         "provider": "openai",
# MAGIC         "name": "gpt-35-turbo",
# MAGIC         "task": "llm/v1/chat",
# MAGIC         "openai_config": {
# MAGIC           "openai_api_key": "{{secrets/dbdemos/azure-openai}}",
# MAGIC           "openai_api_type": "azure",
# MAGIC           "openai_api_base": "https://dbdemos-open-ai.openai.azure.com/",
# MAGIC           "openai_api_version": "2023-05-15",
# MAGIC           "openai_deployment_name": "dbdemo-gpt35"
# MAGIC         }   
# MAGIC       }  
# MAGIC ```

# COMMAND ----------

models = mk_external_models(endpoints)
df = to_dataframe(models, ts_columns)
df = df.drop("ep_state").drop("ep_last_updated_timestamp")
display(df)

# COMMAND ----------

# MAGIC %md #### Pending endpoints
# MAGIC
# MAGIC ##### Sample JSON
# MAGIC ```
# MAGIC   "pending_config": {
# MAGIC     "start_time": 1704673381000,
# MAGIC     "served_models": [
# MAGIC       {
# MAGIC         "name": "airline_sql_agent-4",
# MAGIC         "model_name": "cindy_demo_catalog.airline_bookings.airline_sql_agent",
# MAGIC         "model_version": "4",
# MAGIC         "workload_size": "Small",
# MAGIC         "scale_to_zero_enabled": true,
# MAGIC         "workload_type": "CPU",
# MAGIC         "state": {
# MAGIC           "deployment": "DEPLOYMENT_ABORTED",
# MAGIC           "deployment_state_message": "Served model creation aborted because the endpoint update timed out. Please see service logs for more information."
# MAGIC         },
# MAGIC         "creator": "k2.denali@databricks.com",
# MAGIC         "creation_timestamp": 1704673381000
# MAGIC       }
# MAGIC     ],
# MAGIC   "served_entities": [
# MAGIC     {
# MAGIC       "name": "airline_sql_agent-4",
# MAGIC       "entity_name": "cindy_demo_catalog.airline_bookings.airline_sql_agent",
# MAGIC       "entity_version": "4",
# MAGIC       "workload_size": "Small",
# MAGIC       "scale_to_zero_enabled": true,
# MAGIC       "workload_type": "CPU",
# MAGIC       "state": {
# MAGIC         "deployment": "DEPLOYMENT_ABORTED",
# MAGIC         "deployment_state_message": "Served model creation aborted because the endpoint update timed out. Please see service logs for more information."
# MAGIC       },
# MAGIC       "creator": "k2.denali@databricks.com",
# MAGIC       "creation_timestamp": 1704673381000
# MAGIC     }
# MAGIC   ]
# MAGIC ```

# COMMAND ----------

models = mk_pending_models(endpoints)
df = to_dataframe(models, ts_columns)
display(df)
