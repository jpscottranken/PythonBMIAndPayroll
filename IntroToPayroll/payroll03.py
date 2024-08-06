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

def main():
  # Clear the cache
  importlib.invalidate_caches()

  firstName = ""
  # Input until valid (non-blank) first name is input
  while (firstName == ""):
    firstName = inputFirstName(f"Please enter first name:\t\t\t")

  lastName  = ""
  # Input until valid (non-blank) last name is input
  while (lastName == ""):
    lastName = inputLastName(f"Please enter last name:\t\t\t\t")

  hoursWorked  = float(0.0)
  # Input until valid (non-blank, numeric, in range) hours worked is input
  while (hoursWorked  == float(0.0)):
    hoursWorked = inputHoursWorked(f"Please enter hours worked between {MINHOURS} and {MAXHOURS}:\t")

  hourlyRate   = float(0.0)
  # Input until valid (non-blank, numeric, in range) hourly rate is input
  while (hourlyRate  == float(0.0)):
    hourlyRate  = inputHourlyRate(f"Please enter hourly rate between {MINHRATE} and {MAXHRATE}:\t")

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
      # Normal program termination
      print ("Program Ending Normally. Good Bye")
      time.sleep(3)
      os.system("clear")
      exit()
  else:
    main()

def inputFirstName(prompt):
  userInput = input(prompt)

  try:
    # First Name Input Validation
    if (userInput == ""): # Validation Failed, i.e., No firstName input
      raise ValueError
    else:                 # Validation Succeeded, i.e., firstName input
      return userInput
  except ValueError:
    print (f"Invalid Input For First Name. Please Reenter.")
    return ""

def inputLastName(prompt):
  userInput = input(prompt)

  try:
    # Last Name Input Validation
    if (userInput == ""): # Validation Failed, i.e., No lastName input
      raise ValueError
    else:                 # Validation Succeeded, i.e., lastName input
      return userInput
  except ValueError:
    print (f"Invalid Input For Last Name. Please Reenter")
    return ""

def inputHoursWorked(prompt):
  userInput  = input(prompt)

  try:
    '''
      There are four possible error conditions below:
    
      1.  userInput could be blank.
      2.  userInput could be non-numeric.
      3.  userInput could be out-of-range 1 (< 0).
      4.  userInput could be out-of-range 2 (> 84).
    '''
    if (userInput == ""):
      print (f"No Input For Hours Worked. Please Try Again.")
      return float(0.0)
    elif (math.isnan(float(userInput)) or
        float(userInput) < MINHOURS or float(userInput) > MAXHOURS):
      raise ValueError
    else:
      return float(userInput)
  except ValueError:
    print (f"Invalid Input For Hours Worked. Please Reenter.")
    return float(0.0)

def inputHourlyRate(prompt):
  userInput  = input(prompt)

  try:
    '''
      There are four possible error conditions below:
    
      1.  userInput could be blank.
      2.  userInput could be non-numeric.
      3.  userInput could be out-of-range 1 (< 0).
      4.  userInput could be out-of-range 2 (> 99.99).
    '''
    if (userInput == ""):
      print (f"No Input For Hourly Rate. Please Try Again.")
      return float(0.0)
    elif (math.isnan(float(userInput)) or
        float(userInput) < MINHRATE or float(userInput) > MAXHRATE):
      raise ValueError
    else:
      return float(userInput)
  except ValueError:
    print (f"Invalid Input For Hourly Rate. Please Reenter.")
    return float(0.0)

def calculateGrossPay(hw, hr):
  gross = 0.0

  # If employee worked <= 40 hours (MAXNONOT), pay straight time (no OT worked)
  if (hw <= MAXNONOT):
    gross = hw * hr
  # Employee has worked some OT. Gross should include OT pay
  else:
    gross = (MAXNONOT * hr) + ((hw - MAXNONOT) * hr * OTRATE)

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

main()                          # Call main() at program start

