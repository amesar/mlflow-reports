# Databricks notebook source
# MAGIC %md ### Get Model Signature 
# MAGIC
# MAGIC Get the signature of an MLflow model. 
# MAGIC
# MAGIC MLflow models can live in a variety of places. Sample MLflow model URIs:
# MAGIC * `models:/andre_catalog.ml_models2.sklearn_wine_best/13`
# MAGIC * `models:/Sklearn_Wine_best/1`
# MAGIC * `runs:/030075d9727945259c7d283e47fee4a9/model`
# MAGIC * `/Volumes/andre_catalog/volumes/mlflow_export_import/single/sklearn_wine_best/run/artifacts/model`
# MAGIC * `/dbfs/home/first.last@databricks.com/mlflow_export_import/single/sklearn_wine_best/model`
# MAGIC * `s3:/my-bucket/mlflow-models/sklearn-wine_best`
# MAGIC
# MAGIC The signature can be found in the MLmodel artifact of the MLflow model.
# MAGIC * For a run, you can view the signature in the "Artifacts" tab of the run UI page.
# MAGIC * For a model version, you can only view (in the UI) the signature via the run.
# MAGIC   * To get the actual signature of the deployed model, you need to use the API method `mlflow.models.get_model_info()`.
# MAGIC
# MAGIC Documentation:
# MAGIC * [mlflow.models.ModelSignature](https://mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.ModelSignature)
# MAGIC * [mlflow.models.get_model_info](https://mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.get_model_info)

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../_Common

# COMMAND ----------

dbutils.widgets.text("Model URI", "")
model_uri = dbutils.widgets.get("Model URI")
print("model_uri:", model_uri)

# COMMAND ----------

assert_widget(model_uri, "Model URI")
activate_unity_catalog(model_uri)

# COMMAND ----------

# MAGIC %md #### Get `model_info.signature`

# COMMAND ----------

model_info = mlflow.models.get_model_info(model_uri)
model_info.signature

# COMMAND ----------

dump_as_json(model_info.signature.to_dict())

# COMMAND ----------

# MAGIC %md #### Convert signature to more readable JSON

# COMMAND ----------

def normalize(signature):
    def _normalize(lst):
        import json
        return json.loads(lst) if lst else lst
    return { k:_normalize(v) for k,v in signature.items()}
    
signature = normalize(model_info.signature.to_dict())
dump_as_json(signature)
