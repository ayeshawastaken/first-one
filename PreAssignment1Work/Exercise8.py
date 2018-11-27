#-----------------------------------------------------------------------------
# Name:        Exercise 8 (Exercise8.py)
# Purpose:     Using assertions
#
# Author:      vonlugersbutter
# Created:     Thursday, October 25, 2018
# Updated:     Friday, October 26, 2018
#-----------------------------------------------------------------------------

def convertCToF(celsius1):
  ''' 
  Converts integer Centigrade values to Fahrenheit
  
  Takes in Centigrade values, between the values of -100 and 100, and prints its respective Fahrenheit value using a conversion formula
  
  Parameters
  ----------
  celsius1 : integer
    The inputted or chosen Centigrade value, which is converted
  
  Returns
  ----------
  integer
    The Fahrenheit value of the chosen or inputted Centigrade value
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  if -100<=int(celsius1)<=100:
    fahrenheit1 = 1.8*celsius1 + 32
    return int(fahrenheit1)
  
  else:
    return 'Unacceptable input values.'

# Checks computation of the function
assert convertCToF(-40) == -40, 'The Fahrenheit value for -40 C is -40 F'

# Makes sure the function does not process values that are less than -100 or greater than 100
assert convertCToF(-200) == 'Unacceptable input values.', "Value is not within limitations of the function"

#-----------------------------------------------------------------------------

def convertFToC(fahrenheit2):
  ''' 
  Converts integer Fahrenheit values to Centigrade
  
  Takes in Fahrenheit values, between the values of -100 and 100, and prints its respective Centigrade value using a conversion formula
  
  Parameters
  ----------
  fahrenheit2 : integer
    The inputted or chosen Fahrenheit value, which is converted
  
  Returns
  ----------
  integer
    The Centigrade value of the chosen or inputted Fahrenheit value
    
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  if -100<=int(fahrenheit2)<=100:
    celsius2 = (fahrenheit2 - 32) * (5/9)
    return int(celsius2)
  
  else:
    return 'Unacceptable input values.'

# Checks computation of the function
assert convertFToC(-40) == -40, 'The Centigrade value for -40 F is -40 C'

# Makes sure the function does not process values that are less than -100 or greater than 100
assert convertFToC(-200) == 'Unacceptable input values.', "Value is not within limitations of the function"

#-----------------------------------------------------------------------------

def hypotenuse(leg_a, leg_b):
  '''
  Finds hypotenuse from leg values using Pythagorean Theorem
  
  Calculates the hypotenuse of a right triangle using Pythagorean's theorem and given leg values, and returns the hypotenuse to the sender
  
  Parameters
  ----------
  leg_a: float
    A leg of the given right triangle
    
  leg_b: float
    The other leg of the right angled triangle
  
  Returns
  ----------
  float
    The value of the hypotenuse of the given right triangle
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  if (leg_a>0) and (leg_b>0):
    hypotenuse_value = ((leg_a)**2 + (leg_b)**2)**0.5
    return float(hypotenuse_value)
  
  else:
    return 'Unacceptable input values.'

# Checks computation of the function
assert hypotenuse(3,4) == 5, 'Expecting a triangle with legs 3 and 4 to have a hypotenuse of 5.'

# Makes sure the function does not process values that are negative
assert hypotenuse(-3,-4) == 'Unacceptable input values.', 'Cannot take the hypotenuse of negative side lengths'

#-----------------------------------------------------------------------------

def convertCToFEveryFive(lowC, highC):
  '''
  Outputs table of values based on Celsius to Fahrenheit conversion
  
  Two Centigrade values are inputted, with the lower one inputted before the higher one
  The first Centigrade value is returned beside its respective Fahrenheit value, using a conversion formula
  The Centigrade value increases by 5, and continues to show Fahrenheit values, until the Centigrade value reaches the higher Centigrade given
  
  Parameters
  ----------
  lowC: integer
    The inputted lower Centigrade value, which begins the table of outputs 
    
  highC: integer
    The inputted higher Centigrade value, which ends the table of outputs
    
  Returns
  ----------
  string
    Note that the return is blank, because return cannot be placed in a for loop without displaying "None"
    The table of values is printed. 
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  if lowC<highC:
    for lowC in range(lowC,highC+1,5):
      print(str(lowC) + "C = " + str(int(1.8*(lowC) + 32)) + "F")
    return ''

  else:
    return ('Unacceptable input values.')

convert_table_check = convertCToFEveryFive(-10, 20)

# Makes sure that the returned output is a string
assert isinstance (convert_table_check, str), 'Expects a string in the form of a table'

# The following will break, and is to make sure the function recognizes values correctly
# assert isinstance (convert_table_check, int), 'Expects a string in return'

# Check to make sure the function denies values that are not within limitations
assert convertCToFEveryFive(20,-10) == 'Unacceptable input values.', "The lower value cannot be higher than the higher Centigrade"

#-----------------------------------------------------------------------------
