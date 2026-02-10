'''Calculate grade boundries'''

#set grade boundrys
MIN_A = 90
MIN_B = 70
MIN_C = 50

#Get Score From User
score = int(input("Enter you Score:"))

#Calculate the Grade
if score >= 0 and score <=100:
    if score >= MIN_A:
        print("A")
    elif score >= MIN_B:
        print("B")
    elif score >= MIN_C:
        print("C")
    else:
        print("fail")
else: 
    print("Invalid Score")