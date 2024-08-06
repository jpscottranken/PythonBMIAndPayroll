# pythonTupleMethods.py

#import math
import os
import time
import pythonTupleMenu as ptm

# Program constants
MINHOURS =  0.00      # Minimum employee hours worked
MAXHOURS = 84.00      # Maximum employee hours worked
MINHRATE =  0.00      # Minimum employee hourly rate
MAXHRATE = 99.99      # Maximum employee hourly rate
MAXNONOT = 40.00      # Minimum employee straight (non-OT) hours
MINWAGE  = 15.00      # Arbitrary value chosen for minimum wage

#   Verify that all employee numbers for each 
#   tuple record are indeed unique.
def areAllEmployeeNumbersUnique(employees):
    employeeNumbers = tuple(emp[0] for emp in employees)
    if (len(employeeNumbers) != len(set(employeeNumbers))):
        raise ValueError(f"Each Employee Number Must Be Unique")
    
    #   No error was raised. So, there were no non-unique
    #   employee numbers (each was indeed unique). So,
    #   print out a message stating this.
    print(f"\nAll Employee Numbers ARE Unique!")

#   Verify that all employee first names and
#   last names for each tuple record are NOT empty.
def areAnyEmployeeFirstOrLastNamesEmpty(employees):
    for emp in employees:
        if not emp[1] or not emp[2]:
            raise ValueError("Employee first name and last name cannot be empty!")

    #   No error was raised. So, there were empty
    #   employee last names or first names. So,
    #   print out a message stating this.
    print(f"\nAll Employee First Names And Last Names ARE Not Empty!")

#   Verify that all employee hours worked and
#   all employee hourly rates are within specified ranges.
def areAllHoursWorkedAndHourlyRatesWithinRange(employees):
    for emp in employees:
        if not MINHOURS <= emp[3] <= MAXHOURS:
            #   If true, out of range value entered for hours worked
            raise ValueError(f"Employee Hours Must Be Between {MINHOURS} and {MAXHOURS}")
        if not MINHRATE <= emp[4] <= MAXHRATE:
            #   If true, out of range value entered for hourly rate
            raise ValueError(f"Employee Hours Must Be Between {MINHRATE} and {MAXHRATE}")

    #   No error was raised. So, both the
    #   hours worked and hourly rate were
    #   within the acceptable ranges. So,
    #   print out a message stating this
    #   for each field.
    print("\nAll Employee Hours Worked ARE Within Range")
    print("\nAll Employee Hourly Rates ARE Within Range")

#   Find the number of employees who have worked overtime (> 40)
def countNumberOfEmployeesWorkingOvertime(employees):
    overtimeEmployees = [emp for emp in employees if emp[3] > MAXNONOT]
    print(f"\nNumber Of Employees Working Overtime: {len(overtimeEmployees)}!")
    
    print(f"\nThe names/hours of these employees are:")
    for emp in overtimeEmployees:
        print(f"Name: {emp[1]} {emp[2]}\tHours: {emp[3]:.2f}")

#   Find the number of employees who have not worked overtime (<= 40)
def countNumberOfEmployeesNotWorkingOvertime(employees):
    nonOvertimeEmployees = [emp for emp in employees if emp[3] <= MAXNONOT]
    print(f"\nNumber Of Employees NOT Working Overtime: {len(nonOvertimeEmployees)}!")
    
    print(f"\nThe names/hours of these employees are:")
    for emp in nonOvertimeEmployees:
        print(f"Name: {emp[1]} {emp[2]}\tHours: {emp[3]:.2f}")

#   Number of employees making >= MINWAGE (15.00)
def countNumberOfEmployeesMakingMinimumWageOrAbove(employees):
    minWageOrAboveEmployees = [emp for emp in employees if emp[4] >= MINWAGE]
    print(f"\nNumber Of Employees making minimum wage or above: {len(minWageOrAboveEmployees)}!")
    
    print(f"\nThe names/hourly rate of these employees are:")
    for emp in minWageOrAboveEmployees:
        print(f"Name: {emp[1]} {emp[2]}\tHourly Rate: ${emp[4]:.2f}")

#   Number of employees  making < MINWAGE (15.00)
def countNumberOfEmployeesNotMakingMinimumWage(employees):
    belowMinWageEmployees = [emp for emp in employees if emp[4] < MINWAGE]
    print(f"\nNumber Of Employees making less than the minimum wage: {len(belowMinWageEmployees)}!")
    
    print(f"\nThe names/hourly rate of these employees are:")
    for emp in belowMinWageEmployees:
        print(f"Name: {emp[1]} {emp[2]}\tHourly Rate: ${emp[4]:.2f}")

#   Find the employee with the largest employee number
def indexOfEmployeeWithHighestEmployeeNumber(employees):
    indexHighestEmployeeNumber = max(range(len(employees)), key=lambda i: employees[i][0])
    highestEmpNumberEmp = employees[indexHighestEmployeeNumber]
    print(f"\nEmployee with highest employee number:\nName: {highestEmpNumberEmp[1]} {highestEmpNumberEmp[2]}\tEmployee Number: {highestEmpNumberEmp[0]}")

#   Find the employee with the largest hourly rate
def indexOfEmployeesWithHighestHourlyRate(employees):
    indexHighestHourlyRate = max(range(len(employees)), key=lambda i: employees[i][3])
    highestHourlyRate = employees[indexHighestHourlyRate]
    print(f"\nEmployee with highest hourly rate:\nName: {highestHourlyRate[1]} {highestHourlyRate[2]}\tHourly Rate: {highestHourlyRate[4]}")

#   Find the employee working the most hours
def indexOfEmployeesWorkingMostHours(employees):
    indexMostHours = max(range(len(employees)), key=lambda i: employees[i][3])
    mostHours = employees[indexMostHours]
    print(f"\nEmployee with highest hours worked:\nName: {mostHours[1]} {mostHours[2]}\tHours Worked: {mostHours[3]}")

#   Find the employee with the largest gross pay
def indexOfEmployeeWithLargestGrossPay(employees):
    indexLargestGrossPay = max(range(len(employees)), key=lambda i: employees[i][5])
    largestGross = employees[indexLargestGrossPay]
    print(f"\nEmployee with highest hourly rate:\nName: {largestGross[1]} {largestGross[2]}\tLargest Gross Pay: ${largestGross[5]:.2f}")

#   Find all employees working overtime
def indexesOfEmployeesWorkingOvertime(employees):
    indexOvertimeEmployees = [i for i in range(len(employees)) if employees[i][3] > MAXNONOT]
    print(f"\nIndex of employees who worked overtime: {indexOvertimeEmployees}")
    for i in indexOvertimeEmployees:
        print(f"Name: {employees[i][1]} {employees[i][2]}\tHours: {employees[i][3]:.2f}")
    
def endProgram():
    # Print message that the list is empty,
    # then wait 3 seconds and clear the screen.
    print(f"Normal Program Termination. Good Bye.")
    sleepThenClear()
    exit()

def sleepThenClear():
    time.sleep(3)
    os.system("clear")
