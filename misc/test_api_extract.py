from pyspark.sql import SparkSession
import requests

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Read API URL Data") \
    .getOrCreate()

# Define the API URL
api_url = "http://127.0.0.1:5000/api/data"

# Fetch data from the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response content as JSON
    data = response.json()

    # Create a DataFrame from the JSON data
    df = spark.createDataFrame(data)

    # Show the DataFrame schema and first few rows
    df.printSchema()
    df.show()
else:
    print("Failed to fetch data from the API:", response.status_code)

# Stop the SparkSession
spark.stop()

"""
OUTPUT : 

root
 |-- climate: string (nullable = true)
 |-- island_id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- terrain: string (nullable = true)

+-------+---------+-----------------+-------------+
|climate|island_id|             name|      terrain|
+-------+---------+-----------------+-------------+
|    Hot|        1|         Alabasta|       Desert|
|   Mild|        2|        Dressrosa|      Plateau|
|   Cold|        3|     Wano Country|     Mountain|
|   Mild|        4|          Water 7|         City|
|   Warm|        5|Whole Cake Island|       Island|
|   Warm|        6|      Enies Lobby|       Island|
| Cloudy|        7|          Skypiea|   Sky Island|
|  Humid|        8|  Fish-Man Island|   Underwater|
|   Cold|        9|      Drum Island|Winter Island|
+-------+---------+-----------------+-------------+
"""