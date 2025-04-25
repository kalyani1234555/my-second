# there's no difference between single or double quotes in python. if you start a string with one type then
# must finish it the same type.

print("Today is a good day to learn python")
print('python is fun')

# if you use single quote in a string, then use double quotes to enclose the string

print("python's string are easy to use")

# if you use double quote in a string, then use single quotes to enclose the string

print('we can even include "quotes" in strings')

# we can also concatenate(join) strings to make longer ones, using plus

print("hello" + "world")
print("hello" + " world")

# we can also store the strings in variables, and then concatenation makes more sense"""
greeting = "Hello"  # variable greeting is bound to the string "Hello"
# name = "kalyani"
# input function to read the name from the keyboard. input function displays the text provided to it,
# then waits the text to be entered at the keyboard.
name = input("Please enter your name ")  # the input function called first When it finished,
# when the user presses enter, the value it returns is assigned to our variable name

print(greeting + name)

# if we want the space, we can add that too
print(greeting + " " + name)

age = 25
print(age)

print(type(name))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"pi is approximately {22/7:12.50f}")
pi = 22/7
print(f"pi is approximately {pi:12.50f}")
