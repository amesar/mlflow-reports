# Databricks notebook source
# MAGIC %md ## List and Query Model Serving Endpoint Entities
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC * List and query model serving endpoint entities.
# MAGIC * Entities can be found at endpoint["config"]["served_entities"]
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
endpoints = get_endpoints(call_databricks_model_serving)
len(endpoints)

# COMMAND ----------

# MAGIC %md #### List entities

# COMMAND ----------

from mlflow_reports.endpoints.list_endpoint_entities import list_entities
entities = list_entities(endpoints)

df = to_dataframe(entities, ["ep_creation_timestamp", "ep_last_updated_timestamp"])
df = move_column(df, "ep_endpoint_type")
display(df)

# COMMAND ----------

# MAGIC %md #### List endpoints without entities - in READY state

# COMMAND ----------

from mlflow_reports.endpoints.list_endpoint_entities import list_endpoints_without_entities
endpoints_without_entities = list_endpoints_without_entities(endpoints)
display(to_dataframe(endpoints_without_entities, []))

# COMMAND ----------

# MAGIC %md #### Enpoint type and entity type queries
# MAGIC
# MAGIC * Note that the endpoint type is `FOUNDATION_MODEL_API` wheras the entity type is `FOUNDATION_MODEL`.

# COMMAND ----------

df.createOrReplaceTempView("entities") 

# COMMAND ----------

# MAGIC %md ##### Summary by endpoint_type

# COMMAND ----------

# MAGIC %sql select * from entities order by ep_endpoint_type desc

# COMMAND ----------

# MAGIC %md ##### Group by endpoint_type

# COMMAND ----------

# MAGIC %sql select ep_endpoint_type, count(*) as count from entities group by ep_endpoint_type order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by entity type

# COMMAND ----------

# MAGIC %sql select type, count(*) as count from entities group by type order by count desc

# COMMAND ----------

# MAGIC %md #### Timestamp query

# COMMAND ----------

# MAGIC %sql select * from entities order by ep_creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Creator queries

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select ep_creator, count(*) as count from entities group by ep_creator order by count desc

# COMMAND ----------

# MAGIC %sql select * from entities order by ep_creator

# COMMAND ----------

# MAGIC %md #### Show entities of different endpoint types

# COMMAND ----------

# MAGIC %md ##### Show custom models

# COMMAND ----------

# MAGIC %sql select * from entities 
# MAGIC where type is null
# MAGIC order by ep_creation_timestamp desc

# COMMAND ----------

# MAGIC %sql select ep_creator, entity_name, entity_version from entities 
# MAGIC where entity_name is not null and entity_version is not null
# MAGIC order by ep_creator

# COMMAND ----------

# MAGIC %md ##### Show foundation models

# COMMAND ----------

# MAGIC %sql select * from entities 
# MAGIC where type = 'FOUNDATION_MODEL'
# MAGIC order by ep_creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Show external models

# COMMAND ----------

# MAGIC %sql select * from entities 
# MAGIC where type = 'EXTERNAL_MODEL'
# MAGIC order by ep_creation_timestamp desc
