MIN_AGE = 16
MIN_WEIGHT = 50

age = int(input("Enter Your Age"))
weight = int(input("Enter Your Weight"))
if age >= MIN_AGE and weight >= MIN_WEIGHT:
    print("Eligible")
else:
     print("Your Not Eligible")

