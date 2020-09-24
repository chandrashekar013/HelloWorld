from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('MinimumTemp')
sc = SparkContext(conf=conf)


def parse_lines(line):
    fields = line.split(',')
    station_id = fields[1]
    temp_type = fields[2]
    temp = fields[3]
    return station_id, temp_type, temp


lines = sc.textFile("file:///E:/BigData/Python/Spark/1800.csv")
rdd = lines.map(parse_lines)
print(rdd)

min_temps = rdd.filter(lambda x: 'TMIN' in x[1])
station_temp = min_temps.map(lambda x: (x[0], x[2]))
min_temp = station_temp.reduceByKey(lambda x, y: min(x, y))
results = min_temp.collect()

for values in results:
    print(values[0], values[1])
