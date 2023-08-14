# Databricks notebook source
import os
import pandas as pd

# COMMAND ----------

path = "./wine.csv"
path

# COMMAND ----------

df = pd.read_csv(path)
df

# COMMAND ----------

opath = "wine2.csv"
with open(opath, "w") as f:
  df.to_csv(f, index=False)

# COMMAND ----------


