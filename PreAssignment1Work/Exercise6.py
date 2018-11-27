#-----------------------------------------------------------------------------
# Name:        Exercise 6 (Exercise6.py)
# Purpose:     Using functions
#
# Author:      vonlugersbutter
# Created:     Wednesday, October 24, 2018
# Updated:     Thursday, October 25, 2018
#-----------------------------------------------------------------------------

def convertCToF(celsius1):
  ''' 
  Converts integer Centigrade values to Fahrenheit
  
  '''
  if -100<=int(celsius1)<=100:
    fahrenheit1 = 1.8*celsius1 + 32
    return int(fahrenheit1)
  
  else:
    return 'Unacceptable input values.'
    
print (convertCToF(-40))

def convertFToC(fahrenheit2):
  ''' 
  Converts integer Fahrenheit values to Centigrade
  
  '''
  if -100<=int(fahrenheit2)<=100:
    celsius2 = (fahrenheit2 - 32) * (5/9)
    return int(celsius2)
  
  else:
    return 'Unacceptable input values.'
    
print (convertFToC(-40))

def hypotenuse(leg_a, leg_b):
  '''
  Finds hypotenuse from leg values using Pythagorean Theorem
  '''
  if (leg_a>0) and (leg_b>0):
    hypotenuse_value = ((leg_a)**2 + (leg_b)**2)**0.5
    return float(hypotenuse_value)
  
  else:
    return 'Unacceptable input values.'

print (hypotenuse(3,4))

def convertCToFEveryFive(lowC, highC):
  '''
  Outputs table of values based on Celsius to Fahrenheit conversion
  '''
  if lowC<highC:
    for lowC in range(lowC,highC+1,5):
      print(str(lowC) + "C = " + str(int(1.8*(lowC) + 32)) + "F")
    return ''

  else:
    return ('Unacceptable input values.')

print (convertCToFEveryFive(-10,20))
