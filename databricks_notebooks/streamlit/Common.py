# Databricks notebook source
!pip install git+https:///github.com/amesar/mlflow-reports/#egg=mlflow-reports
!pip install mlflow_skinny==2.11.2 # NOTE: doesn't honor >= or default version
!pip install dbtunnel[asgiproxy,streamlit]
dbutils.library.restartPython()

# COMMAND ----------

token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
host_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get("browserHostName").get()
dbutils.fs.put("file:///root/.databrickscfg",f"[DEFAULT]\nhost=https://{host_name}\ntoken = "+token,overwrite=True)

# COMMAND ----------

import os
local_dir = "../../mlflow_reports/streamlit"
git_dir = "https://raw.githubusercontent.com/amesar/mlflow-reports/master/mlflow_reports/streamlit"

def mk_script_paths (script):
    script_paths = {
        "local": os.path.join(local_dir, script),
        "github": os.path.join(git_dir, script)
    }
    for k,v in script_paths.items():
        print(f"{f'{k}':<6}: {v}")
    return script_paths

# COMMAND ----------


