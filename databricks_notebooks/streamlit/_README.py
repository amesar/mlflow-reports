# Databricks notebook source
# MAGIC %md ## Streamlit MLflow and Databricks Notebooks
# MAGIC
# MAGIC ##### Overview
# MAGIC * Browse MLflow objects and Databricks endpoints in a single pane.
# MAGIC * Ability to see table view and API JSON response
# MAGIC * Thanks to team at https://github.com/stikkireddy/dbtunnel.
# MAGIC
# MAGIC ##### Notebooks
# MAGIC * [Streamlit_MLflow_Object_Explorer]($Streamlit_MLflow_Object_Explorer) - list and get details for MLflow objects.
# MAGIC   * Registered models, model versions, model signatures, experiments and runs.
# MAGIC * [Streamlit_Databricks_Explorer]($Streamlit_Databricks_Explorer) - list and get details for Databricks endpoints.
# MAGIC   * Model serving endpoints, vector search endpoints and vector search indexes.
# MAGIC
# MAGIC ##### Streamlight Python Scripts
# MAGIC * [../mlflow_reports/streamlit]($../../mlflow_reports/streamlit) - Streamlit Python file scripts.
# MAGIC * Streamlit relative local script paths work.
# MAGIC * Streamlit script paths as raw github seeem not to work yet from notebook.
# MAGIC
# MAGIC #####  Last updated: _2024-03-25_

# COMMAND ----------

# MAGIC %md #### Access Streamlit app in browser window
# MAGIC
# MAGIC ##### To open browser window with Streamlit app
# MAGIC
# MAGIC Click on `https://dbc-dp-1444828305810485.cloud.databricks.com/driver-proxy/o/1444828305810485/1116-012035-d88gkxi0/8080/`
# MAGIC
# MAGIC ##### Cell output
# MAGIC
# MAGIC ```
# MAGIC [2024-03-25T03:45:58+0000] [INFO] {streamlit.py:_run:26} - Starting server...
# MAGIC [2024-03-25T03:45:58+0000] [INFO] {tunnels.py:run_uvicorn_app:392} - Running proxy server via command: python -m dbtunnel.vendor.asgiproxy --port 8080 --service-port 9908 --url-base-path /driver-proxy/o/1444828305810485/1116-012035-d88gkxi0/8080/ --framework streamlit
# MAGIC [2024-03-25T03:45:58+0000] [INFO] {streamlit.py:_run:46} - Use this link to access the Streamlit UI in Databricks: 
# MAGIC https://dbc-dp-1444828305810485.cloud.databricks.com/driver-proxy/o/1444828305810485/1116-012035-d88gkxi0/8080/
# MAGIC [2024-03-25T03:45:59+0000] [INFO] {streamlit.py:run_streamlit:62} - Deploying streamlit app at path: /tmp/tmpq04zwimf/mlflow_objects.py on port: 9908
# MAGIC ```
