from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from importdataoption.config.ConfigStore import *
from importdataoption.udfs.UDFs import *

def TransUnionFICOxml(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("xml")\
        .option("rowTag", "Subject")\
        .option("mode", "PERMISSIVE")\
        .schema(
          StructType([
            StructField("Address", StringType(), True), StructField("FICO", StructType([
              StructField("Score", LongType(), True), StructField("ValidFrom", DateType(), True), StructField("ValidTo", StringType(), True)
            ]), True), StructField("Name", StringType(), True), StructField("SSN", StringType(), True), StructField("Trades", StructType([
              StructField("Trade", ArrayType(
              StructType([
                StructField("AccountNumber", StringType(), True), StructField("Balance", LongType(), True), StructField("DateOpened", DateType(), True), StructField("PastDue", LongType(), True), StructField("Terms", StringType(), True)
            ]), 
              True
          ), True)
            ]), True)
        ])
        )\
        .load("dbfs:/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ingest/FICO/TransUnionFICO.xml")