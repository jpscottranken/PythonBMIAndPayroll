# pythonListMenu.py
import pythonListMethods as plm

def theListMenu():
    employees = []  # List of employees

    options = {  # Set of menu options
        "1": lambda: plm.addNewEmployee(employees, 1),
        "2": lambda: plm.clearEmployeeList(employees),
        "3": lambda: print(plm.copyEmployeeList(employees)),
        "4": lambda: print(plm.countEmployees(employees)),
        "5": lambda: print(plm.findEmployeeIndex(employees, int(input("Enter associated employee number:\t")))),
        "6": lambda: plm.insertNewEmployee(employees, int(input("Enter position to insert new employee:\t"))),
        "7": lambda: plm.popEmployee(employees, int(input("Enter position to pop:\t"))),
        "8": lambda: plm.removeEmployeeByEmpNumber(employees, input("Enter employee number to remove:\t")),
        "9": lambda: plm.reverseEmployeeList(employees),
        "10": lambda: plm.sortEmployeeList(employees),
        "11": lambda: plm.displayAllEmployees(employees)
    }

    while True:
        print("\nPython List Menu")
        print("Enter a   1 to add a new employee")
        print("Enter a   2 to clear the employee list")
        print("Enter a   3 to make a copy of the employee list")
        print("Enter a   4 to count the current number of employees")
        print("Enter a   5 to find an employee index")
        print("Enter a   6 to insert a new employee at position x")
        print("Enter a   7 to remove (pop) employee at position x")
        print("Enter an  8 to remove an employee via employee number")
        print("Enter a   9 to reverse the employee list")
        print("Enter a  10 to sort the employee list by employee number")
        print("Enter an 11 to display all employees")
        print("Enter a  12 to exit the program now")

        choice = input("Enter a 1 - 12 now please:\t")
        if choice == "12":
            plm.endProgram()
        elif choice in options:
            try:
                options[choice]()
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid choice. Please try again.")