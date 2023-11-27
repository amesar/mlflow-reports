# Databricks notebook source
# MAGIC %md ## List and Query AI Gateway Routes
# MAGIC
# MAGIC * https://mlflow.org/docs/latest/python_api/mlflow.gateway.html

# COMMAND ----------

# MAGIC %md #### Create routes dataframe

# COMMAND ----------

import pandas as pd
import mlflow
import mlflow.gateway
mlflow.__version__, mlflow.gateway.get_gateway_uri() 

# COMMAND ----------

def create_pandas_df():
    routes = mlflow.gateway.search_routes()
    data = [ (rt.name, rt.route_type, rt.model.name, rt.model.provider) for rt in routes ]
    return pd.DataFrame(data, columns = ["name","route_type", "model_name", "model_provider"])

# COMMAND ----------

df = spark.createDataFrame(create_pandas_df())
print("Routes:", df.count())

# COMMAND ----------

# MAGIC %md #### SQL queries

# COMMAND ----------

df.createOrReplaceTempView("routes") 

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
