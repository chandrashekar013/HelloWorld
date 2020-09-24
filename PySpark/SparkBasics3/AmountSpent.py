from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('AmountSpent')
sc = SparkContext(conf=conf)


def get_customer_details(line):
    fields = line.split(',')
    customer_id = fields[0]
    amount = float(fields[2])
    return customer_id, amount


lines = sc.textFile("file:///E:/BigData/Python/Spark/customer-orders.csv")
rdd = lines.map(get_customer_details)
total_amount = rdd.reduceByKey(lambda x, y: (x + y))
sorted_total_amount = total_amount.map(lambda x: (x[1], x[0])).sortByKey(False)

total_amount_ret = sorted_total_amount.collect()

for c in total_amount_ret:
    print('customer: ', c[1], ': amount: ', c[0])
