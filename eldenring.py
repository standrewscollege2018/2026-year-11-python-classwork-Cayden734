'''Helps With Soulsbrone Bosses'''
bossoption = ["Margit"]
gameoptions = ["Elden Ring", "Sekiro",]
gamesel = input(f"Enter A Game(Soulsborne)")
print(gamesel)
if gamesel.lower() == "starcraft":
    print("This Code is Only For Good Games and Not shit ones")
else:
    if gamesel in gameoptions:
        bosssel = input("Enter A Boss")
        if bosssel in bossoption:
            print("Correct")
            
            
        else:
            print("Incorrect Game(Only Soulsborne)")


