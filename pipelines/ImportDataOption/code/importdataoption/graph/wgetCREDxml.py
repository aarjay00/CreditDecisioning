from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from importdataoption.config.ConfigStore import *
from importdataoption.udfs.UDFs import *

def wgetCREDxml(spark: SparkSession):
    import os
    os.system(
        'wget https://raw.githubusercontent.com/databricks/terraform-databricks-lakehouse-blueprints/prophecy_quickstart/industry/fsi/data/credit_report.xml'
    )

    return 
