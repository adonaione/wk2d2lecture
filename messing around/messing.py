# def say_hi(name):
#     if name == ' ':
#         print("You didn't enter anything!")
#     else:
#         print("Hi there...")
#         for letter in name:
#             print(letter)

# say_hi("adonai")

# name = input("What is your name? ")
# print("hi", name)
# while name == input("What is your name? "):
#     print(name)

# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8

# Vowels are: A, E, I, O, U

# create a space for user input
example = input("What is your name? ")
# loop through the string
vowels = ['a','e','o','u','i','A','E','O','U','I']
if str(vowels) in example:
    print("yes")
# identify and count vowels