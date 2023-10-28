# Databricks notebook source
print("my third notebook")

print("my fourth notebook")
print("my fith notebook")
print("my seventh notebook")

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/formula1dlg2a/processed/constructors/

# COMMAND ----------

df = spark.read.parquet("/mnt/formula1dlg2a/processed/constructors/")

display(df)

# COMMAND ----------


