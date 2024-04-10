# Databricks notebook source
# MAGIC %md
# MAGIC # Header 1
# MAGIC ## Header 2
# MAGIC **bold text**
# MAGIC *italics text*
# MAGIC ~~strikethrough text~~
# MAGIC `monospace text`
# MAGIC ---
# MAGIC > Block quote
# MAGIC Ordered list:
# MAGIC 1. Item 1
# MAGIC 1. Item 2
# MAGIC 1. Item 3
# MAGIC Unordered list:
# MAGIC - Item a
# MAGIC - Item b
# MAGIC - Item c
# MAGIC

# COMMAND ----------

def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# COMMAND ----------

print(fibonacci(10))

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC
