def extract_data(spark):
    """Load data from Parquet file format.

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """
    abilities = spark.read.format("csv").option("header", "true").load("hdfs://source_data/csv/abilities.csv")
    


    return True