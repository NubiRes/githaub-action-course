# Databricks notebook source
# MAGIC %md
# MAGIC #### The protection rules apply to all including adminstrators. I romoved the approver.

# COMMAND ----------

print("checking the protection of the main barnch")

print("checking the protection of the main barnch")
print("checking the protection of the main barnch")
print("checking the protection of the main barnch")

# COMMAND ----------

# MAGIC %md
# MAGIC # No Approver Required

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/formula1dlg2a/presentation/driver_standing/

# COMMAND ----------

df = spark.read.parquet("/mnt/formula1dlg2a/presentation/driver_standing/")

# COMMAND ----------

display(df)

# COMMAND ----------


