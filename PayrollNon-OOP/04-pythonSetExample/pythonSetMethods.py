#   pythonSetMethods.py

import pythonSetMenu as psm
import os
import time 

#   Constants
MAXNONOTHOURS  = 40.00
WELLPAIDWORKER = 20.00

#   Create two global sets:
#   overtimeWorkers will be all workers with hoursWorked >  MAXNONOTHOURS
#   wellpaidWorkers will be all workers with hourlyRate  >= WELLPAIDWORKER/hour
overtimeWorkers = set()
wellpaidWorkers = set()

def showSetsForMethodExamples(employees):
    global overtimeWorkers, wellpaidWorkers

    #   Set comprehension to get overtime workers
    overtimeWorkers = {ot for ot in employees if ot[3] > MAXNONOTHOURS}

    #   Set comprehension to get wellpaid workers
    wellpaidWorkers = {wp for wp in employees if wp[4] >= WELLPAIDWORKER}

    print("\nHere is the list of well-paid workers")
    for wp in wellpaidWorkers:
        print(wp)

    print("\nHere is the list of overtime workers")
    for ot in overtimeWorkers:
        print(ot)

    print("\n\n")

def addExample():
    print(f"\nThe add() option is not provided in this program.")

def clearExample():
    print(f"\nThe clear() option is not provided in this program.")
    #   employees.clear()
    #   overtimeWorkers.clear()
    #   wellpaidWorkers.clear()

def copyExample(employees):
    global overtimeWorkers, wellpaidWorkers
    print(f"\nMaking copies of the employee, overtimeWorker, and wellpaidWorkers sets.")
    print(f"\nemployees Set Copy: {employees.copy()}")
    print(f"\novertimeWorkers Set Copy: {overtimeWorkers.copy()}")
    print(f"\nwellpaidWorkers Set Copy: {wellpaidWorkers.copy()}")

def differenceExample():
    global overtimeWorkers, wellpaidWorkers
    differenceWorkers = wellpaidWorkers.difference(overtimeWorkers)
    print(f"\nDifference Workers: {differenceWorkers}")

def difference_updateExample():
    global overtimeWorkers, wellpaidWorkers
    #differenceUpdateWorkers = wellpaidWorkers.difference_update(overtimeWorkers)
    wellpaidWorkers.difference_update(overtimeWorkers)
    print(f"\nDifference Update Workers: {wellpaidWorkers}")

def discardExample():
    #   https://www.geeksforgeeks.org/python-__iter__-__next__-converting-object-iterator/
    global wellpaidWorkers
    print(f"\nThe Original wellpaidWorkers set: {wellpaidWorkers}")
    employeeToDiscard = next(iter(wellpaidWorkers))
    wellpaidWorkers.discard(employeeToDiscard)
    print(f"\nThe wellpaidWorkers set after employeeToDiscard: {wellpaidWorkers}")

def intersectionExample():
    global overtimeWorkers, wellpaidWorkers
    intersectionWorkers = wellpaidWorkers.intersection(overtimeWorkers)
    print(f"\nThe intersectionWorkers: {intersectionWorkers}")

def intersection_updateExample():
    global wellpaidWorkers, overtimeWorkers
    wellpaidWorkers.intersection_update(overtimeWorkers)
    print(f"\nwellpaidWorkers after intersection_update: {wellpaidWorkers}")

def isdisjointExample():
    global wellpaidWorkers, overtimeWorkers
    print(f"\nAre wellpaidWorkers and overtimeWorkers disjoint? {wellpaidWorkers.isdisjoint(overtimeWorkers)}")

def issubsetExample():
    global wellpaidWorkers, overtimeWorkers
    print(f"\nIs wellpaidWorkers a subset of overtimeWorkers? {wellpaidWorkers.issubset(overtimeWorkers)}")

def issupersetExample():
    global wellpaidWorkers, overtimeWorkers
    print(f"\nIs wellpaidWorkers a superset of overtimeWorkers? {wellpaidWorkers.issuperset(overtimeWorkers)}")

def popExample():
    global overtimeWorkers
    print(f"\nOriginal overtimeWorkers set before removal: {overtimeWorkers}")
    removedEmployee = overtimeWorkers.pop()
    print(f"Removed overtimeWorkers: {removedEmployee}")
    print(f"overtimeWorkers set after removal: {overtimeWorkers}")

def removeExample():
    global wellpaidWorkers
    print(f"\nThe Original wellpaidWorkers set: {wellpaidWorkers}")
    employeeToRemove = next(iter(wellpaidWorkers))
    wellpaidWorkers.discard(employeeToRemove)
    print(f"\nThe wellpaidWorkers set after employeeToRemove: {wellpaidWorkers}")

def symmetric_differenceExample():
    global wellpaidWorkers, overtimeWorkers
    symmetricDifferenceWorkers = wellpaidWorkers.symmetric_difference(overtimeWorkers)
    print(f"\nSymmetric Difference Workers: {symmetricDifferenceWorkers}")
    
def symmetric_difference_updateExample():
    global wellpaidWorkers, overtimeWorkers
    symmetricDifferenceUpdateWorkers = overtimeWorkers.symmetric_difference_update(wellpaidWorkers)
    print(f"\nSymmetric Difference Workers: {symmetricDifferenceUpdateWorkers}")

def unionExample():
    global wellpaidWorkers, overtimeWorkers
    unionOfWellpaidAndOvertimeWorkers = wellpaidWorkers.union(overtimeWorkers)
    print(f"Union Of wellpaidWorkers and overtimeWorkers is: {unionOfWellpaidAndOvertimeWorkers}")

def updateExample():
    global wellpaidWorkers, overtimeWorkers
    wellpaidWorkers.update(overtimeWorkers)
    print(f"wellpaidWorkers after update is: {wellpaidWorkers}")
    
def endProgram():
    # Print message that the list is empty,
    # then wait 3 seconds and clear the screen.
    print(f"\nNormal Program Termination. Good Bye.")
    sleepThenClear()
    exit()

def sleepThenClear():
    time.sleep(3)
    os.system("clear")
