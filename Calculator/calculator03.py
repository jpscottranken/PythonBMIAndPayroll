"""
The calculator02.py program demonstrates:
1.  import
2.  as
3.  if
4.  def
5.  return
6.  print
7.  str
8.  try
9.  except
10. finally
11. multiline Python comments (""" """)
12. modules

To clear the terminal, I used this URL:

https://stackoverflow.com/questions/48713604/how-can-i-clear-the-terminal-in-visual-studio-code

This program is a "redo" of sorts of the calculator01.py program
that was done in the Keywords GitHub repository, located at URL:

https://github.com/jpscottranken/Keywords

Changes Made:

1.  Added multiline comments.

2.  Added exception handling with try except and finally.

    This exception handling made sure that if the user
    attempt to floating point divide or integer divide or
    modulo by 0, a ValueError exception would be thrown
    and the result would be set to Divide By 0 Is Not Possible.

    Also, if the user inputs non-numeric values for either
    number1 or number2, s/he will get an error message and
    be asked to re-input.

3.  Replaced the computer-generated number1 and number2
    (created via a call to the Python random number generator)
    with input statements which let the user input the values
    she/he wanted for number1 and number2
"""

import numpy as np
import jpsMath as jps

# Create two variables. Each is a 
# random number between 1 and 100.
#number1 = np.random.randint(1,100)
#number2 = np.random.randint(1,100)

def get_and_validate_numeric_input(prompt):
  while True:    
    user_input = input(prompt)
    try:
        # Attempt to convert input to a float
        numeric_value = float(user_input)
        return numeric_value
    except ValueError:
        # If conversion fails, inform user, prompt again
        print("Invalid input. Please enter a numeric value.")

    finally:
      print('This will print regardless success or failure above.')

# Prompt for the two values to be used in the calculations
number1 = get_and_validate_numeric_input('Enter first numeric value: ')
number2 = get_and_validate_numeric_input('Enter second numeric value: ')

# Set two temporary variables
temp1 = number2
temp2 = number1

"""
If necessary (number1 < number2),
flip the values, i.e. put the
original value of number1 into
number2 and the original value
of number2 into number1
"""
if(number1 < number2):
  number1 = temp1
  number2 = temp2

# Call the calculator functions above
print(str(number1) + ' + '  + str(number2) + ' = ' + str(jps.add2(number1, number2)))
print(str(number1) + ' - '  + str(number2) + ' = ' + str(jps.subtract2(number1, number2)))
print(str(number1) + ' * '  + str(number2) + ' = ' + str(jps.multiply2(number1, number2)))
print(str(number1) + ' / '  + str(number2) + ' = ' + str(jps.divide2(number1, number2)))
print(str(number1) + ' // ' + str(number2) + ' = ' + str(jps.intDivide2(number1, number2)))
print(str(number1) + ' % '  + str(number2) + ' = ' + str(jps.mod2(number1, number2)))
print(str(number1) + ' ** ' + str(number2) + ' = ' + str(jps.expo2(number1, number2)))
