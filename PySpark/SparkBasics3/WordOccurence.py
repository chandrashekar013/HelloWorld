from pyspark import SparkConf, SparkContext
import re

conf = SparkConf().setMaster('local').setAppName('WordOccurence')
sc = SparkContext(conf=conf)


def normalize_words(line):
    return re.compile(r'\W+', re.UNICODE).split(line.lower())


lines = sc.textFile("file:///E:/BigData/Python/Spark/book.txt")
rdd = lines.flatMap(normalize_words)
print(type(rdd), 'mn')

words_by_count = rdd.countByValue()
print(type(words_by_count), 'hi')

for word, count in words_by_count.items():
    clean_word = word.encode('ascii', 'ignore')
    if clean_word:
        print(clean_word, ':', count)
