'''Rock Paper Sissors Game'''
# Your Choice
Choice = (input("Rock, Paper or Sissors"))

import random

# Coputers List of Choices
options_list = ["Rock", "Paper", "Sissors",]
#Computer Picking Choice
random_selection = random.choice(options_list)


#printing Computers Choice
print(f"{random_selection}")

print(Choice)
if Choice == "Rock" and random_selection == "Sissors":
    print("You Win")
if Choice == "Rock" and random_selection == "Paper":
    print("You Loose")
if Choice == "Rock" and random_selection == "Rock":
    print("Tie")
if Choice == "Sissors" and random_selection == "Sissors":
    print("Tie")
if Choice == "Sissors" and random_selection == "Paper":
    print("You Win")
if Choice == "Sissors" and random_selection == "Rock":
    print("You Loose")
if Choice == "Paper" and random_selection == "Sissors":
    print("You Loose")
if Choice == "Paper" and random_selection == "Paper":
    print("Tie")
if Choice == "Paper" and random_selection == "Rock":
    print("You Win")










