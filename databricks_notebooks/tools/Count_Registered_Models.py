# Databricks notebook source
# MAGIC %md ### Count Registered Models
# MAGIC
# MAGIC Count the number of registered models.
# MAGIC
# MAGIC ##### Widgets
# MAGIC
# MAGIC * `1. Unity Catalog` - Use Unity Catalog or Workspace model registry.
# MAGIC * `2. Filter` - `filter_string` argument for for search_registered_models().
# MAGIC * `3. Max results` argument for for search_registered_models().
# MAGIC
# MAGIC ##### Documentation
# MAGIC
# MAGIC * [MlflowClient.search_registered_models](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models)

# COMMAND ----------

dbutils.widgets.dropdown("1. Unity Catalog", "yes", ["yes","no"])
unity_catalog = dbutils.widgets.get("1. Unity Catalog") == "yes"
registry_uri = "databricks-uc" if unity_catalog else "databricks"

dbutils.widgets.text("2. Filter", "")
filter = dbutils.widgets.get("2. Filter")
filter = filter or None

dbutils.widgets.text("3. Max results", "")
max_results = dbutils.widgets.get("3. Max results")
max_results = int(max_results) if max_results else None

print("unity_catalog:", unity_catalog)
print("registry_uri:", registry_uri)
print("filter:", filter)
print("max_results:", max_results)

# COMMAND ----------

import mlflow
mlflow.set_registry_uri(registry_uri)
client = mlflow.tracking.MlflowClient()
client._registry_uri

# COMMAND ----------

def count_registered_models(filter, max_results=None):
    count = 0
    num_iterations = 0
    kwargs = {}
    while True:
        num_iterations += 1
        models = client.search_registered_models(filter_string=filter, max_results=max_results, **kwargs)
        count += len(models)
        if not models.token:
            break
        kwargs = {"page_token": models.token}
    #print("num_iterations:", num_iterations)
    return count

# COMMAND ----------

count_registered_models(filter, max_results)
