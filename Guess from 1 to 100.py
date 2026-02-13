import random
correct = False
while correct == False:
    
    number = random.randint(1,100)
    
    Guess = (input("Guess a Number Between 1 and 100"))
    
    if Guess == (f"{number}"):
        print("Correct")
        correct = True

    else:
        print("Incorrect")