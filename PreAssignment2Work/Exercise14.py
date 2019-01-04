#-----------------------------------------------------------------------------
# Name: Exercise 14 (Exercise14.py)
# Purpose: Display understanding of reading files
#
# Author: vonlugersbutter
# Created: Monday, December 10, 2018
# Updated: Friday, December 14, 2018
#-----------------------------------------------------------------------------

import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

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
print()

name = input("I want a clementine *wheezes*. What is your name, hero? ")

print("Erica: " + name.upper() + "!!! Come on, let's go!")
print("Now you, hero, frankly had no idea what Erica was talking about.")

bee_movie = open('data.txt', 'r')
bee_movie_contents = bee_movie.readlines()
bee_movie.close()

print()
print("You were dragged into a room, and Jackie and Ayesha were sitting on the ground with brie-flavoured popcorn. Jasmine was sitting on the sofa wrapped in quilts like a little sushi roll. <3")
print()

age = int(input('Erica: ' + name + "! How old are you?!"))
print()

def bee_movie_calculator(age_of_hero): 
  '''
  Returns number of years since the bee movie came out, and how long the user has been alive with the bee movie.

  Takes the number of years the user has been alive, and finds the number of years the user has lived with the bee movie.

  Parameters
	----------
	age_of_hero : integer
		Age of user, which will be used to compute how long the user has lived with the bee movie

	Returns
	-------
	string
		A message that shows the number of years one has lived with the bee movie

  Raises
	------
	TypeError
		If the age of the hero is not an integer
	ValueError
		If the age of the hero is below 3 or over 99
	Exception
		If the age calculation goes wrong
	'''

  if not isinstance(age_of_hero, int):
    raise TypeError('The age of the hero was not an integer, as expected.')
	
  if age_of_hero <= 3 or age_of_hero > 99:
    raise ValueError('The age of the hero was not in the predefined range.')
	
  bee_movie_release = 2007
  year_of_hero_birth = 2018 - age_of_hero
  
  logging.debug('Age of the hero is: ' + str(age_of_hero))
  
  if year_of_hero_birth >= bee_movie_release:
    alive_with_bee_movie = age_of_hero
  
  if year_of_hero_birth < bee_movie_release: 
    alive_with_bee_movie = bee_movie_release - year_of_hero_birth
  
  logging.debug('Years alive with the bee movie is ' + str(alive_with_bee_movie))
  
  if not isinstance(alive_with_bee_movie,int):
    raise Exception('Something went wrong with the bee movie age calculation.')
  
  return print("Erica: That means you have been alive with the Bee Movie for " + str(alive_with_bee_movie) + " years!!!")
  
print(bee_movie_calculator(age))

print()
print("And you saw it. A black screen, with white serif words appearing on the screen. \n")

for line in bee_movie_contents[0:9]:
  print(line)
  
print("And so, you, the Hero of Hyrule, settled down with brie popcorn and proceeded to watch the bee movie for the rest of the afternoon.")
print("Your adventure will continue in another exercise, hero. Farewell for now, " + name + ".") 
