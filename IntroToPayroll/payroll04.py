# Gleaned from the following URL:
# https://stackoverflow.com/questions/320929/currency-formatting-in-python
import locale           # For currency symbol (US - $)
locale.setlocale( locale.LC_ALL, '' )
import importlib        # For clearing cache
import math             # For math.isnan (is not a number)
import os               # For os.system("clear) for clearing the screen
import time             # For setting a timer

# Global Constants
MINHOURS =  0.00  # Minimum hours an employee can work
MAXHOURS = 84.00  # Maximum hours an employee can work
MINHRATE =  0.00  # Minimum employee hourly rate
MAXHRATE = 99.99  # Maximum employee hourly rate
MAXNONOT = 40.00  # Maximum employee hours for no overtime
OTRATE   =  1.50  # Overtime rate

# Global Variables
totalEmployees  = 0           # Total number of employees
highestGrossPay =      -1.00  # Highest employee gross amount
lowestGrossPay  = 1000000     # Lowest  employee gross amount
averageGrossPay =       0.00  # Average employee gross amount
totalGrossPay   =       0.00  # Total all employees gross amount

def main():
  # Clear the cache
  importlib.invalidate_caches()

  firstName = ""
  # Input until valid (non-blank) first name is input
  while (firstName == ""):
    firstName = inputFirstOrLastName(f"Please enter first name:\t\t\t", 1)

  lastName  = ""
  # Input until valid (non-blank) last name is input
  while (lastName == ""):
    lastName = inputFirstOrLastName(f"Please enter last name:\t\t\t\t", 2)

  hoursWorked  = float(0.0)
  # Input until valid (non-blank, numeric, in range) hours worked is input
  while (hoursWorked  == float(0.0)):
    hoursWorked = inputHoursWorkedOrHourlyRate(f"Please enter hours worked between {MINHOURS} and {MAXHOURS}:\t", 1)

  hourlyRate   = float(0.0)
  # Input until valid (non-blank, numeric, in range) hourly rate is input
  while (hourlyRate  == float(0.0)):
    hourlyRate  = inputHoursWorkedOrHourlyRate(f"Please enter hourly rate between {MINHRATE} and {MAXHRATE}:\t", 2)

  grossPay = float(0.0)
  # We now have a valid hoursWorked and a valid hourlyRate
  # So, call calculateGrossPay to calculate the gross pay.
  # Do take OT or non-OT into account when doing this calculation.
  grossPay = calculateGrossPay(hoursWorked, hourlyRate)

  # Print out firstName, lastName, hoursWorked,
  # hourlyRate, and grossPay for this employee.
  printEmployeeInfo(firstName, lastName,
                    hoursWorked, hourlyRate, grossPay)
  
  # Allow user to run program again if desired
  again = runProgramAgain()

  if (again == False):   # if (again == False)
    printOutFinalTotals()
    quitProgram()
  else:
    main()

def inputFirstOrLastName(prompt, number):
  theName   = ""
  userInput = input(prompt)

  if (number == 1):    #  First Name
    theName = "First"
  elif (number == 2):  #  Last Name
    theName = "Last"

  try:
    # First Name Input Validation
    if (userInput == ""): # Validation Failed, i.e., No name input
      print (f"No Input For {theName} Name. Please Reenter.")
      return ""
    
    else:                 # Validation Succeeded, i.e., name input
      return userInput
  except ValueError:
    print (f"No Input For {theName} Name. Please Reenter.")
    return ""

def inputHoursWorkedOrHourlyRate(prompt, number):
  userInput  = input(prompt)

  theType = ""
  min     = float(0.0)
  max     = float(0.0)

  if (number == 1):     # Hours Worked
    theType = "Hours Worked"
    min     = MINHOURS
    max     = MAXHOURS
  elif (number == 2):   # Hourly Rate
    theType = "Hourly Rate"
    min     = MINHRATE
    max     = MAXHRATE

  try:
    '''
      There are four possible error conditions below:
    
      1.  userInput could be blank.
      2.  userInput could be non-numeric.
      3.  userInput could be out-of-range 1 (< MIN).
      4.  userInput could be out-of-range 2 (> MAX).
    '''
    if (userInput == ""):
      print (f"No Input For {theType}. Please Try Again.")
      return float(0.0)
    elif (math.isnan(float(userInput)) or
        float(userInput) < min or float(userInput) > max):
      raise ValueError
    else:
      return float(userInput)
  except ValueError:
    print (f"Invalid Or Out-Of-Range Input For {theType}. Please Reenter.")
    return float(0.0)

def calculateGrossPay(hw, hr):
  global lowestGrossPay, highestGrossPay
  global totalEmployees, averageGrossPay
  global totalGrossPay
  gross = 0.0

  # Increment totalEmployees counter
  totalEmployees += 1

  # If employee worked <= 40 hours (MAXNONOT), pay straight time (no OT worked)
  if (hw <= MAXNONOT):
    gross = hw * hr
  # Employee has worked some OT. Gross should include OT pay
  else:
    gross = (MAXNONOT * hr) + ((hw - MAXNONOT) * hr * OTRATE)

  # Check if current gross pay is new highestGrossPay
  if (gross > highestGrossPay):
    # We have a new highestGrossPay
    highestGrossPay = gross

  # Check if current gross pay is new lowestGrossPay
  if (gross < lowestGrossPay):
    # We have a new lowestGrossPay
    lowestGrossPay = gross

  # Add current gross pay to totalGrossPay accumulator
  totalGrossPay += gross

  return gross

def printEmployeeInfo(fn, ln, hw, hr, gp):
  print (f"NAME:\t\t{fn} {ln}")
  print (f"HOURS WORKED:\t{hw}")
  print (f"HOURLY RATE:\t{locale.currency(hr)}")
  print (f"GROSS PAY:\t{locale.currency(gp)}")

# Allow the user to run the program again if desired
# or end the program run now if not desired
def runProgramAgain():
  doAgain = input("Run Program Again? Enter a Y or N Please:\t")

  # Handle the user just hitting the <enter> key
  if (doAgain == ""):
    time.sleep(3)
    os.system("clear")

    main()
  # Assume user entered something like Y or N or Yes or No, etc.
  else:
    yesOrNo = doAgain.upper()   # UPPERCASE user input
    firstChar = yesOrNo[0]      # Grab just first character of user input
    if (firstChar != "Y"):      # User DOES NOT wish to run program again
      return False
    else:                       # User DOES wish to run program again
      time.sleep(3)
      os.system("clear")
      return True

def printOutFinalTotals():
  global lowestGrossPay, highestGrossPay
  global totalEmployees, averageGrossPay
  global totalGrossPay
  # Calculate the average gross pay
  averageGrossPay = totalGrossPay / totalEmployees
  print (f"LOWEST  GROSS PAY:\t\t{locale.currency(lowestGrossPay)}")
  print (f"HIGHEST GROSS PAY:\t\t{locale.currency(highestGrossPay)}")
  print (f"AVERAGE GROSS PAY:\t\t{locale.currency(averageGrossPay)}")
  print (f"TOTAL   GROSS PAY:\t\t{locale.currency(totalGrossPay)}")

def quitProgram():
  # Normal program termination
  print ("Program Ending Normally. Good Bye")
  time.sleep(6)
  os.system("clear")
  exit()
  
main()                          # Call main() at program start
