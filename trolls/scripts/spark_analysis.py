from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col, count, explode, split, regexp_replace, lower, length

spark = SparkSession.builder.appName("Russian Troll Tweets Analysis").getOrCreate()

df = spark.read.csv("data/raw/troll_tweets.csv", header=True, inferSchema=True)

df.write.mode("overwrite").parquet("data/parquet/tweets.parquet")

df_parquet = spark.read.parquet("data/parquet/tweets.parquet")
df_parquet.createOrReplaceTempView("tweets")

result = spark.sql("""
SELECT to_date(try_to_timestamp(publish_date, 'M/d/yyyy H:mm')) as tweet_date, COUNT(*) AS tweet_count
FROM tweets
WHERE try_to_timestamp(publish_date, 'M/d/yyyy H:mm') IS NOT NULL
GROUP BY tweet_date
ORDER BY tweet_date
""")

result.show(50)

result.write.mode("overwrite").csv("data/trends/tweet_trends.csv", header=True)

result_authors = spark.sql("""
SELECT author, COUNT(*) AS tweet_count
FROM tweets
GROUP BY author
ORDER BY tweet_count DESC
LIMIT 10
""")

result_authors.show()

result_authors.write.mode("overwrite").csv("data/trends/top_authors.csv", header=True)

result_lang = spark.sql("""
SELECT language, COUNT(*) AS tweet_count
FROM tweets
GROUP BY language
ORDER BY tweet_count DESC
""")

result_lang.show()

result_lang.write.mode("overwrite").csv("data/trends/language_distribution.csv", header=True)

result_hashtags_df = spark.sql("""
SELECT explode(regexp_extract_all(lower(content), '(#\\\\w+)', 0)) AS word
FROM tweets
WHERE content IS NOT NULL AND content RLIKE '#\\\\w+'
""")

top_hashtags = result_hashtags_df.groupBy("word").count().orderBy(col("count").desc(), col("word").asc()).limit(20)

top_hashtags.show()

top_hashtags.write.mode("overwrite").csv("data/trends/top_hashtags.csv", header=True)

spark.sparkContext.setLogLevel("ERROR")

spark.stop()