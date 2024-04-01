# Import necessary libraries
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SQLiteReader").getOrCreate()

# Define the JDBC URL for SQLite
jdbc_url = "jdbc:sqlite:/sources/characters.db"

# Read data from a table named "your_table"
df = spark.read.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "characters") \
    .load()

# Show the data
df.show()