Menu = [
    "ADD EXPENSE",
    "VIEW EXPENSE",
    "TOTAL EXPENSE",
    "EXIT"

]

while True:
    print("~~EXPENSE TRACKER~~")                                      #EXPENSE TRACKER PROGRAM
    print("1.ADD EXPENSE\n2.VIEW EXPENSE\n3.CALCULATE TOTAL\n4.EXIT") #FEATURES:
                                                                      #-ADD NEW EXPENSES
                                                                      #-VIEW EXPENSES
                                                                      #-CALCULATE TOTAL
                                                                      #-EXIT PROGRAM
                                                                      #-DATA STORED IN:expenses/#.txt                                                              #FEATURES:
                                                                      
   
    choice = int(input("Enter the choice: ")) #ENTERING CHOICE
     #MAIN LOOP - KEEPS RUNNING UNTIL USER EXITS

    if choice ==1:
        try:#EXCEPTION HANDLING
            amt = int(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount!!.Enter valid amount: ")
            continue

        category = input("Enter the category: ") #CATEGORY OF THE EXPENSE
        date = input("Enter the date: ")
        with open("expenses.txt","a") as file: #OPEN THE FILE AND APPEND(INSERT) NEW DATA INTO THE FILE(expenses.txt)
            file.write(f"{amt}|{category}|{date}\n")

    elif choice == 2:
        with open("expenses.txt","r") as file: #OPEN THE FILE IN READ MODE
            for line in file:
                print(line.strip()) #USE STRIP() TO REMOVE EXTRASPACES/NEWLINE

    elif choice == 3:
        total = 0 #INITIAL TOTAL
        with open("expenses.txt","r") as file:
            for line in file: #LOOPS THROUGH ALL EXPENSES IN THE FILE
                parts = line.strip().split("|")
                total += int(parts[0].strip()) #CALCULATE TOTAL BUT ADDING EACH EXPENSE AMOUNT 
            print(f"TOTAL IS: {total}") #PRINT THE TOTAL

    elif choice == 4:
        print("Exiting!!!") #EXIT THE PROGRAM
        break #CODE STOPS AFTER CHOICE 4

    else:
        print("Invalid choice!!.Select a valid choice(1-4)") #HANDLES INVALID MENU CHOICES

        
            
    