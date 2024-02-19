# Databricks notebook source
# MAGIC %md ## Model Version SQL Queries
# MAGIC
# MAGIC ##### Overview
# MAGIC
# MAGIC * SQL queries for the model versions.
# MAGIC * To create the database, see the [Create_MLflow_Database]($Create_MLflow_Database) notebook.
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Database` - full path name such as `andre_m.mlflow_uc` or `andre_m.mlflow_ws`.

# COMMAND ----------

# MAGIC %md ### Setup

# COMMAND ----------

dbutils.widgets.text("Database", "andre_catalog.mlflow_uc")
database_name = dbutils.widgets.get("Database")
print("database_name:", database_name)

# COMMAND ----------

spark.sql(f"use {database_name}")

# COMMAND ----------

# MAGIC %md ### Describe table and history

# COMMAND ----------

# MAGIC %sql describe versions

# COMMAND ----------

# MAGIC %sql describe history versions

# COMMAND ----------

# MAGIC %md ### Queries

# COMMAND ----------

# MAGIC %md #### Count

# COMMAND ----------

# MAGIC %sql select count(*) as num_versions from versions

# COMMAND ----------

# MAGIC %md #### Show number of versions per user

# COMMAND ----------

# MAGIC %sql select user_id, count(*) as num_versions from versions group by user_id order by num_versions desc

# COMMAND ----------

# MAGIC %md #### Show versions by user

# COMMAND ----------

# MAGIC %sql select user_id, * from versions order by user_id, name

# COMMAND ----------

# MAGIC %md #### Show versions by latest creation_timestamp

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp desc

# COMMAND ----------

# MAGIC %md #### Show versions by earliest creation_timestamp

# COMMAND ----------

# MAGIC %sql select * from versions order by creation_timestamp
