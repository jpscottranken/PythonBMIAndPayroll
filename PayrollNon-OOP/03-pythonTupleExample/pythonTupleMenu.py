# pythonTupleMenu.py

'''
    This program implementation will use Python Tuples
    to mange employee information. In addition, it will use
    the Python Tuple methods as opposed to the Python
    Dictionary methods in the previous program.

    Like the previous program each employee will be
    identified by his/her unique employee number.

    It is also constructed using a console menu.
'''

import pythonTupleMethods as ptm

def theTupleMenu():
    #   Assume the following Python tuple of employee records
    employees = [                       #   Tuple of employee records
                    (211489, "Emma", "Smith", 33.09, 24.49, 810.37),
                    (328730, "Olivia", "Johnson", 31.75, 35.08, 1113.79),
                    (166083, "Ava", "Williams", 29.86, 92.88, 2773.40),
                    (655817, "Isabella", "Brown", 59.78, 12.6, 877.84),
                    (415777, "Sophia", "Jones", 70.43, 82.5, 7065.71),
                    (916687, "Mia", "Garcia", 4.3, 62.67, 269.48),
                    (690990, "Amelia", "Miller", 21.02, 55.17, 1159.67),
                    (837837, "Harper", "Davis", 29.37, 56.92, 1671.74),
                    (161640, "Evelyn", "Rodriguez", 69.99, 47.41, 4029.14),
                    (126821, "Abigail", "Martinez", 67.81, 91.43, 7471.20),
                    (863150, "Ella", "Hernandez", 14.72, 92.41, 1360.28),
                    (890538, "Elizabeth", "Lopez", 14.67, 3.14, 46.06),
                    (899620, "Camila", "Gonzalez", 25.03, 64.95, 1625.70),
                    (477071, "Luna", "Wilson", 59.81, 35.51, 2475.58),
                    (430709, "Sofia", "Anderson", 10.45, 80.79, 844.26),
                    (294856, "Avery", "Thomas", 16.22, 96.37, 1563.12),
                    (656481, "Mila", "Taylor", 39.04, 8.48, 331.06),
                    (432047, "Aria", "Moore", 69.32, 44.98, 3777.42),
                    (896900, "Scarlett", "Jackson", 6.96, 38.73, 269.56),
                    (127103, "Penelope", "Martin", 56.76, 92.56, 6029.36),
                    (248991, "Layla", "Bronson", 28.08, 95.22, 2673.78),
                    (826365, "Chloe", "Perez", 29.43, 81.04, 2385.01),
                    (662556, "Victoria", "Thompson", 83.25, 90.25, 9464.97),
                    (815071, "Madison", "White", 69.42, 13.36, 1123.98),
                    (438868, "Eleanor", "Harris", 19.3, 8.12, 156.72)
                ]

    options = {                            # Set of menu options
        "1": lambda: ptm.areAllEmployeeNumbersUnique(employees),
        "2": lambda: ptm.areAnyEmployeeFirstOrLastNamesEmpty(employees),
        "3": lambda: ptm.areAllHoursWorkedAndHourlyRatesWithinRange(employees),
        "4": lambda: ptm.countNumberOfEmployeesWorkingOvertime(employees),
        "5": lambda: ptm.countNumberOfEmployeesNotWorkingOvertime(employees),
        "6": lambda: ptm.countNumberOfEmployeesMakingMinimumWageOrAbove(employees),
        "7": lambda: ptm.countNumberOfEmployeesNotMakingMinimumWage(employees),
        "8": lambda: ptm.indexOfEmployeeWithHighestEmployeeNumber(employees),
        "9": lambda: ptm.indexOfEmployeesWithHighestHourlyRate(employees),
        "10": lambda: ptm.indexOfEmployeesWorkingMostHours(employees),
        "11": lambda: ptm.indexOfEmployeeWithLargestGrossPay(employees),
        "12": lambda: ptm.indexesOfEmployeesWorkingOvertime(employees),
        "13": lambda: ptm.endProgram()
    }

    while True:
        ptm.sleepThenClear()
        print("\nPython Tuples Menu")
        print("Enter a   1 to show if all employee numbers are unique or not")
        print("Enter a   2 to show if any employee first/last names are empty")
        print("Enter a   3 to show if all hours worked and hourly rates are within range")
        print("Enter a   4 to count the number of employees working overtime")
        print("Enter a   5 to count the number of employees not working overtime")
        print("Enter a   6 to count the number of employees making minimum wage or above")
        print("Enter a   7 to count the number of employees not making minimum wage")
        print("Enter an  8 to show the index of the employee with the highest employee number")
        print("Enter a   9 to show the index of the employee with the highest hourly rate")
        print("Enter a   10 to show the index of the employee working the most hours")
        print("Enter a   11 to show the index of the employee with the largest gross pay")
        print("Enter a   12 to show the indexes of all employees working overtime")
        print("Enter a   13 to exit the program now")
   
        choice = input("Enter a 1 - 13 now please:\t")
        if choice == "13":
            ptm.endProgram()
        elif choice in options:
            try:
                options[choice]()
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid choice. Please try again.")