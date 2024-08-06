# Add the 2 numbers together
def add2(n1, n2):
  return n1 + n2

# Subtract second number from first
def subtract2(n1, n2):
  return n1 - n2

# Multiply first number by second
def multiply2(n1, n2):
  return n1 * n2

# Divide first number by second
def divide2(n1, n2):
  #return n1 / n2
  return(checkForDivideByZero(n1, n2, 1))

# Divide first number by second
# "throw away" any remainder
def intDivide2(n1, n2):
  #return n1 // n2
  return(checkForDivideByZero(n1, n2, 2))

# Divide first number by second
# display remainder
def mod2(n1, n2):
  #return n1 % n2
  return(checkForDivideByZero(n1, n2, 3))

# Raise first number to second number
def expo2(n1, n2):
  return n1 ** n2

# For division and/or mod operations, if the
# second number is a 0, raise a
def checkForDivideByZero(n1, n2, value):
  result = 0
  if (n2 != 0):
    match(value):
      case 1:
        result = round(n1 / n2, 2)    # floating point divide
      case 2:
        result = n1 // n2             # integer by integer divide
      case 3:
        result = n1 % n2              # modulo (remainder only)
  else:   
      result = 'Divide By 0 Is Not Possible'
  return result
