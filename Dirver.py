
name = ["Henry", "Rory", "Lucas", "Terence"]
drive = ["No licence", "No licence", "Learners", "Restricted"]
quit = 1
while quit != 0:
    print("Student driver status")
    print("=" * 25)
    for i in range(len(name)):
        print(f"{i+1}. {name[i]:10} {drive[i]:10}")
    selection = int(input("Select Student to update:"))
    if selection == 0:
        quit = 0
    else:
        drive2 = input("Enter new status")
        drive[selection-1] = drive2
    if selection == 4:
        name = ["Henry", "Rory", "Lucas", "Diddy"]
   
  
    
