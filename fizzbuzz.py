'''Fizzbuzz Game'''

number = int(input("Enter A Number"))
number = number + 1

for num in range(1,number):
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")

    else:
        print(f"{num}")
    
