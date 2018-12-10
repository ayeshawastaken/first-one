#-----------------------------------------------------------------------------
# Name: Exercise 13 (Exercise13.py)
# Purpose: Display understanding of string manipulation
#
# Author: vonlugersbutter
# Created: Monday, December 3, 2018
# Updated: Friday, December 7, 2018
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

name = input('One day you will tire of me. What is your name, hero? ')

print()
print(name + "... Go now, to Hyrule. \n")

print("Jackie, Erica, Jasmine, and you had all been discussing words. Now, what they did not realize was that you, hero of Hyrule, had a way with words (and a way with cheese).")
print('''"'''+ name + '''," Erica said mockingly. "What do you know about words?"''')
print("How naive of her. \n")
print()

print("Firstly, you told Erica how each word is simply a string of letters with some sort of attached meaning, and they can hence be easily manipulated.")
print("Take, for example, the word 'Hyrule'.")
first_example = 'Hyrule'
first_example = first_example.lower()

if first_example.isalnum():
  print("Now, from this word, we can tell that " + first_example + " has either numbers or letters in it.")

print("In reality, the word is just a list of letters.")

first_example_characters = list(first_example)

for character in first_example_characters:
  if character in first_example_characters[0:5]:
    print(character, end=', ')
  else:
    print(character)

print()
print("Joining the letters together in an arbitrary assigned order somehow gives a meaning to the jumble of lines and curves.")
joined_first_example = "".join(first_example_characters)
print(joined_first_example)

new_word = 'H y r u l e'
new_word.upper()
new_word_list = new_word.split(' ')

print("Now, we can look at these letters independently, and notice how they do not have any meaning on their own.")
for character in new_word:
  print(character)

print()
print("Erica: Now, don't get so metaphysical about words. You're going to have a breakdown about them and I just mopped the floor. (Do with that information what you will.) \n")

print("But you could no longer hear Erica, \rand continued to ramble on about the gift that is language. \n")

print('''"And," you said to Erica, "one can make the expression of a word loud and harsh simply by changing the case. Take, for example:''')
command = "do the dishes"
command = command.lower()

if command.islower():
  print(command)
    
if command.isupper():
  raise Exception("String manipulation has not functioned properly.")

command = command.upper()

if command.isupper():
  print(command)
  
if command.islower():
  raise Exception("String manipulation has not functioned properly.")

print()
print("The first command is not nearly as harsh as the second. \n")

print("But then, aren't all words just combinations of letters? And all letters are just combinations of lines, curves, and dots that we have somehow assigned value to?")
letter_example = "comp/uter"
print("For example, take the word " + letter_example + ".")
print()

print("Hark! What's that there, in the middle of the word?")

for character in letter_example:
  
  if not character.isalpha():
    print("Aha! Nothing gets past the hero of Hyrule. That word would be a word if it did not have that " + character)
    print()
    
if not letter_example.isspace():
  print("The word does not have a space in it either, and again, we have made spaces an arbitrary way to separate words. \n")
  
if not letter_example.isdecimal():
  print("The word does not have any numbers in it, but then again, how can we simply define numbers and make arbitrary symbols for them? How are we able to recognize them the way the hero of Hyrule recognizes the aroma of mouldy cheese? \n")
  
opinion = input("What do you think of numbers, " + name + "? ")

print()
print("Ah, nevermind that now. Let us focus our energies on words.")

word_is_word = False

while word_is_word is False:
  first_word = input("Name a word, " + name + ". ")
  
  logging.debug(first_word)
  
  if first_word.isalpha():
    word_is_word = True
    break
  
  for character in first_word: 
    if character.isdecimal():
      print("That's not a word, it has a number in it!")
      print()
    
    if character.isspace():
      print("That has spaces in it! Give me a word.")
      print()

first_word_def = input("And, hero, what is the arbitrary definition of this word? ")

hero_dictionary = {first_word: first_word_def}

logging.debug(hero_dictionary)

print()
print("Here's an idea: let's make a hero dictionary! ")

word_is_word = False

while word_is_word is False:
  second_word = input("Alright. What's the second word you would like to choose? ")
  
  logging.debug(second_word)
  
  if second_word.isalpha():
    word_is_word = True
    break
  
  for character in second_word: 
    if character.isdecimal():
      print("That's not a word, it has a number in it!")
      print()
    
    if character.isspace():
      print("That has spaces in it! Give me a word.")
      print()

second_word_def = input("And what is the definition of this word? ")

hero_dictionary[second_word] = second_word_def

logging.debug(hero_dictionary)

print()
print("Here's another thing. Letters are what make up words, yes? ")
starts_ends_example = 'malignant'

logging.debug(starts_ends_example)

if starts_ends_example.startswith('m'):
  print("Now, " + starts_ends_example + " starts with an 'm'.")

else: 
  print(starts_ends_example + " does not start with an 'm'.")

if starts_ends_example.endswith('t'):
  print("And, " + starts_ends_example + " ends with a 't'.")

else:
  print(starts_ends_example + " does not end with a 't'.")

print()
print("Now, I shall add some words that should be part of the hero's dictionary.")
print()

hero_dictionary['Hero of Hyrule'] = 'noun: The best and most illustrious personality Hyrule has ever seen'
hero_dictionary['milk'] = 'noun: a very nice liquid-like substance commonly drunk by the Hero of Hyrule at 3 AM straight from the carton (See Hero of Hyrule)'
hero_dictionary['Erica'] = "noun: Local merchant; believes that the Hero of Hyrule has to help everybody all the time and can't have their own milk-drinking time once in a while"
hero_dictionary['sip'] = 'verb: antonym to chug; what Jackie does with soy milk'
hero_dictionary['chug'] = 'verb: the correct fashion of drinking milk'
hero_dictionary['illustrious'] = 'adjective: a trait commonly attributed to the Hero of Hyrule'

print("Alright, let's make this dictionary. Note that it won't be in alphabetical order because there aren't that many words in this dictionary.")
print()

title = ("         HERO'S DICTIONARY         ")

title = title.lstrip()
title = title.rstrip()

print(title.center(51,"~"))
print()

print("Made by the beloved Hero of Hyrule".ljust(51,"~"))
print()

for word_and_def in hero_dictionary: 
  word_and_def = word_and_def.strip()
  print(word_and_def.ljust(51,"~"))
  print("\t" + hero_dictionary[word_and_def])
  print()

print("Well done hero! You made a very nice dictionary.")
print("Farewell, for now, hero. Your adventure will continue in another exercise.")
