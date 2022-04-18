spark = SparkSession.builder().master("local[1]")
          .appName("SparkByExamples.com")
          .getOrCreate()
		  
df = spark.read.csv("/tmp/resources/zipcodes.csv")
df.printSchema()

#alternative-1
df1 = spark.read.format("csv").load("/tmp/resources/zipcodes.csv")
df1.printSchema()

#alternative-2
df2 = spark.read.format("org.apache.spark.sql.csv").load("/tmp/resources/zipcodes.csv")
df2.printSchema()