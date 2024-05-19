# Databricks notebook source
# MAGIC %md ### Get Model Serving Endpoint Signature
# MAGIC
# MAGIC Get the model signature of a model serving endpoint "entity" (custom models only).
# MAGIC
# MAGIC ##### Widgets
# MAGIC * `1. Endpoint` 
# MAGIC * `2. Entity (model)` == `config.served_entities[0].name`. One of the served entities (model), usually there is just one.
# MAGIC
# MAGIC ##### Endpoint JSON response example
# MAGIC
# MAGIC ```
# MAGIC { 
# MAGIC   "name": "dbdemos_endpoint_advanced_andre_catalog_rag_chatbot_2024_03_04",
# MAGIC   . . .
# MAGIC   "config": {
# MAGIC     "served_entities": [
# MAGIC       {
# MAGIC         "name": "dbdemos_advanced_chatbot_model-1",
# MAGIC         "entity_name": "andre_catalog.rag_chatbot.dbdemos_advanced_chatbot_model",
# MAGIC         "entity_version": "1",
# MAGIC         "workload_size": "Small",
# MAGIC         "scale_to_zero_enabled": true,
# MAGIC         "workload_type": "CPU",
# MAGIC         "environment_vars": {
# MAGIC           "DATABRICKS_TOKEN": "{{secrets/dbdemos/rag_sp_token}}"
# MAGIC         },
# MAGIC         "state": {
# MAGIC           "deployment": "DEPLOYMENT_READY",
# MAGIC           "deployment_state_message": ""
# MAGIC         },
# MAGIC         "creator": "k1.denali@databricks.com",
# MAGIC         "creation_timestamp": 1709591231000,
# MAGIC         "_creation_timestamp": "2024-03-04 22:27:11"
# MAGIC       }
# MAGIC     ],
# MAGIC   . . .
# MAGIC   }
# MAGIC }
# MAGIC   ```
# MAGIC
# MAGIC ##### Documentation
# MAGIC * Databricks
# MAGIC   * [GET api/2.0/serving-endpoints/{name}](https://docs.databricks.com/api/workspace/servingendpoints/get) - REST API

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("1. Endpoint", "dbdemos_endpoint_advanced_andre_catalog_rag_chatbot_2024_03_04")
dbutils.widgets.text("2. Entity (model)", "dbdemos_advanced_chatbot_model-1")

endpoint_name = dbutils.widgets.get("1. Endpoint")
entity_name = dbutils.widgets.get("2. Entity (model)")

print("endpoint_name:    ", endpoint_name)
print("entity_name:", entity_name)

# COMMAND ----------

assert_widget(endpoint_name, "1. Endpoint name")
assert_widget(entity_name, "2. Entity (model)")

# COMMAND ----------

# MAGIC %md #### Get endpoint

# COMMAND ----------

from mlflow.deployments import get_deploy_client
deploy_client = get_deploy_client("databricks")
rsp = deploy_client.get_endpoint(endpoint_name)
dump_as_json(rsp)

# COMMAND ----------

# MAGIC %md #### Helper functions

# COMMAND ----------

import yaml
from mlflow.artifacts import download_artifacts
from mlflow.utils.file_utils import TempDir

def get_MLmodel(model_name, model_version):
    model_uri = f"models:/{model_name}/{model_version}"
    with TempDir() as tmp:
        artifact_uri = f"{model_uri}/MLmodel"
        local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=tmp.path())
        with open(local_path, "r") as f:
            return yaml.safe_load(f)

# COMMAND ----------

def get_signature(endpoint_name, entity_name):
    def find(entities, entity_name):
        matches = [ x for x in entities if x["name"] == entity_name ]
        return matches[0] if matches else None

    endpoint = deploy_client.get_endpoint(endpoint_name)
    config = endpoint.get("config", {})
    entities = config.get("served_entities", [])

    entity = find(entities, entity_name)
    if not entity:
        print(f"WARNING: no entity '{entity_name}'")
        return {}

    model_name = entity.get("entity_name")
    model_version = entity.get("entity_version")
    print("model_name:", model_name)
    print("model_version:", model_version)
    if not model_version:
        print(f"WARNING: no model_version - is not a 'custom model'")
        return {}
    
    if "." in model_name:
        mlflow.set_registry_uri("databricks-uc")
    else:
        mlflow.set_registry_uri("databricks")
        
    mlmodel = get_MLmodel(model_name, model_version)
    return mlmodel.get("signature")

# COMMAND ----------

# MAGIC %md #### Get signature
# MAGIC
# MAGIC The signature `inputs` and `outputs` fields are a JSON string and not a JSON dictionary.

# COMMAND ----------

signature = get_signature(endpoint_name, entity_name)

# COMMAND ----------

dump_as_json(signature)

# COMMAND ----------

# MAGIC %md #### Convert response to human readable JSON

# COMMAND ----------

def normalize(signature):
    def _normalize(lst):
        import json
        return json.loads(lst) if lst else lst
    return { k:_normalize(v) for k,v in signature.items()}
    
happy_signature = normalize(signature)
dump_as_json(happy_signature)
