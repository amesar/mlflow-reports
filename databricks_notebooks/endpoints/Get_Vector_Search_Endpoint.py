# Databricks notebook source
# MAGIC %md ### Get Vector Search endpoint details and its indexes
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `Endpoint name` - Vector Search endpoint name
# MAGIC * `Save JSON as file` - Save endpoint _and its indexes_ as JSON file

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

!pip install -U -q databricks-vectorsearch
dbutils.library.restartPython() 

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("1. Endpoint name", "andre_dbdemo")
dbutils.widgets.text("2. Save JSON as file", "")

endpoint_name = dbutils.widgets.get("1. Endpoint name")
output_file = dbutils.widgets.get("2. Save JSON as file")

print("endpoint_name:", endpoint_name)
print("output_file:", output_file)

# COMMAND ----------

assert_widget(endpoint_name, "1. Endpoint name")

# COMMAND ----------

# MAGIC %md #### Create Vector Search client

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient
client = VectorSearchClient(disable_notice=True) 

# COMMAND ----------

# MAGIC %md #### Get Vector Search endpoint

# COMMAND ----------

endpoint = client.get_endpoint(endpoint_name)
dump_as_json(endpoint)

# COMMAND ----------

# MAGIC %md #### Get endpoint indexes

# COMMAND ----------

indexes = client.list_indexes(endpoint_name)
indexes

# COMMAND ----------

indexes = client.list_indexes(endpoint_name)
indexes = indexes.get("vector_indexes", [])
len(indexes)

# COMMAND ----------

dump_as_json(indexes)

# COMMAND ----------

# MAGIC %md #### Write to file both endpoint and its indexes

# COMMAND ----------

if output_file:
    endpoint["indexes"] = indexes
    write_json(output_file, endpoint)

# COMMAND ----------

# MAGIC %md #### Exit if no indexes

# COMMAND ----------

if len(indexes) == 0:
    msg = f"No indexes for endpoint '{endpoint_name}'"
    print(msg)
    dbutils.notebook.exit(msg)

# COMMAND ----------

# MAGIC %md #### Query Vector Search indexes with SQL

# COMMAND ----------

df = to_dataframe(indexes)
df = df.drop("endpoint_name")
df = move_column(df, "creator", 1)
display(df)

# COMMAND ----------

df.createOrReplaceTempView("indexes") 

# COMMAND ----------

# MAGIC %sql select  * from indexes order by name
