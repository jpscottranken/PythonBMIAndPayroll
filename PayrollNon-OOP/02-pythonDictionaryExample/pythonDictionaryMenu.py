# pythonDictionaryMenu.py

'''
    This program implementation will use Python Dictionaries
    to mange employee information. In addition, it will use
    the Python Dictionary methods as opposed to the Python
    List methods in the previous program.

    Like the previous program each employee will be
    identified by his/her unique employee number. This will
    serve as the key.

    Like the previous program, the program provides
    functions to add, remove and manipulate employee records.
    It is also constructed using a console menu.
'''

import pythonDictionaryMethods as pdm

def theDictionaryMenu():
    employees = {}  # Dictionary of employees

    options = {  # Set of menu options
        "1": lambda: pdm.addNewEmployee(employees),
        "2": lambda: pdm.clearEmployeeDictionary(employees),
        "3": lambda: print(pdm.copyEmployeeDictionary(employees)),
        "4": lambda: print(pdm.countEmployees(employees)),
        "5": lambda: print(pdm.findEmployee(employees, int(input("Enter employee number:\t")))),
        "6": lambda: pdm.removeEmployee(employees, int(input("Enter employee number to remove:\t"))),
        "7": lambda: pdm.displayAllEmployees(employees)
    }

    while True:
        pdm.sleepThenClear()
        print("\nPython Dictionary Menu")
        print("Enter a   1 to add a new employee")
        print("Enter a   2 to clear the employee dictionary")
        print("Enter a   3 to make a copy of the employee dictionary")
        print("Enter a   4 to count the current number of employees")
        print("Enter a   5 to find an employee by employee number")
        print("Enter a   6 to remove an employee by employee number")
        print("Enter an  7 to display all employees")
        print("Enter a   8 to exit the program now")

        choice = input("Enter a 1 - 8 now please:\t")
        if choice == "8":
            pdm.endProgram()
        elif choice in options:
            try:
                options[choice]()
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid choice. Please try again.")