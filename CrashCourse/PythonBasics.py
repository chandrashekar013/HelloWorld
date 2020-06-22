# simple print & Plain calculations
print("hello,world !!")
print(1 + 2)
print(float(1 * 2))
print("this " + "line contains", " multiple", "words with a number as well", 3)

# "' both used interchangeable in String
print("Hi , how are you. I'm fine")
print('How about you, Me too doing great"')

# variable and print value
greeting = "Welcome !!"
print(greeting)

# take input from keyboard
input_keyboard = input('Please enter the name: ')
print("Hi " + input_keyboard)

# escape characters \n and \t
split_words = "this\n " + "word as been split \n multiple times. Also has few tab \t characters"
print(split_words)

# String split over multiple lines'
multiple_lines = """ this 
sentence has been split
over multiple
lines"""
print(multiple_lines)

# undo multiple line split using escape character
multiple_line_split_undo = """multiple \
line split \
has been undone """
print(multiple_line_split_undo)

# use escape character as raw literal
print("c:\\users\\windows")
print(r"c:\users\windows")

# type of variable n convert point same variable label to string
height = 172
print(type(height))

height = "one hundred seventy two"
print(height, type(height))

# concat int and str
# print("Hi number " + 3)  # will throw error
print("Hi number " + str(3))

# operators
a = 10
b = 5
print(a // b)  # integer division. output: 2
print(a / b)  # regular division. output: 2.0

# Sequence - Str
sequence_string = "sequence"
print(sequence_string[3])  # output: u

# negative index
print(sequence_string[-2])  # output: c


