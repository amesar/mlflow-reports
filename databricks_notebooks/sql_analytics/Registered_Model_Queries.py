# Databricks notebook source
# MAGIC %md ## Registered Model SQL Queries
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC * SQL queries for the registed models.
# MAGIC * To create the database, see the [Create_MLflow_Database]($Create_MLflow_Database) notebook.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Database` - full path name such as `andre_m.mlflow_uc` or `andre_m.mlflow_ws`.
# MAGIC * `Version` - version of table.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("Database", "andre_catalog.mlflow_uc")
database_name = dbutils.widgets.get("Database")
table_name = f"{database_name}.models"

dbutils.widgets.text("Version", "")
version = dbutils.widgets.get("Version")
if version: version = "@v"+version

print("database_name:", database_name)
print("table_name:", table_name)
print("version:", version)

# COMMAND ----------

# MAGIC %md ### Describe table and history

# COMMAND ----------

display(spark.sql(f"describe {table_name}"))

# COMMAND ----------

display(spark.sql(f"describe history {table_name}"))

# COMMAND ----------

display_table_uri(table_name)

# COMMAND ----------

# MAGIC %md ### Create view

# COMMAND ----------

cmd = f"CREATE OR REPLACE TEMPORARY VIEW models as select * from {table_name}{version}"
spark.sql(cmd)
cmd

# COMMAND ----------

# MAGIC %md ### Queries

# COMMAND ----------

# MAGIC %md #### Count

# COMMAND ----------

# MAGIC %sql select count(*) as num_models from models

# COMMAND ----------

# MAGIC %md #### Show number of models per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_models from models group by user_id order by num_models desc

# COMMAND ----------

# MAGIC %md #### Show versions by user

# COMMAND ----------

# MAGIC %sql select user_id, * from models order by user_id, name

# COMMAND ----------

# MAGIC %md #### Show models by latest creation_timestamp

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Show models by latest creation_timestamp

# COMMAND ----------

# MAGIC %sql select * from models order by creation_timestamp
