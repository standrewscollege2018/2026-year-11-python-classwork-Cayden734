'''Rock Paper Sissors Game'''
# Your Choice
import random
for i in range (0,4):
    Choice = (input("Rock, Paper or Sissors"))

    

    # Coputers List of Choices
    options_list = ["Rock", "Paper", "Sissors",]
    #Computer Picking Choice
    random_selection = random.choice(options_list)


    #printing Computers Choice
    print(f"{random_selection}")

    print(Choice)
    if Choice.lower() == "rock" and random_selection == "sissors":
        print("You Win")
    if Choice.lower() == "Rock" and random_selection == "paper":
        print("You Loose")
    if Choice.lower() == "Rock" and random_selection == "rock":
        print("Tie")
    if Choice == "Sissors" and random_selection == "sissors":
        print("Tie")
    if Choice == "Sissors" and random_selection == "paper":
        print("You Win")
    if Choice == "Sissors" and random_selection == "rock":
        print("You Loose")
    if Choice == "Paper" and random_selection == "sissors":
        print("You Loose")
    if Choice == "Paper" and random_selection == "paper":
        print("Tie")
    if Choice == "Paper" and random_selection == "rock":
        print("You Win")










