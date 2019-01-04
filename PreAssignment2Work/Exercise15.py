#-----------------------------------------------------------------------------
# Name: Exercise 15 (Exercise15.py)
# Purpose: Display understanding of writing files
#
# Author: vonlugersbutter
# Created: Wednesday, December 12, 2018
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

name = input("oowwowoowowowo... What's your name, hero? ")

print("Jasmine: " + name.upper() + "!! I have a great idea, let's write poems together! \n")

print("Now you, hero of Hyrule, had no idea what you were going to write as Jasmine dragged you to her Emporium. You were a hero, not a bard.")

poem_type = input("Jasmine: What kind of poems do you like to write, " + name + "?")
print()

for character in poem_type:
  if character.isalpha():
    break
  elif not character.isalpha():
    there_is_a_letter = False
    while there_is_a_letter == False:
      if character.isspace():
        break
      elif not character.isspace():
        raise Exception('Poem type does not have letters or spaces, as expected.')

print("Jasmine: I like those kinds of poems, too. Come on, I'll show you how to write a good limerick.")
print("Jasmine: Limericks have the rhyming scheme AABBA. Here, I'll write a limerick on this piece of paper.")

jasmine_limerick = ['Jackie went to bed', "Ayesha started to shred", "The cheese that was to be eaten", "At Tetris, Erica was beaten", "Then Jasmine shooke her head"]

poems = open('output.txt' , 'w')
for line in jasmine_limerick: 
  poems.write(line)
  poems.write("\n")
poems.write("\n")
poems.close()

print("Jasmine: There we go!")
print("You glanced at the paper. \n")

poems = open('output.txt','r')
poem_lines = poems.readlines()
for line in poem_lines[0:5]:
  print(line)
print()
poems.close()

print("Hmm. That's pretty interesting.")
print("Jasmine: Now you try! It doesn't have to rhyme, you know. You can write prose, too.\n")
print("You stared blankly at the piece of paper, and wrote down the first thing you could think of.")

wednesday = ['it is wednesday my dudes.' , 'aaaaaaaaaaaaAAAAAAAAAAAAAA']

poems = open('output.txt' , 'a')
for line in wednesday: 
  poems.write(line)
  poems.write("\n")
poems.write("\n")
poems.close()

print("Jasmine looked at the paper, and frowned a bit.")

poems = open('output.txt','r')
poem_lines = poems.readlines()
for line in poem_lines[5:8]:
  print(line)
print()
poems.close()

print("a. It's prose.")
print("b. I couldn't think of anything else.")
hero_opinion = input("Jasmine: What's this, " + name + "?")
print()


def write_your_own_poem():
  '''
  Allows the user to create multiple lines of poetry, and combine them in a dictionary

  Combines a series of lines inputted by the user, ensuring that they consist only of letters and spaces, and forms them into a dictionary

  Parameters
	----------
	None

	Returns
	-------
	None

  Raises
	------
	TypeError
		If the inputted line contains something other than letters or spaces
	'''
  
  print("Jasmine: Ah. Well, let's move on. Why don't you write another? This time, make some lines, and then combine them together in no particular order!")
  print()
  
  hero_done = False
  
  first_line = input("Jasmine: Go ahead and add a line. ")
  
  for character in first_line:
    if character.isalpha():
      break
    elif not character.isalpha():
      there_is_no_letter = True
      while there_is_no_letter == True:
        if character.isspace():
          break
        elif not character.isspace():
          raise TypeError('Line entered does not have letters or spaces, as expected.')
  
  logging.debug(first_line)
  out_of_order_poem = {1 : first_line}
  print()
  
  while hero_done == False:
    
    print("a. Add a line.")
    print("b. End poem.")
    want_to_add_line = input("Jasmine: Do you want to add another line? ")
    logging.debug(want_to_add_line)
    print()
    
    if want_to_add_line == "a":
      line_added = input("Jasmine: Go ahead and write the line you want to add. ")
      logging.debug(line_added)
      print()
      
      for character in line_added:
        if character.isalpha():
          break
        elif not character.isalpha():
          there_is_a_letter = False
          while there_is_a_letter == False:
            if character.isspace():
              break
            elif not character.isspace():
              raise ValueError('Poem type does not have letters or spaces, as expected.')
      
      out_of_order_poem[int(len(out_of_order_poem) + 1)] = line_added
    
    elif want_to_add_line == "b":
      break
  
  logging.debug(out_of_order_poem)
  
  print("Jasmine: Well done! Let's see the poem you wrote. <3 \n")
  for v in out_of_order_poem.values():
    print(v + "\n")
  
  return

print(write_your_own_poem())

print()
print("Jasmine: *sigh* Well, it was quite fun writing poems with you, " + name + ". Would you like to keep the paper? ")
print("You nodded. \n")

print("Jasmine went to go eat some cookies, while you sat there scribbling 'prose' onto the paper.")

poems = open('output.txt', 'a')
avocado = ["it's an avocado" , "thanks"]
for line in avocado: 
  poems.write(line)
  poems.write("\n")
poems.write("\n")
poems.close()

poems = open('output.txt', 'a')
katrina = ["hurricane katrina" , "more like hurricane tortilla"]
for line in katrina: 
  poems.write(line)
  poems.write("\n")
poems.write("\n")
poems.close()

poems = open('output.txt', 'a')
christmas = ["happy christhums", "it's chrismah" , "merry chrisis", "merry chrysler"]
for line in christmas: 
  poems.write(line)
  poems.write("\n")
poems.write("\n")
poems.close()

print()
print("Maybe poetry isn't so bad after all. But, then again, the hero of Hyrule is remarkably good at everything.")
print("Farewell for now, hero. Your adventure will continue in another exercise, " + name + ". ")
