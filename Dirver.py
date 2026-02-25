

name = ["Henry", "Rory", "Lucas", "Terence"]
drive = ["No licence", "No licence", "Learners", "Restricted"]
quit = 1
while quit != 0:
    print("Student driver status")
    print("=" * 25)
    for i in range(len(name)):
        print(f"{i+1}. {name[i]:10} {drive[i]:10}")

    # Get selection and error prevention
    get_selection = True
    while get_selection == True:
        try:
            selection = int(input("Select Student to update:"))
            if selection < 0 or selection > len(name):
                print("Invalid number")
            else:
                get_selection = False

        except ValueError:
            print("Invalid data type")

    if selection == 0:
        quit = 0
    else:
        drive2 = input("Enter new status")
        if drive2 in drive:
            drive[selection-1] = drive2
            if selection == 4:
                name = ["Henry", "Rory", "Lucas", "Diddy"]
        else:
            print("Incorrect Status")
                

        
   
  
    
