from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetrics.config.ConfigStore import *
from createmetrics.udfs.UDFs import *

def credit_score_table_1(spark: SparkSession) -> DataFrame:
    return spark.sql(f"SELECT * FROM test_delta.credit_score_table VERSION AS OF 1")
