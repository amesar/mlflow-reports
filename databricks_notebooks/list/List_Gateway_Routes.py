# Databricks notebook source
# MAGIC %md ## List and Query AI Gateway Routes
# MAGIC * AI Gateway is deprecated. See [MLflow AI Gateway Migration Guide
# MAGIC ](https://mlflow.org/docs/latest/llms/gateway/migration.html#gateway-migration)
# MAGIC * Use the [List_Model_Serving_Endpoints]($List_Model_Serving_Endpoints) notebook
# MAGIC * Docs: [mlflow.gateway](https://mlflow.org/docs/latest/python_api/mlflow.gateway.html)

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %pip install mlflow[skinny]
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd
import mlflow
mlflow.__version__,  mlflow.gateway.get_gateway_uri() 

# COMMAND ----------

# MAGIC %md #### Create routes dataframe

# COMMAND ----------

routes = mlflow.gateway.search_routes()
len(routes)

# COMMAND ----------

data = [ (rt.name, rt.route_type, rt.model.name, rt.model.provider) for rt in routes ]
df = spark.createDataFrame(data, ["name","route_type", "model_name", "model_provider"])
display(df)

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("routes") 
df.count()

# COMMAND ----------

# MAGIC %md ##### Group by route_type

# COMMAND ----------

# MAGIC %sql select route_type, count(*) as count from routes group by route_type order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by model_name

# COMMAND ----------

# MAGIC %sql select model_name, count(*) as count from routes group by model_name order by count desc

# COMMAND ----------

# MAGIC %md ##### Group by model_provider

# COMMAND ----------

# MAGIC %sql select model_provider, count(*) as count from routes group by model_provider order by count desc

# COMMAND ----------

# MAGIC %md ##### Select by route_type

# COMMAND ----------

# MAGIC %sql select * from routes order by route_type
