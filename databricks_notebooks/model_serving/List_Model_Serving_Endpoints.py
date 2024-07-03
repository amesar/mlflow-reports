# Databricks notebook source
# MAGIC %md ## List and Query Model Serving Endpoints
# MAGIC
# MAGIC List and query "model serving endpoints" aka MLflow "deployment endpoints".
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Show JSON` - Show JSON API response.
# MAGIC * `2. Save JSON as file` - Save JSON as a file.
# MAGIC
# MAGIC ##### REST API Documetation
# MAGIC * [GET api/2.0/serving-endpoints](https://docs.databricks.com/api/workspace/servingendpoints/list) 
# MAGIC
# MAGIC ##### Github
# MAGIC * https://github.com/amesar/mlflow-reports/tree/master/mlflow_reports/model_serving

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

# MAGIC %md #### Get JSON response from API call

# COMMAND ----------

from mlflow_reports.model_serving import get_endpoints
endpoints = get_endpoints()
len(endpoints)

# COMMAND ----------

if output_file or show_json:
    dump_as_json(endpoints, output_file, silent=not show_json)

# COMMAND ----------

# MAGIC %md #### Create endpoints dataframe

# COMMAND ----------

df = to_dataframe(endpoints)
df = move_column(df, "endpoint_type")
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("endpoints") 

# COMMAND ----------

# MAGIC %sql describe endpoints

# COMMAND ----------

# MAGIC %md ##### Show my endpoints

# COMMAND ----------

cmd = f"""
select name, creator, endpoint_type, creation_timestamp from endpoints 
where creator='{_user}'
order by creation_timestamp desc, name
"""
display(sql(cmd))

# COMMAND ----------

# MAGIC %md ##### Summary by creation_timestamp

# COMMAND ----------

# MAGIC %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by creation_timestamp desc, name

# COMMAND ----------

# MAGIC %md ##### Summary by endpoint_type

# COMMAND ----------

# MAGIC %sql select name, creator, endpoint_type, creation_timestamp from endpoints order by endpoint_type desc, name

# COMMAND ----------

# MAGIC %md ##### Group by creator

# COMMAND ----------

# MAGIC %sql select creator, count(*) as count from endpoints group by creator order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by endpoint_type

# COMMAND ----------

# MAGIC %sql select endpoint_type, count(*) as count from endpoints group by endpoint_type order by count desc

# COMMAND ----------

# MAGIC %md ##### Show custom models

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp from endpoints 
# MAGIC where endpoint_type is null
# MAGIC order by name

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp from endpoints 
# MAGIC where endpoint_type is null
# MAGIC order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Show foundation models

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp from endpoints 
# MAGIC where endpoint_type like 'FOUNDATION%'
# MAGIC order by name, creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Show external models

# COMMAND ----------

# MAGIC %sql select name, creator, creation_timestamp from endpoints 
# MAGIC where endpoint_type = 'EXTERNAL_MODEL'
# MAGIC order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md ##### Group external models by task

# COMMAND ----------

# MAGIC %sql select task, count(*) as count from endpoints group by task order by count desc
