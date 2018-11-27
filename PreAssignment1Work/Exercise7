#-----------------------------------------------------------------------------
# Name:        Exercise 7 (Exercise7.py)
# Purpose:     Using documentation
#
# Author:      vonlugersbutter
# Created:     Thursday, October 25, 2018
# Updated:     Tuesday, November 6, 2018
#-----------------------------------------------------------------------------

def convertCToF(celsius):
  ''' 
  Converts integer Centigrade values to Fahrenheit
  
  Takes in Centigrade values, between the values of -100 and 100, and prints its respective Fahrenheit value using a conversion formula
  
  Parameters
  ----------
  celsius : integer
    The inputted or chosen Centigrade value, which is converted
  
  Returns
  ----------
  integer
    The Fahrenheit value of the chosen or inputted Centigrade value
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  
  if -100<=int(celsius)<=100:             # does not accept values outside of restrictions
    fahrenheit = 1.8*celsius + 32         # uses formula to convert celsius value to fahrenheit, which is set as a local variable
    return int(fahrenheit)                # returns the fahrenheit value
  
  else:
    return 'Unacceptable input values.'   # if the parameter is outside of the given restriction, it is not accepted
    
# function was defined above, and is executed here so the program runs
print (convertCToF(-40))

#-----------------------------------------------------------------------------

def convertFToC(fahrenheit):
  ''' 
  Converts integer Fahrenheit values to Centigrade
  
  Takes in Fahrenheit values, between the values of -100 and 100, and prints its respective Centigrade value using a conversion formula
  
  Parameters
  ----------
  fahrenheit : integer
    The inputted or chosen Fahrenheit value, which is converted
  
  Returns
  ----------
  integer
    The Centigrade value of the chosen or inputted Fahrenheit value
    
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
 
  if -100<=int(fahrenheit)<=100:          # ensures that the parameter is within an acceptable range
    celsius = (fahrenheit - 32) * (5/9)   # processes given fahrenheit value and computes celsius value, which is set as a local variable
    return int(celsius)                   # returns the celsius value
  
  else:
    return 'Unacceptable input values.'   # does not accept input values outside of the given range

# executes function here, as everything above was defining the function
print (convertFToC(-40))

#-----------------------------------------------------------------------------

def hypotenuse(leg_a, leg_b):
  '''
  Finds hypotenuse from leg values using Pythagorean Theorem
  
  Calculates the hypotenuse of a right triangle using Pythagorean's theorem and given leg values, and returns the hypotenuse to the sender
  
  Parameters
  ----------
  leg_a : float
    A leg of the given right triangle
    
  leg_b : float
    The other leg of the right angled triangle
  
  Returns
  ----------
  float
    The value of the hypotenuse of the given right triangle
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  
  if (leg_a>0) and (leg_b>0):                           # ensures that the given values are not negative or zero, since this is a triangle
    hypotenuse_value = ((leg_a)**2 + (leg_b)**2)**0.5   # computes hypotenuse with Pythagorean Theorem, and sets it as a variable
    return float(hypotenuse_value)                      # returns the hypotenuse value of the 2 given legs
  
  else:
    return 'Unacceptable input values.'                 # does not accept negative or zero values, as they are not in the domain of the situation

# actually runs the program for this function, since above was the definition of the function
print (hypotenuse(3,4))

#-----------------------------------------------------------------------------

def convertCToFEveryFive(lowC, highC):
  '''
  Outputs table of values based on Celsius to Fahrenheit conversion
  
  Two Centigrade values are inputted, with the lower one inputted before the higher one
  The first Centigrade value is returned beside its respective Fahrenheit value, using a conversion formula
  The Centigrade value increases by 5, and continues to show Fahrenheit values, until the Centigrade value reaches the higher Centigrade given
  
  Parameters
  ----------
  lowC : integer
    The inputted lower Centigrade value, which begins the table of outputs 
    
  highC : integer
    The inputted higher Centigrade value, which ends the table of outputs
    
  Returns
  ----------
  string
    Note that the return is blank, because return cannot be placed in a for loop without displaying "None"
    The table of values is printed. 
  
  string
    If inputted values do not meet the given limitations, display Unacceptable input values
  '''
  if lowC<highC:                                                    # the table must run from low to high, which is impossible if lowC is higher than highC
    for lowC in range(lowC,highC+1,5):                              # finds values from lowC to highC as it adds 5 each time
      print(str(lowC) + "C = " + str(int(1.8*(lowC) + 32)) + "F")   # prints string of both celsius value and its corresponding Fahrenheit value
    return ''                                                       # blank return; return cannot be processed inside of a for loop

  else:
    return ('Unacceptable input values.')                           # if the lowC is higher than highC, the table cannot be made, and input is not accepted

# runs the function for values of -10C to 20C
print (convertCToFEveryFive(-10,20))

#-----------------------------------------------------------------------------
