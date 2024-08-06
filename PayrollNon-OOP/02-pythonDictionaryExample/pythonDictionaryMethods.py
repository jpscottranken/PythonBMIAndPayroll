# pythonDictionaryMethods.py

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
def addNewEmployee(employees):
    employeeNumber = getEmployeeNumber(employees)
    employeeFirstName = getEmployeeFirstName()
    employeeLastName = getEmployeeLastName()
    employeeHoursWorked = getEmployeeHoursWorked()
    employeeHourlyRate = getEmployeeHourlyRate()
    employeeGrossPay = calculateEmployeeGrossPay(employeeHoursWorked, employeeHourlyRate)

    employee = {
                "empFirst":  employeeFirstName, 
                "empLast":   employeeLastName, 
                "empHours":  employeeHoursWorked, 
                "empRate":   employeeHourlyRate, 
                "empGross":  employeeGrossPay}
    
    employees[employeeNumber] = employee
    print(f"Employee #{employeeNumber} was added to the employee dictionary")

# Input employee number. Number cannot be a duplicate,
# i.e. there cannot be an existing employee with this number.
def getEmployeeNumber(employees):
    while True:
        try:
            empNumber = int(input("Enter an employee number (must be unique):\t"))
            if empNumber == "" or empNumber in employees:
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

# Clear the employee dictionary
def clearEmployeeDictionary(employees):
  if employees:
    employees.clear()
    print("\nThe Employee Dictionary Has Been Cleared!")
  else:
     dictionaryIsEmpty()

# Create and return a copy of the employee dictionary
def copyEmployeeDictionary(employees):
  if employees:
    return employees.copy()
  else:
    dictionaryIsEmpty()

# Give a count of the number of employees in
# the employee dictionary
def countEmployees(employees):
  if employees:
    print(f"\nThere Are A Total Of {len(employees)} Employees In Our Dictionary!")
  else:
     dictionaryIsEmpty()

# Find an employee based on the inputted 
# employee number
def findEmployee(employees, number):
    if (employees):                             #   dictionary not empty
        employee = employees.get(number)         #   Attempt to find employee
        if (employee):                           #   Associated employee found
            return employee
        else:                                    #   Associated employee not found
            return "\nEmployee Not Found In Dictionary"
    else:
        dictionaryIsEmpty()

# Remove a desired employee from a desired 
# position in the employee list
def removeEmployee(employees, number):
    if employees:                             #   dictionary not empty
        employeeToRemove = employees.pop(number, None) #   Attempt to find employee
        if (employeeToRemove):                   #   Associated employee found
            print(f"\nEmployee # {number} removed from dictionary")
        else:                                    #   Associated employee not found
            return "\nEmployee Not Found In Dictionary"
    else:
        dictionaryIsEmpty()

# Display the current contents of the
# employee list
def displayAllEmployees(employees):
  if employees:
    sleepThenClear()
    print("Here are the contents of the employee dictionary:")
    for empNumber, employee in employees.items():
        print(f"Employee Number: {empNumber}")
        print(f"Employee Name: {employee['empFirst']} {employee['empLast']}")
        print(f"Employee Hours: {employee["empHours"]:.2f}")
        print(f"Employee Rate: ${employee["empRate"]:.2f}")
        print(f"Employee Gross: ${employee["empGross"]:.2f}")
        print("\n")
  else:
    dictionaryIsEmpty()

def dictionaryIsEmpty():
    # Print message that the dictionary is empty,
    # then wait 3 seconds and clear the screen.
    print(f"Sorry, The Dictionary Is Empty.")
    sleepThenClear()

def endProgram():
    # Print message that the list is empty,
    # then wait 3 seconds and clear the screen.
    print(f"Normal Program Termination. Good Bye.")
    sleepThenClear()
    exit()

def sleepThenClear():
    time.sleep(3)
    os.system("clear")

