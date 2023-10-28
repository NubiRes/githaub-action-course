# Databricks notebook source
# MAGIC %md
# MAGIC #### Protecting the main branch

# COMMAND ----------

print("Hello World")
print("Greetings Hello World")

# COMMAND ----------

print("Added branch protection")

# COMMAND ----------

df = spark.read \
    .option("inferSchema", "true") \
        .option("header", "true") \
            .csv("/mnt/formula1dlg2a/employee/employee_list_1_day_3.csv")

display(df)

# COMMAND ----------



# COMMAND ----------


