# pythonSetMenu.py

'''
    This program implementation will use Python Sets
    to mange employee information. In addition, it will use
    the Python Set methods as opposed to the Python
    Tuple methods in the previous program.

    Like the previous program each employee will be
    identified by his/her unique employee number.

    It is also constructed using a console menu.
'''

import pythonSetMethods as psm

def theSetMenu():
    #   Assume the following Python Set of employee records
    employees = {                       #   Set of employee records
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
                }

    options = {                            # Set of menu options
        "0": lambda: psm.addExample(),
        "1": lambda: psm.clearExample(),
        "2": lambda: psm.copyExample(employees),
        "3": lambda: psm.differenceExample(),
        "4": lambda: psm.difference_updateExample(),
        "5": lambda: psm.discardExample(),
        "6": lambda: psm.intersectionExample(),
        "7": lambda: psm.intersection_updateExample(),
        "8": lambda: psm.isdisjointExample(),
        "9": lambda: psm.issubsetExample(),
        "10": lambda: psm.issupersetExample(),
        "11": lambda: psm.popExample(),
        "12": lambda: psm.removeExample(),
        "13": lambda: psm.symmetric_differenceExample(),
        "14": lambda: psm.symmetric_difference_updateExample(),
        "15": lambda: psm.unionExample(),
        "16": lambda: psm.updateExample(),
        "17": lambda: psm.exitProgram()
    }

    psm.sleepThenClear()
    psm.showSetsForMethodExamples(employees)
    psm.sleepThenClear()

    while True:
        print("\nPython Sets Menu")
        print("Enter a   0 to show Python add() Set Method")
        print("Enter a   1 to show Python clear() Set Method")
        print("Enter a   2 to show Python copy()  Set Method")
        print("Enter a   3 to show Python difference() Set Method")
        print("Enter a   4 to show Python difference_update() Set Method")
        print("Enter a   5 to show Python discard() Set Method")
        print("Enter a   6 to show Python intersection() Set Method")
        print("Enter a   7 to show Python intersection_update() Set Method")
        print("Enter an  8 to show Python isdisjoint() Set Method")
        print("Enter a   9 to show Python issubset() Set Method")
        print("Enter a   10 to show Python issuperset() Set Method")
        print("Enter a   11 to show Python pop() Set Method")
        print("Enter a   12 to show Python remove() Set Method")
        print("Enter a   13 to show Python symmetric_difference Set Method")
        print("Enter a   14 to show Python symmetric_difference_update Set Method")
        print("Enter a   15 to show Python union() Method")
        print("Enter a   16 to show Python update() Method")
        print("Enter a   17 to exit the program now")
   
        choice = input("Enter a 1 - 17 now please:\t")
        if choice == "17":
            psm.endProgram()
        elif choice in options:
            try:
                options[choice]()
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid choice. Please try again.")