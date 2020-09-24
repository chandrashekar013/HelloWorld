from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('PopularSuperHero')
sc = SparkContext(conf=conf)


def get_marvel_occurences(line):
    fields = line.split()
    return fields[0], len(fields) - 1


def get_marvel_names(text):
    fields = text.split()
    return fields[0], fields[1]


load_marvel_occurences = sc.textFile("file:///E:/BigData/Python/Spark/Marvel-graph.txt")
marvel_occurences = load_marvel_occurences.map(get_marvel_occurences)

load_marvel_names = sc.textFile("file:///E:/BigData/Python/Spark/Marvel-names.txt")
marvel_names = load_marvel_names.map(get_marvel_names)

count_marvel = marvel_occurences.reduceByKey(lambda x, y: x + y).map(lambda x: (x[1], x[0])).sortByKey()

popular_movie_id = count_marvel.max()
popular_marvel_name = marvel_names.lookup(popular_movie_id[1])[0]
print(popular_marvel_name)
