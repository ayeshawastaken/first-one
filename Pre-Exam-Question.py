#-----------------------------------------------------------------------------
# Name: Pre-Exam Question (Pre-Exam-Question.py)
# Purpose: Displaying understanding of conventions and interpreting errors
#
# Author: vonlugersbutter
# Created: Tuesday, January 22, 2019
# Updated: Tuesday, January 22, 2019
#-----------------------------------------------------------------------------

import logging
logging.basicConfig(filename='debug.txt', filemode='w',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def volume_of_cone(radius, height):
  '''
  Calculates the volume of a cone using its radius and height

  Computes the volume of a cone using its inputted radius and height. It then returns the volume value.

  Parameters
	----------
	radius : float 
	  Radius of the base of the given cone 
	height : float 
	  Height of the center of the base of the cone to the upper tip of the cone

	Returns
	-------
	float
	  The volume of the given cone

  Raises
	------
	TypeError
	  If the user inputs a radius that is not a number
	  If the user inputs a height that is not a number
	  If the returned volume is not a number
	ValueError
		If the user inputs a number that is non-positive
		If the returned volume is non-positive
	Exception
	  If the volume calculation goes awry
  	'''
  
  logging.debug('Beginning of function.')
  
  logging.debug('Radius before adjustment: ' + str(radius))
  logging.debug('Height before adjustment: ' + str(height))
  
  # assert isinstance(radius, float), 'Expecting a float for radius'
  # assert isinstance(radius, float), 'Expecting a float for radius'
  
  try: 
    if not isinstance(radius, (int, float)):
      raise TypeError('Radius entered is not a number, as expected.')
    if radius <= 0:
      raise ValueError('Radius value is non-positive.')
  
  except (TypeError,ValueError) as e:
    print("Something went wrong: " + str(e) + " Overriding input to make radius 5.0.")
    radius = 5.0
  
  logging.debug('Radius after adjustment: ' + str(radius))
  
  try: 
    if not isinstance(height, (int, float)):
      raise TypeError('Height entered is not a number, as expected.')
    if height <= 0:
      raise ValueError('Height value is non-positive.')
  
  except (TypeError, ValueError) as e:
    print("Something went wrong: " + str(e) + " Overriding input to make height 5.0.")
    height = 5.0
  
  logging.debug('Height after adjustment: ' + str(height))
  
  pi = 3.141592654
  
  logging.debug("Value of pi, used to compute volume: " + str(pi))
  
  area_of_circle = pi * radius * radius
  
  logging.debug('Area of circle base: ' + str(area_of_circle))
  
  volume = area_of_circle * height / 3.0 
  
  # assert isinstance(radius, float), 'Expecting a float for radius'
  
  logging.debug('Final volume: ' + str(volume))
  
  try:
    if not isinstance(volume, (int, float)):
      raise TypeError('The final computed volume is not a number.')
    if volume <= 0:
      raise ValueError('The final computed volume is non-positive.')
    if volume != (pi*(radius**2)*height /3):
      raise Exception('Volume calculation was invalid.')
    
  except (TypeError, ValueError) as e:
    print("Something went wrong: " + str(e) + " This means something went awry with the calculation.")
  
  logging.debug("End of function.")
  
  return volume


assert_volume = 3.141592654*(2**2)*4 /3

logging.debug("Supposed to be the volume of a cone with radius 2 and height 4: " + str(assert_volume))
assert volume_of_cone(2,4) == assert_volume, 'Expecting a cone with height 4 and radius 2 to have a volume of approximately 17.'

# Start of program here
print(volume_of_cone(5,5))
