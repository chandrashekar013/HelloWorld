from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('PopularMovie')
sc = SparkContext(conf=conf)


def get_movie_names():
    movie_names = {}
    with open("E:/BigData/Python/Spark/ml-100k/u.ITEM") as f:
        for line in f:
            fields = line.split('|')
            movie_names[int(fields[0])] = fields[1]
    return movie_names


movie_dict = sc.broadcast(get_movie_names())
lines = sc.textFile("file:///E:/BigData/Python/Spark/ml-100k/u.data")
movie_id = lines.map(lambda x: int(x.split()[1]))
rdd = movie_id.map(lambda x: (x, 1)).reduceByKey(lambda x, y: (x + y))
sorted_rdd = rdd.map(lambda x: (x[1], x[0])).sortByKey(False)
# sortedMoviesWithNames = sortedMovies.map(lambda countMovie : (nameDict.value[countMovie[1]], countMovie[0]))
map_movie_name = sorted_rdd.map(lambda x: (movie_dict.value[x[1]], x[0]))
popular_movie = map_movie_name.collect()

for movies in popular_movie:
    print('movie_name: ', movies[0], 'count: ', movies[1])
