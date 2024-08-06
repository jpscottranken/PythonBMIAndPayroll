# pythonListMethods.py
#import math
import os
import time

# Program constants
MINHOURS =  0.00      # Minimum employee hours worked
MAXHOURS = 84.00      # Maximum employee hours worked
MINHRATE =  0.00      # Minimum employee hourly rate
MAXHRATE = 99.99      # Maximum employee hourly rate
MAXNONOT = 40.00      # Minimum employee straight (non-OT) hours
OVERTIMERATE = 1.5    # Overtime rate

# This function attempts to add a new employee
# Said employee can be added either at the end of the list
# or in a specified postion in an existing list
def addNewEmployee(employees, number, position=0):
    employeeNumber = getEmployeeNumber(employees)
    employeeFirstName = getEmployeeFirstName()
    employeeLastName = getEmployeeLastName()
    employeeHoursWorked = getEmployeeHoursWorked()
    employeeHourlyRate = getEmployeeHourlyRate()
    employeeGrossPay = calculateEmployeeGrossPay(employeeHoursWorked, employeeHourlyRate)

    employee = [employeeNumber, employeeFirstName, employeeLastName, employeeHoursWorked, employeeHourlyRate, employeeGrossPay]

    if number == 1:  # Add employee to end of list
        employees.append(employee)
        print(f"Employee #{employeeNumber} was added to the end of the employees list")
    elif number == 2:  # Add employee at a specific position
        employees.insert(position, employee)
        print(f"Employee #{employeeNumber} was added to position {position} of the employees list")

# Input employee number. Number cannot be a duplicate,
# i.e. there cannot be an existing employee with this number.
def getEmployeeNumber(employees):
    while True:
        try:
            empNumber = int(input("Enter an employee number (must be unique):\t"))
            if empNumber == "" or any(emp[0] == empNumber for emp in employees):
                raise ValueError("Each Employee Number Must Be Unique and Non-Empty!")
            return empNumber
        except ValueError as ve:
            print(ve)

# Input employee first name. First name cannot be blank.
def getEmployeeFirstName():
    while True:
        firstName = input("Enter Employee First Name:\t\t\t")
        if firstName:
            return firstName
        else:
            print("First Name Cannot Be Left Empty. Please Try Again:")

# Input employee last name. Last name cannot be blank.
def getEmployeeLastName():
    while True:
        lastName = input("Enter Employee Last Name:\t\t\t")
        if lastName:
            return lastName
        else:
            print("Last Name Cannot Be Left Empty. Please Try Again:")

# Input employee hours worked. Hours worked name cannot be blank,
# cannot be non-numeric, and must be between 0.00 and 84.00.
def getEmployeeHoursWorked():
    while True:
        try:
            hoursWorked = float(input("Enter Hours Worked:\t\t\t\t"))
            if MINHOURS <= hoursWorked <= MAXHOURS:
                return hoursWorked
            else:
                # Print out-of-range error message
                print(f"Hours Worked Must Be Between {MINHOURS} And {MAXHOURS}. Please try again")
        except ValueError:
            # Print invalid input error message
            print(f"Input Was Invalid. Enter A Number Between {MINHOURS} And {MAXHOURS}.")

# Input employee hourly rate. Hourly rate name cannot be blank,
# cannot be non-numeric, and must be between 0.00 and 99.99.
def getEmployeeHourlyRate():
    while True:
        try:
            hourlyRate = float(input("Enter Hourly Rate:\t\t\t\t"))
            if MINHRATE <= hourlyRate <= MAXHRATE:
                return hourlyRate
            else:
               # Print out-of-range error message
                print(f"Hourly Rate Must Be Between {MINHRATE} And {MAXHRATE}. Please try again")
        except ValueError:
            # Print invalid input error message
            print(f"Input Was Invalid. Enter A Number Between {MINHRATE} And {MAXHRATE}.")

# Calculate gross pay. Straight time is hours worked * hourly rate
# OT is: 40 * hourly rate + ((hours worked - 40) * hourly rate * 1.5)
def calculateEmployeeGrossPay(hw, hr):
    if hw <= MAXNONOT:  # No Overtime Worked
        return hw * hr
    else:
        return (MAXNONOT * hr) + ((hw - MAXNONOT) * hr * OVERTIMERATE)

# Clear the employee list
def clearEmployeeList(employees):
  if (not(isTheListEmpty(employees))):
    employees.clear()
    print("The Employee List Has Been Cleared!")
  else:
     listIsEmpty()

# Create and return a copy of the employee list
def copyEmployeeList(employees):
  if (not(isTheListEmpty(employees))):
    return employees.copy()
  else:
    listIsEmpty()

# Give a count of the number of employees in
# the employee list
def countEmployees(employees):
  if (not(isTheListEmpty(employees))):
    print(f"There Are A Total Of {len(employees)} Employees In Our List!")
  else:
     listIsEmpty()

# Find an employee based on the inputted 
# employee number
def findEmployeeIndex(employees, number):
  if (not(isTheListEmpty(employees))):
    for e, employee in enumerate(employees):
        if employee[0] == int(number):
            # Match was found
            return e
        
    # No match was found
    return -1
  else:
     listIsEmpty()

# Insert a new employee at a desired position 
# in the employee list
def insertNewEmployee(employees, position):
    addNewEmployee(employees, 2, position)

# Remove a desired employee from a desired 
# position in the employee list
def popEmployee(employees, position):
  if (not(isTheListEmpty(employees))):
    if 0 <= position < len(employees):
        employeeToRemove = employees.pop(position)
        # Found the employee to pop
        print(f"Employee {employeeToRemove[0]} Removed From Position {position}")
    else:
        # Did not find the employee to pop
        print("Invalid Position Inputted. Please Try Again.")
  else:
    listIsEmpty()

# Delete an employee based on the
# inputted employee number
def removeEmployeeByEmpNumber(employees, number):
  if (not(isTheListEmpty(employees))):
    index = findEmployeeIndex(employees, number)
    if index != -1:
        # Found the employee to delete
        removedEmployee = employees.pop(index)
        print(f"Employee {removedEmployee} Has Been Removed From The List.")
    else:
        # Did not find the employee to delete
        print(f"Employee With Number {number} Not Found.")
  else:
    listIsEmpty()

# Reverse the order of the employee list
def reverseEmployeeList(employees):
  if (not(isTheListEmpty(employees))):
    # Reverse the order of the list
    employees.reverse()
    print(f"The Employee List Has Been Reversed")
  else:
    listIsEmpty()

# Sort the employee list by employee number
def sortEmployeeList(employees):
  if (not(isTheListEmpty(employees))):
    # Sort in ascending order by employeeNumber
    employees.sort(key=lambda e: e[0]) 
    print(f"The Employee List Has Been Sorted By The Employee Number")
  else:
    listIsEmpty()

# Display the current contents of the
# employee list
def displayAllEmployees(employees):
  if (not(isTheListEmpty(employees))):
    for employee in employees:
        print(f"Employee Number: {employee[0]}")
        print(f"Employee Name: {employee[1]} {employee[2]}")
        print(f"Employee Hours: {employee[3]:.2f}")
        print(f"Employee Rate: ${employee[4]:.2f}")
        print(f"Employee Gross: ${employee[5]:.2f}")
        print("\n")
  else:
    listIsEmpty()

def isTheListEmpty(employees):
    # If the employee list length is 0,
    # i.e. there are no employees in the
    # list, return True.
    if (len(employees) == 0):
        return True
    
    # If it gets down to here, there are
    # employees in the list. So return False.
    return False

def listIsEmpty():
    # Print message that the list is empty,
    # then wait 3 seconds and clear the screen.
    print(f"Sorry, The List Is Empty.")
    time.sleep(3)
    os.system("clear")

def endProgram():
    # Print message that the list is empty,
    # then wait 3 seconds and clear the screen.
    print(f"Normal Program Termination. Good Bye.")
    time.sleep(3)
    os.system("clear")
    exit()
