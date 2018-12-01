#-----------------------------------------------------------------------------
# Name: Exercise 12 (Exercise12.py)
# Purpose: Display understanding of dictionaries, lists, and tuples
#
# Author: vonlugersbutter
# Created: Thursday, November 29, 2018
# Updated: Friday, November 30, 2018
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

name = input("How many times have we met, hero? I cannot count, but I still forget. What is your name? ")
print()

print( name + ". Go now, to Hyrule. \n")

print("Erica: " + name + "!!! Come quickly!!")
print("Erica: Oh, " + name + ", you have to help me! I'm supposed to have a list of all the items in my store, an inventory, but I can't find the list I made before anywhere! The auditors are coming tomorrow and I have to have an inventory! Please help me make a list!! \n")

print("a. I'll help.")
print("b. No, go away.")
help_erica = input("Will you help Erica make an inventory? ")
print()

if help_erica == "a":
  print("Erica: Thank you so much~~!")

if help_erica == "b":
  print("Erica: >:( If you help me I'll give you shredded brie that's been out of the fridge for 3 days.")
  print("Now, 3 day old shredded brie is a delicacy that no hero can sanely resist. Especially when those 3 precious days were spent outside of a fridge. You decide to help Erica.")

print()

print("Erica: Alright, so come into the store so we can count all the items.")
print("You are now in Erica's store. ")

print()
print("Erica: I already counted how many bottles of red potion I have. It's 11 bottles.")

logging.debug('Start of dictionary creation')
erica_items = {"Red Potion" : 11}

print("Erica: Oh, and there are 4 Hylian Shields in stock.")

erica_items["Hylian Shield"] = 4

print()
print("Erica: So what's on that list now? \n")

for i in erica_items.items():
  item, number = i
  print(number, end=' ')
  print(item)

print()
print("Erica: Oh, that's not enough for the auditors. Let's keep counting.")

number_of_swords = int(input("Erica: How many swords are there? Can you please count them? "))

erica_items["Swords"] = number_of_swords

print("Erica: Hold on, there are 2 kinds of swords! There are the ones with wooden hilts and with metal hilts. We have to sort them differently.")
print()

number_of_wooden_swords = int(input("How many wooden swords are there? "))
number_of_metal_swords = int(input("How many metal swords are there? "))
print()

erica_items["Wooden Swords"] = number_of_wooden_swords
erica_items["Metal Swords"] = number_of_metal_swords

print("Erica: Take swords off the list then.")
del erica_items["Swords"]
print("Erica: Can you show me the list again?")

for i in erica_items.items():
  item, number = i
  print(number, end=' ')
  print(item)

print("Erica: Alright, now I need you to go count some items, while I count the stuff in the inside of the warehouse. I'll get you a list of instructions. \n")

erica_instructions = ["Count the bottles of milk", "Count the male golden bugs" , "Count the female golden bugs", "Count the reekfish", "Try to count the bags of shredded brie without eating them" , "Report back to Erica with all the values"]

for i in erica_instructions:
  print(erica_instructions.index(i) + 1, end='')
  print(". ",i)

print()

print("As you went over to the bottles of milk and began to count them, Erica yelled to you from the back warehouse.")
print("Erica: " + name + "! I just remembered that I bought twenty bottles of blue potion last week from my supplier! I forgot how many I sold. How many bottles do you see at the front counter right now?")
print()

bottles_seen = int(input("How many bottles of blue potion do you see behind the counter? "))

logging.debug('Beginning of Profit function')

def potion_profit(blue_potion_bottles):
  '''
  Returns profit made based on number of bottles of blue potion

  User inputs number of bottles behind counter, which is used to determine how many bottles of blue potion Erica sold last week. User is returned the total profit Erica made by selling the potion

  Parameters
	----------
	blue_potion_bottles : integer
		Number of bottles found behind the counter, as inputted by the user

	Returns
	-------
	string
		The profit that Erica made last week by selling blue potion bottles

  Raises
	------
	TypeError
		If the number of blue potion bottles is not an integer
	ValueError
		If the number of blue potion bottles is over 20 or below 0
	Exception
		If the profit calculation returns incorrectly
	'''

  if not isinstance(blue_potion_bottles, int):
    raise TypeError('Number of blue bottles is expected to be an integer')
  
  if blue_potion_bottles > 20 or blue_potion_bottles < 0: 
    raise ValueError('Number of blue potion bottles cannot be lower than zero or higher than 20')
  
  logging.debug('Number of blue potion bottles to start is ' + str(blue_potion_bottles))
  
  bottles_sold = 20 - blue_potion_bottles
  
  logging.debug('Number of bottles sold is ' + str(bottles_sold))

  print("Erica: So, if you see " + str(blue_potion_bottles) + " bottles behind the counter, that means I sold " + str(bottles_sold) + " of them." )
  print()

  profit_made = bottles_sold*59.99
  
  logging.debug('Profit made is ' + str(profit_made))
  
  if not isinstance(profit_made,float):
    raise Exception("Profit made was not given as a float as expected")

  return print("Erica: Each bottle costs 59.99 rupees, so I must have made " + str(profit_made)+ " rupees from them.")

potion_profit(bottles_seen)
logging.debug('End of the profit function')

# The tests below have been commented out so that they do not interfere with the program
#try:
#  potion_profit(20)
#  potion_profit(200)
logging.critical('Using a value higher than 20 for the blue potion bottles will cause the program to stop')
#  potion_profit(-3)
logging.critical('Using a negative value for blue potion bottles will cause the program to stop')
#except (TypeError, ValueError) as e:
#  print("One of the values were incorrect: " + str(e))
#except Exception as e:
#  print("Something went wrong: " + str(e))

print()
print("After helping Erica with her blue potion shenanigan, you go back to counting the milk.")
print("You carefully count 32 milk bottles, 43 bags of shredded brie, and 19 frozen whole reekfish.")
print("You can cross that off your instructions list.")

del erica_instructions[0]
del erica_instructions[2]
del erica_instructions[2]

for i in erica_instructions:
  print(erica_instructions.index(i) + 1, end='')
  print(". ",i)

print()
print("Oh, and don't forget to add the things you counted to the inventory.")
erica_items["Milk Bottles"] = 32
erica_items["Bags of Shredded Brie"] = 43
erica_items["Whole Frozen Reekfish"] = 19
print()

for i in erica_items.items():
  item, number = i
  print(number, end=' ')
  print(item)

print()
print("Erica: " + name + "! What does shenanigan mean again? I'm trying to remember but I can't.")
print()

hero_dictionary = {"shenanigan" : "a devious trick used especially for an underhand purpose OR tricky or questionable practices or conduct", "shredded brie" : "the greatest, and most unprecedented food product ever manufactured by mankind" , "Hero of Hyrule" : "only the greatest, most illustrious, and most literate personality that Hyrule has ever seen", "milk" : "some sort of white-colored liquid addictive substance, commonly chugged by the Hero of Hyrule at 3 AM straight from the carton"}

print("Now you, hero, being the very literate hero of Hyrule you are, instantly take out your pocket dictionary that you always have with you, and look up the formal definition of shenanigan.")
print()

print("You read aloud from the dictionary (as according to Merriam-Webster):")
print("Shenanigan is defined as " + str(hero_dictionary['shenanigan']) + ".")

print()
print("Erica: Alright, alright. Hold on, is reekfish on the list? How many reekfish do we have?")
print("Erica looks at the list.")
print()

if 'Whole Frozen Reekfish' in erica_items.keys():
  print("Erica: Ah, there it is.")
  print("Erica: We have " + str(erica_items['Whole Frozen Reekfish']) + ".")
  
if 'Whole Frozen Reekfish' not in erica_items.keys():
  print("Erica: Oh dear. Well, you'd better go count them.")
  print("Erica: I think there are 19 reekfish.")

print()
print("You and Erica begin an animated conversation of whether tuples are better than lists. You, with your highly structured manner, prefer tuples, while Erica thinks that lists are more practical because they can be modified.")

print()
print("You tell Erica about how stating the time would be an example of a tuple.")
time = (11, 4)

hour,minute = time
print("For example, saying that it is " + str(minute) + " minutes past " + str(hour) + " could be represented as a tuple, since it has a specific structure. The hour and the minute have their places in the tuple and these cannot be altered without changing the meaning of the tuple.")
print()

print("Erica then argues that a list could be used for the same purpose, and would allow seconds to be added and deleted from the list.")

time = [11,4,37]
time_without_seconds = time.copy()
del time_without_seconds[-1]

print("For example, one could easily switch between saying " + str(time) + " and " + str(time_without_seconds) + ".")
print("Erica did agree however, that because lists lack structure, one cannot assign meaning to the position of items in a list like one can in a tuple.")

print("Erica and you both agree, however, that using a dictionary would be useless for both applications, since it stores items in a random order, which lacks structure completely.")
print()

print("You count the golden bugs, and add them to the inventory.")
erica_items["Male Golden Bugs"] = 11
erica_items["Female Golden Bugs"] = 14
print()

print("a. I'm done.")
print("b. I still have items to count.")
done_list = input("Erica: Are you done the inventory, " + name + "?")
print()

if done_list == "a":
  print("Erica: Excellent! I'll add the items I counted.")

if done_list == "b":
  print("Erica: Hmm? Give me that. You're done the inventory, you counted everything.")
  print("Erica: I'll add in the items I counted.")

print()
erica_items["Iron Boot Pairs"] = 1
erica_items["Clawshots"] = 2
erica_items["Arrows"] = 100
erica_items["Ball and Chain"] = 1
erica_items["Gale Boomerangs"] = 1

for i in erica_items.items():
  item, number = i
  print(number, end=' ')
  print(item)

print()

print("Erica: Yay! The inventory list is complete. Thanks for the help, " + name + "!")
print("Your adventure will continue in an another exercise. Farewell for now, hero.")
