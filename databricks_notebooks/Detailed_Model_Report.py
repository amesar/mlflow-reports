# Databricks notebook source
# MAGIC %md ## Detailed MLflow Model Report
# MAGIC
# MAGIC **Overview**
# MAGIC * Generates a markdown file (*.md) for the detailed report for an MLflow model.
# MAGIC
# MAGIC **Widgets**
# MAGIC * `Model URI` - either the experiment name or the ID
# MAGIC * `Get permissions` - dump run data if showing runs
# MAGIC * `Output file` - output markdown file such as `model.md`

# COMMAND ----------

# MAGIC %md #### Setup

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

dbutils.widgets.text("1. Model URI", "")
dbutils.widgets.dropdown("2. Get permissions", "yes", ["yes","no"])
dbutils.widgets.text("3. Output file", "")

model_uri = dbutils.widgets.get("1. Model URI")
get_permissions = dbutils.widgets.get("2. Get permissions") == "yes"

output_file = dbutils.widgets.get("3. Output file")
import os
os.environ["OUTPUT_FILE"] = output_file

print("model_uri:", model_uri)
print("get_permissions:", get_permissions)
print("output_file:", output_file)

# COMMAND ----------

assert_widget(model_uri, "1. Model URI")
assert_widget(output_file, "2. Output file")

# COMMAND ----------

# MAGIC %md #### Build markdown report

# COMMAND ----------

from mlflow_reports.markdown import detailed_report

data = detailed_report.build_report(model_uri, get_permissions, output_file)
dump_as_json(data)

# COMMAND ----------

# MAGIC %md #### Check markdown output file

# COMMAND ----------

# MAGIC %sh echo $OUTPUT_FILE
# MAGIC ls -l $OUTPUT_FILE 

# COMMAND ----------

# MAGIC %sh cat $OUTPUT_FILE 
