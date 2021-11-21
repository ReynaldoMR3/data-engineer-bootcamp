import sys

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

from pyspark.sql.functions import regexp_replace, trim, col, lower, when, array_contains
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import StopWordsRemover


def cleanStrings(column):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.
    Arguments:   
        column: A  dataframe column.

    Returns:
        Column: A Column named 'clean_reviews' with clean-up operations applied.
    """
    return lower(trim(regexp_replace(column,'\\p{Punct}',''))).alias('clean_reviews')

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "glue-db", table_name = "raw20211120222308229600000004")

datasource1 = datasource0.toDF()

datasource2 = datasource1.select('cid', cleanStrings(col('review_str')))

tokenizer = Tokenizer(inputCol="clean_reviews", outputCol="final_reviews")

datasource3 = tokenizer.transform(datasource2)

remover = StopWordsRemover(inputCol='final_reviews', outputCol='review_token')

datasource4 = remover.transform(datasource3)

datasource5 = (
    datasource4
        .select(
            'cid', 
            'review_token',
            when(array_contains('review_token', 'good'), True)
                .otherwise(False)
                .alias('positive_review')
            )
)

datasource6 = (
    datasource5
        .select(
            'cid',
            when(col('positive_review') == True, 1)
                .otherwise(0)
                .alias('positive_review')
        )
)


datasource7 = DynamicFrame.fromDF(datasource6, glueContext, 'positive_reviews')

datasink1 = glueContext.write_dynamic_frame.from_options(frame = datasource7, connection_type = "s3", connection_options = {"path": "s3://staging20211120201523566000000005"}, format = "parquet")

job.commit()