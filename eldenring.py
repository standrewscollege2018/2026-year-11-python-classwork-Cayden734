'''Helps With Soulsbrone Bosses'''

gameoptions = ["Elden Ring", "Sekiro",]
gamesel = input(f"Enter A Game(Soulsborne)")
print(gamesel)
if gamesel.lower() == "starcraft":
    print("This Code is Only For Good Games and Not shit ones")
else:
    if gamesel in gameoptions:
        print("correct")

    else:
        print("Incorrect Game(Only Soulsborne)")

