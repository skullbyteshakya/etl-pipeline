from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Read SQLite Table Data") \
    .config("spark.driver.extraClassPath", "sqlite-jdbc-3.45.2.0.jar") \
    .getOrCreate()

# Define the SQLite database URL
db_url = "jdbc:sqlite:/CODE/projects/ETL/etl-pipeline/sources/characters.db"

# Define the table name
table_name = "characters"

# Define connection properties
properties = {
    "driver": "org.sqlite.JDBC",
    "user": "",  # SQLite doesn't use username/password authentication by default
    "password": ""
}

# Read data from the SQLite table
df = spark.read.jdbc(url=db_url, table=table_name, properties=properties)

# Show the DataFrame schema and first few rows
df.printSchema()
df.show()

# Stop the SparkSession
spark.stop()

"""
OUTPUT :

root
 |-- character_id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- occupation: string (nullable = true)
 |-- bounty: integer (nullable = true)
 |-- devil_fruit: string (nullable = true)

+------------+-----------------+--------------------+----------+---------------+
|character_id|             name|          occupation|    bounty|    devil_fruit|
+------------+-----------------+--------------------+----------+---------------+
|           1|  Monkey D. Luffy|      Pirate Captain|1500000000|Gomu Gomu no Mi|
|           2|     Roronoa Zoro|           Swordsman| 320000000|           null|
|           3|             Nami|           Navigator|  66000000|           null|
|           4|            Usopp|              Sniper| 200000000|           null|
|           5|            Sanji|                Cook| 330000000|           null|
|           6|Tony Tony Chopper|              Doctor| 100000000|Hito Hito no Mi|
|           7|       Nico Robin|       Archaeologist| 130000000|Hana Hana no Mi|
|           8|           Franky|          Shipwright|  94000000|           null|
|           9|            Brook|            Musician|  83000000|Yomi Yomi no Mi|
|          10|           Jinbei|Fish-Man Karate M...| 438000000|           null|
+------------+-----------------+--------------------+----------+---------------+

"""