'''This Program demonstrates print, data types, variables, inputs and f-strings'''

print(123)
print("Hello")
# You Need Speech marks("") when printing text 
#Diffrant Data Types
#Interges, Decimals(Floating point numbers)
# Text (string), boolean (true or false)

# We use variables to store infomation
# variables must be all lower case
name = "Chico"
first_name = "alex"
last_name = "green"
age = 16

# you can use varible inside print() statements
print(name)
# to combine variable with a string we use f-strings
# the variable goes inside curly brakets {}
print(f"My cat is called {name} and he is {age} years old")

# we Use input() to get input from the user


user_name = input("What is your name?")
print(f"Hello {user_name}")

user_age = input(f"Hi {user_name} how old are you")
print(f"You are {user_name} and you are {user_age}")