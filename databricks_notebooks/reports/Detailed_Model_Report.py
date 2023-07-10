# Databricks notebook source
# MAGIC %md ## Detailed MLflow Model Report
# MAGIC
# MAGIC **Overview**
# MAGIC * Generates a markdown file for a detailed report of an MLflow model.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model URI` - model URI such as `models:/my-model/1` or `runs:/18121205149219141865/model`
# MAGIC * `Get permissions` - dump run data if showing runs
# MAGIC * `Output file` - output markdown file such as `model.md`
# MAGIC * `Output data file` - output JSON file (e.g. `model.json`) of API data used to build the report
# MAGIC * `Unity Catalog` - use Unity Catalog
# MAGIC
# MAGIC **Sample files**
# MAGIC
# MAGIC Non-UC samples:
# MAGIC * [report.md](https://github.com/amesar/mlflow-reports/blob/master/samples/databricks/model_reports/credit_adjudication/report.md) - Markdown model report
# MAGIC * [report.json](https://github.com/amesar/mlflow-reports/blob/master/samples/databricks/model_reports/credit_adjudication/report.json) - MLflow API data used to generate the report
# MAGIC
# MAGIC UC samples:
# MAGIC * [report.md](https://github.com/amesar/mlflow-reports/blob/master/samples/databricks/model_reports/credit_adjudication/uc_report.md) 
# MAGIC * [report.json](https://github.com/amesar/mlflow-reports/blob/master/samples/databricks/model_reports/credit_adjudication/uc_report.json) 

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ../Common

# COMMAND ----------

dbutils.widgets.text("1. Model URI", "")
dbutils.widgets.dropdown("2. Get permissions", "yes", ["yes","no"])
dbutils.widgets.text("3. Output file", "")
dbutils.widgets.text("4. Output data file", "model.md")
dbutils.widgets.dropdown("5. Unity Catalog", "no", ["yes","no"])

model_uri = dbutils.widgets.get("1. Model URI")
get_permissions = dbutils.widgets.get("2. Get permissions") == "yes"
output_file = dbutils.widgets.get("3. Output file")
output_data_file = dbutils.widgets.get("4. Output data file")
use_uc = dbutils.widgets.get("5. Unity Catalog") == "yes"

import os
os.environ["OUTPUT_FILE"] = output_file
os.environ["OUTPUT_DATA_FILE"] = output_data_file

print("model_uri:", model_uri)
print("get_permissions:", get_permissions)
print("output_file:", output_file)
print("output_data_file:", output_data_file)
print("use_uc:", use_uc)

# COMMAND ----------

assert_widget(model_uri, "1. Model URI")
assert_widget(output_file, "2. Output file")

activate_unity_catalog(use_uc)

# COMMAND ----------

# MAGIC %md #### Build markdown report

# COMMAND ----------

from mlflow_reports.markdown import detailed_report

data = detailed_report.build_report(
    model_uri = model_uri, 
    get_permissions = get_permissions, 
    output_file = output_file
)
dump_as_json(data, output_data_file)

# COMMAND ----------

# MAGIC %md #### Check markdown output file

# COMMAND ----------

# MAGIC %sh echo $OUTPUT_FILE
# MAGIC ls -l $OUTPUT_FILE 

# COMMAND ----------

# MAGIC %sh head -n 60 $OUTPUT_FILE 

# COMMAND ----------

# MAGIC %md #### Check JSON data file

# COMMAND ----------

# MAGIC %sh 
# MAGIC if test -f "$OUTPUT_DATA_FILE"; then
# MAGIC   echo $OUTPUT_DATA_FILE
# MAGIC   ls -l $OUTPUT_DATA_FILE 
# MAGIC else
# MAGIC   echo "No OUTPUT_DATA_FILE"
# MAGIC fi

# COMMAND ----------

# MAGIC %sh
# MAGIC if test -f "$OUTPUT_DATA_FILE"; then
# MAGIC     cat $OUTPUT_DATA_FILE
# MAGIC fi
