# Databricks notebook source
# MAGIC %md ## Get Feature Table
# MAGIC
# MAGIC Overview:
# MAGIC * Get feature table details and lineage information.
# MAGIC * Inconsistent and incomplete results across 4 different ways of fetching details.
# MAGIC
# MAGIC Get feature table details from clients
# MAGIC   * [FeatureEngineeringClient](https://api-docs.databricks.com/python/feature-engineering/latest/feature_engineering.client.html)
# MAGIC   * [FeatureStoreClient](https://api-docs.databricks.com/python/feature-engineering/latest/feature_engineering.client.html)
# MAGIC
# MAGIC Get feature table details from undocumented REST API endpoints
# MAGIC   * REST API `api/2.0/feature-store/feature-tables/get`
# MAGIC     * Note: not documented in [Databricks REST API reference](https://docs.databricks.com/api/workspace/introduction)
# MAGIC   * REST API `api/2.0/feature-store/feature-tables/search`
# MAGIC     * Note: UC table does not appear in search results but WS tables does.
# MAGIC
# MAGIC Get Unity Catalog table details
# MAGIC   * [api/2.1/unity-catalog/tables/{table_name}](https://docs.databricks.com/api/workspace/tables/get)
# MAGIC
# MAGIC Get Unity Catalog table lineage details
# MAGIC   * REST API `api/2.0/lineage-tracking/table-lineage`
# MAGIC   * [Data Lineage API](https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html) - example in Databricks documentation
# MAGIC   * Note: not documented in [Databricks REST API reference](https://docs.databricks.com/api/workspace/introduction)
# MAGIC
# MAGIC ##### Sample tables
# MAGIC   * andre_catalog.fs_wine_uc.wine_features - Created by FE client
# MAGIC   * andre_catalog.fs_wine_uc.wine_tmp - Created with PK and without FE client
# MAGIC   * andre_catalog.fs_wine.wine_features_ws - Created by FS client
# MAGIC   * hive_metastore.andre_fs_wine.wine_features - Created by FS client
# MAGIC     * andre_fs_wine.wine_features - Created by FS client

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("Feature table", "andre_catalog.fs_wine_uc.wine_features")
table_name = dbutils.widgets.get("Feature table")
print(f"table_name:", table_name)

# COMMAND ----------

import requests

base_uri = f"https://{_host_name}/api"
base_uri

# COMMAND ----------

# MAGIC %md #### REST API `api/2.0/feature-store/feature-tables/get`
# MAGIC * Note: not documented in [Databricks REST API reference](https://docs.databricks.com/api/workspace/introduction)

# COMMAND ----------

uri = f"{base_uri}/2.0/feature-store/feature-tables/get"
uri

# COMMAND ----------

rsp = requests.get(uri, headers=_auth_headers, json={"name": table_name})
dump_as_json(rsp.json())

# COMMAND ----------

# MAGIC %md #### REST API `api/2.0/feature-store/feature-tables/search`
# MAGIC * Note: returns WS tables but not UC tables

# COMMAND ----------

from mlflow_reports.feature_store import get_feature_tables
tables = get_feature_tables.list()
print(f"Found {len(tables)} feature tables")

# COMMAND ----------

for tbl in tables:
    print(tbl["name"])

# COMMAND ----------

matches = [ tbl for tbl in tables if tbl.get("name") == table_name ]
if len(matches) > 0:
    dump_as_json(matches[0])

# COMMAND ----------

# MAGIC %md #### FeatureEngineeringClient
# MAGIC * Note: does not restore lineage info such as online_stores, notebook_producers, etc.

# COMMAND ----------

from databricks.feature_engineering.client import FeatureEngineeringClient
fe_client = FeatureEngineeringClient(model_registry_uri="databricks")
fe_client

# COMMAND ----------

try:
    table = fe_client.get_table(name=table_name)
    table
except Exception as e:
    print(f"{type(e).__name__}: {e}")
    table = None

# COMMAND ----------

if table:
    dump_as_json(table.__dict__)

# COMMAND ----------

# MAGIC %md #### FeatureStoreClient
# MAGIC * Note: 
# MAGIC     * For UC table, does not return lineage info such as online_stores, notebook_producers, etc.
# MAGIC     * For WS tables does return them.

# COMMAND ----------

from databricks.feature_store import FeatureStoreClient
fs_client = FeatureStoreClient()
fs_client

# COMMAND ----------

table = fs_client.get_table(table_name)
table

# COMMAND ----------

try:
    dump_as_json(table.__dict__)
except Exception as e: # TypeError: Object of type Notebook is not JSON serializable
    dump_obj(table)
    print(f"\nERROR: {type(e).__name__}: {e}")

# COMMAND ----------

# MAGIC %md #### REST API `api/2.1/unity-catalog/tables/{table_name}`
# MAGIC * Note: does restore lineage info such as online_stores, notebook_producers, etc.

# COMMAND ----------

uri = f"{base_uri}/2.1/unity-catalog/tables/{table_name}"
uri

# COMMAND ----------

rsp = requests.get(uri, headers=_auth_headers)
dump_as_json(rsp.json())

# COMMAND ----------

# MAGIC %md #### REST API `2.0/lineage-tracking/table-lineage`
# MAGIC
# MAGIC * [Data Lineage API](https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html)
# MAGIC   * [api/2.0/lineage-tracking/table-lineage](https://docs.databricks.com/en/data-governance/unity-catalog/data-lineage.html#retrieve-table-lineage)

# COMMAND ----------

uri = f"{base_uri}/2.0/lineage-tracking/table-lineage"
uri

# COMMAND ----------

params = {
    "table_name": table_name,
     "include_entity_lineage": "true"
}
rsp = requests.get(uri, headers=_auth_headers, json=params)
dump_as_json(rsp.json())
