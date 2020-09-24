# Exceptions, Generators, Comprehensions n lambda expression
import functools


# exception


def throw_exception(a, b):
    return a / b


try:
    throw_exception(1, 0)
except ZeroDivisionError:
    print('exception occurred')


# yield


def yield_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


for value in yield_generator(5):
    print(value)  # would return same value as range

# list comprehensions
numbers = [1, 2, 3, 4]
square = []

for number in numbers:
    square.append(number * 2)
print(square)

# alternate in list comprehension
square = [number * 2 for number in numbers]
print(square)

# set comprehension
square = {number * 2 for number in numbers}
print(square)

# conditional comprehension
numbers = ['1', '2', '3', '4']
number_without_four = [number for number in numbers if '4' not in number]
print(number_without_four)

x = 12
expression = 'twelve' if x == 12 else 'unknown'
print(expression)

# nested comprehensions
animals = ['Tiger', 'lion', 'cheetah']
colors = ['brown', 'yellow', 'pale-yellow']

for anm_color in [(animal, color) for animal in animals for color in colors]:
    print(anm_color)

# map
string = "this is a sentence"
for word in map(str.upper, string.split(' ')):  # map contains one function n iterable as arg0
    print(word)


# reduce


def sum_no(a, b: int):
    return a + b


numbers = [1, 3, 4, 1, 2]
rv = functools.reduce(sum_no, numbers)
print(rv)

# All Any
numbers = [1, 2, 3, 4, 0]
print('All: ', all(numbers))
print('Any: ', any(numbers))
