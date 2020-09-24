from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('FakeFriends')
sc = SparkContext(conf=conf)


def parse_line(line):
    fields = line.split(',')
    age = fields[2]
    no_of_friends = int(fields[3])
    return age, no_of_friends


lines = sc.textFile("file:///E:/BigData/Python/Spark/fakefriends.csv")
rdd = lines.map(parse_line)

totals_by_age = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
average_by_age = totals_by_age.mapValues(lambda x: x[0] / x[1])
results = average_by_age.collect()

for value in results:
    print(value)
