import requests


def extract_data(spark):
    """Load data from Parquet file format.

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """
    # Extract data from CSV ---------------------------------------------------------

    abilities = spark.read.format("csv").option("header", "true").load("hdfs://source_data/csv/abilities.csv")
    abilities.printSchema()
    abilities.show()

    # Extract data from API ---------------------------------------------------------
    # Define the API URL
    api_url = "http://127.0.0.1:5000/api/data"

    # Fetch data from the API
    response = requests.get(api_url)
    islands = True
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response content as JSON
        data = response.json()

        # Create a DataFrame from the JSON data
        islands = spark.createDataFrame(data)

        # Show the DataFrame schema and first few rows
        islands.printSchema()
        islands.show()
    else:
        print("Failed to fetch data from the API:", response.status_code)

    # Extract data from SQLite ---------------------------------------------------------
    # .config("spark.driver.extraClassPath", "sqlite-jdbc-3.45.2.0.jar")
    # make sure to add this in the sparksession creation

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
    characters = spark.read.jdbc(url=db_url, table=table_name, properties=properties)
    characters.printSchema()
    characters.show()

    return abilities, islands, characters
