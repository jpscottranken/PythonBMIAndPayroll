'''
    Write a Python program that calculates and displays
    a person's body mass index (BMI).  BMI is used to
    determine whether a person is underweight, optimal
    weight, overweight or obese for his or her height
    using the following formula:

    bmi = weight * 703 / (height * height)

    Weight is inputted in lbs. (int) and height is
    inputted in inches (int). For valid input, the
    program should calculate and display the BMI and
    a message indicating whether a person is underweight,
    optimal weight, overweight, or obese for their height
    using these metrics:

    a)	A BMI <  18.5 is considered underweight.
    b)	A BMI >= 18.5 and < 25.0 is considered optimal weight.
    c)	A BMI >= 25.0 and < 30.0 is considered overweight.
    d)	A BMI >= 30.0 is considered obese.  Use constants!

    In addition to above, make sure the program also:

    1.	Assures a valid numeric height between 12 (MINHEIGHT)
        and 96 (MAXHEIGHT) is inputted or an error message is
        displayed. Note: These are arbitrary values.

    2.	Assures a valid numeric weight between 1 (MINWEIGHT)
        and 777 (MAXWEIGHT) is inputted or an error message is
        displayed. Note: These are arbitrary values.

    3.	Lets the user run the program multiple times if/as
        desired.  Keep track of the total number of underweight,
        the total number of optimal weight, the total number of
        overweight, and the total number of obese weight BMIs.
        Output these totals at the end of the program.
'''

# Imported Python Modules
import math
import os
import importlib
import time

# Global constants
MINHEIGHT  =  12        # Minimum allowable height to input
MAXHEIGHT  =  96        # Maximum allowable height to input
MINWEIGHT  =   1        # Minimum allowable weight to input
MAXWEIGHT  = 777        # Maximum allowable weight to input
MINOPTIMAL =  18.5      # Minimum BMI for an optimal weight
MINOVER    =  25.0      # Minimum BMI for an overweight
MINOBESE   =  30.0      # Minimum BMI for an obese weight

# Global variables (accumulators)
totalUnderweight   = 0  # total # underweight people
totalOptimalWeight = 0  # total # optimal weight people
totalOverweight    = 0  # total # overweight people
totalObese         = 0  # total # obese people

# main() - The program "driver"
def main():
  # Clear the cache
  importlib.invalidate_caches()

    # input height
  height = 0
  while (height == 0):
    height = inputHeightOrWeight(f"Input Height Between {MINHEIGHT} and {MAXHEIGHT}:\t", 1)

  # input weight
  weight = 0
  while (weight == 0):
    weight = inputHeightOrWeight(f"Input Weight Between {MINWEIGHT} and {MAXWEIGHT}:\t", 2)

  # We have both a valid height (12 - 96)
  # and a valid weight (1 - 777). So,
  # calculate the BMI
  bmi = calculateBMI(height, weight)

  # calculate BMI status
  bmiStatus = calculateBMIStatus(bmi)

  # print the individual's height, weight, bmi, and bmiStatus
  printIndividualBMIInfo(height, weight, bmi, bmiStatus)

  # ask the user if s/he wants to run the program again
  again = runProgramAgain()

  if (again == False):
    # if no (False),  print the values of each total weight accumulator
    printTotalCounters()
    exit()
  else:
  # if yes, call main() to input height, input weight, etc.
    main()

# Handle inputting height OR weight and
# Validating the entry, i.e. make sure that:
# 1.  The entry is numeric
# 2.  The entry is within range for the height or weight
def inputHeightOrWeight(prompt, number):
  theType   = ""    # Will be set to either "height" or "weight"
  userInput = ""    # Value read in from the prompt
  min       = 0     # Either MINHEIGHT or MINWEIGHT
  max       = 0     # Either MAXHEIGHT or MAXWEIGHT

  userInput = input(prompt)
  try:
    if (number == 1):
      theType = "height"
      min     = MINHEIGHT
      max     = MAXHEIGHT
    elif (number == 2):
      theType = "weight"
      min     = MINWEIGHT
      max     = MAXWEIGHT
  
    # Input validation 1 - Checking for blank or nonnumeric input
    if (userInput == "" or math.isnan(int(userInput))):
      raise ValueError
    # Input validation 2 - Checking out-of-range height or weight
    elif (int(userInput) < min or int(userInput) > max):
      raise ValueError
    else:
      # Input was numeric and within valid range. Return it.
      return int(userInput)  
  except ValueError:
      # If conversion fails, inform user, prompt again
    print (f"Invalid Input For {theType}. Please reenter")
    return 0

def calculateBMI(h, w):
  # Calculate and return the body mass index (BMI)
  # utilizing the formula described earlier.
  return w * 703 / (h * h)

def calculateBMIStatus(bmi):
  # Access to the four global variables
  global totalUnderweight, totalOptimalWeight
  global totalOverweight, totalObese

  # Status (Underweight, Optimal weight, Overweight, or Obese)
  status = ""

  if (bmi < MINOPTIMAL):      # bmi < 18.5
    status = "Underweight"
    totalUnderweight += 1     # Incrment Underweight counter
  elif (bmi < MINOVER):       # bmi >= 18.5 and < 25.0
    status = "Optimal Weight"
    totalOptimalWeight += 1   # Incrment Optimal weight counter
  elif (bmi < MINOBESE):      # bmi >= 25.0 and < 30.0
    status = "Overweight" 
    totalOverweight += 1      # Incrment Overweight counter
  else:                       # bmi >= 30.0
    status = "Obese"
    totalObese += 1           # Incrment Obese counter

  # Return Underweight, Optimal weight, Overweight, or Obese
  return status 

# Print individual's info
def printIndividualBMIInfo(h, w, bmi, st):
  print (f"Height:\t\t {h} inches")
  print (f"Weight:\t\t {w} pounds")
  print (f"BMI:\t\t {round(bmi, 2)}")
  print (f"BMI Status:\t {st}")

# Allow the user to run the program again if desired
# or end the program run now if not desired
def runProgramAgain():
  doAgain = input("Run Program Again? Enter a Y or N Please:\t")

  # Handle the user just hitting the <enter> key
  if (doAgain == ""):
    time.sleep(3)
    os.system("clear")

    main()
  # Assume user entered something like Y or N
  else:
    yesOrNo = doAgain.upper()   # UPPERCASE user input
    firstChar = yesOrNo[0]      # Grab just first character of user input
    if (firstChar != "Y"):      # User DOES NOT wish to run program again
      return False
    else:                       # User DOES wish to run program again
      time.sleep(3)
      os.system("clear")
      return True

def printTotalCounters():
  # Make global variables available to this function
  global totalUnderweight, totalOptimalWeight
  global totalOverweight, totalObese
  print (f"Total Number Underweight    People:\t {totalUnderweight}")
  print (f"Total Number Optimal weight People:\t {totalOptimalWeight}")
  print (f"Total Number Overweight     People:\t {totalOverweight}")
  print (f"Total Number Obese weight   People:\t {totalObese}")
  
main()