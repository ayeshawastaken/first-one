#-----------------------------------------------------------------------------
# Name: Exercise 11 (Exercise11.py)
# Purpose: Display understanding of logging, such as raise, try and except, and the logging module
#
# Author: vonlugersbutter
# Created: Saturday, November 24, 2018
# Updated: Tuesday, November 27, 2018
#-----------------------------------------------------------------------------

# Note that some of the tests below have been commented out simply because they make the program stop. Such errors are noted in debug.txt

print(r"                                       /@")
print(r"                       __        __   /\/")
print(r"                      /==\      /  \_/\/  ")
print(r"                    /======\    \/\__ \__")
print(r"                  /==/\  /\==\    /\_|__ \ ")
print(r"               /==/    ||    \=\ / / / /_/")
print(r"             /=/    /\ || /\   \=\/ /     ")
print(r"          /===/   /   \||/   \   \===\ ")
print(r"        /===/   /_________________ \===\ ")
print(r"     /====/   / |                /  \====\ ")
print(r"   /====/   /   |  _________    /  \   \===\    THE LEGEND OF ")
print(r"   /==/   /     | /   /  \ / / /  __________\_____      ______       ___")
print(r"  |===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \ ")
print(r"   \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \ ")
print(r"    \===\__    \   /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \ ")
print(r"     \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \ ")
print(r"      \===\ \  \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |")
print(r"       \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ |")
print(r"        \==\    _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | |")
print(r"         \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | |")
print(r"          \==\ /  / / /________/ |/_________|/_________| /____/   /___\ /___\ ")
print(r"           \==\  /               | /==/")
print(r"            \=\ /________________|/=/    ")
print(r"             \==\     _____      /==/ ")
print(r"            / \===\   \   /    /===/")
print(r"           / / /\===\  \_/  /===/")
print(r"          / / /   \====\ /====/")
print(r"         / / /      \===|===/")
print(r"         |/_/         \===/")
print(r"                        =  ")

name = input("I forget again. Forgive me, hero. What is your name? ")
print()

import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

print("Ah, " + name + ". It is good to see you again. Go now, to Hyrule. \n")

import time

time.sleep(3)

print("Erica: " + name + "!! I need you to help me with math homework, quickly! \n")

print("a. Ok, I'll help.")
print("b. Leave me alone. I need to go eat cheese.")
help_erica = input("What would you like to say?")
print()

if help_erica == "a":
  print("Erica: Ah, thank you!")

if help_erica == "b":
  print("Erica: What? Eat cheese? Oh, be quiet. Come and help me!")

print()
print("And so, the Hero of Hyrule was forced to help Erica with her math homework.")

print("Erica: I need to be able to do factorials! Quick, give me a number between 1 and 10, inclusive.")

factorial_number = int(input("Which number would you like to give to Erica? "))

def test_erica_factorials(factorial_number):
  ''' 
  Takes factorial of inputted number
  
  Takes in integer n, between 1 and 10 inclusive, and finds the product of every integer from 1 to n
  
  Parameters
  ----------
  factorial_number : integer
    The inputted integer, of which the factorial will be returned
  
  Returns
  ----------
  string
    A message with the factorial of the inputted integer

  Raises
  ----------
  TypeError
    If inputted value is not an integer
  ValueError
    If the required integer was outside of the given range
  Exception
    If the factorial is calculated incorrectly
  '''
  
  if not isinstance (factorial_number, int): 
    raise TypeError('The input was expected to be an integer.')
  
  if not (factorial_number <= 10) and (factorial_number >= 1):
    raise ValueError('Values not within expected range [1, 10]')
    
  logging.debug('Original input value is ' + str(factorial_number))
  
  factorial_result = 1
  while factorial_number >= 1:
    factorial_result = factorial_result * factorial_number
    factorial_number = factorial_number - 1
  
  logging.debug('The factorial of the input is ' + str(factorial_result))
  
  if not isinstance(factorial_result, int): 
    raise Exception('Factorial was not an integer, like expected.')

  factorial_answer = ("Erica: The factorial is " + str(factorial_result) + ".")
  return factorial_answer

print(test_erica_factorials(factorial_number))
logging.debug("End of factorial function.")
print()

try:
  print("Erica: Well, now let's consider the number 3.")
  print(test_erica_factorials(3))
  logging.debug("End of factorial function.")
  print()
  
  # print("Erica: But if you told me to find the factorial of cat...")
  logging.error("Taking factorial of string results in program stopping")
  # print(test_erica_factorials("cat"))
  # print()

  # print("Erica: And if you told me to find the factorial of -8.")
  logging.error("Taking factorial of a negative results in program stopping")
  # print(test_erica_factorials(factorial_number))

except Exception as e:
  print("There is something wrong: " + str(e))
  
logging.disable(logging.CRITICAL)

print()

print("Erica: Hey, I think I'm pretty good at finding factorials. See, now wasn't that better than eating cheese all by yourself? Thanks for helping me, " + name + "! <3")

print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
