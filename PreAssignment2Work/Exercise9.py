#-----------------------------------------------------------------------------
# Name:       Exercise 9 (Exercise9.py)
# Purpose:    Display understanding of lists, indexes, and using list functions
# 
# Author:     vonlugersbutter
# Created:    Monday, November 12, 2018
# Updated:    Monday, November 19, 2018
#-----------------------------------------------------------------------------

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
import time

name = input("We have met so often, but my poor memory renders me forgetful. What is your name, hero? \n")

print("Go now, " + name + ", to Hyrule. \n")

time.sleep(1)
print(".")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print()

print("Jackie waves to you.")
print("Jackie: Hi, " + name + "! What are you up to?")
print("Jackie: Nothing? Oh. \n")

time.sleep(4)

print("Erica: Jackie!! " + name + "!! I just got a letter from Ashei, that one girl I know that lives near the Snowpeak Mountains. \n")

print("Jackie: What did she say? \n")

print("Erica: She said that someone's been entering into the Zora's Domain, and stealing Reekfish! Ashei knew about " + name + " and how they are the Hero of Hyrule, and requested their assistance. \n")

print("Jackie: What do you think, " + name +"? \n")

print("a. Yes, I'll go and help her.")
print("b. No, I'm fine right here in Ordon.")
print("c. I'm not sure.")
going_to_snowpeak = input("Will you go help Ashei? \n")

if going_to_snowpeak == "a":
  print("Erica: Perfect! Off you go to the Snowpeak Mountains!")

if going_to_snowpeak == "b":
  print("Erica: Oh, be quiet. You're the Hero of Hyrule. You have to help people.")

if going_to_snowpeak == "c":
  print("Erica: I'll decide for you. You're going to Snowpeak.")

print()
print("Jackie: Good luck! I'll lend you Epona to get there. \n")

time.sleep(5)
print("And so, you, Hero of Hyrule, ventured off to Snowpeak Mountains. Eventually, as you reached Hyrule fields, you continued to Snowpeak. \n")

time.sleep(2)
print("My god it's cold. \n")
time.sleep(7)

print("You trudge through the snow, frowning at how cold it is, until you see a girl with black hair in armour. That must be Ashei. \n")

print("Ashei turns around to greet you. \n")
print("Ashei: You must be " + name + ". Good to see you. I'm glad you came to help.")
print("Ashei: The problem is that someone keeps sneaking down to the Zora's Domain and stealing reekfish from their holds. They've asked me to help them, but the only thing I've been able to see at night is a huge silhouette of some kind of monster. \n")

ashei_question = input("Ashei: Do you follow? \n")

print("Ashei: Last night, I managed to get a quick sketch of it while it was taking the reekfish. I tried to chase after it, but it vanished off into a blizzard. That's when I decided to tell Erica about it. \n")

ashei_instructions = ['Find the creature','Figure out why it is stealing fish']

print("Ashei: Here are your instructions, hero. \n")

for i in ashei_instructions:
  print(ashei_instructions.index(i) + 1, end='')
  print(". ", i)

print()
print("Ashei: Here's the sketch. \n")

print("You got Ashei's drawing. It has a tall, roundish silhouette of something holding a reekfish. \n")

time.sleep(3)

print("Ashei: Wait a minute, hero! I forgot to ask you to do some more tasks once you find out why the fish is going missing. \n")

ashei_instructions.append('Tell Ashei why the fish was disappearing')

ashei_instructions.append('Tell the Zora people why fish was missing from the holds')

print("Ashei: Here are your new instructions, hero: \n")

for i in ashei_instructions:
  print(ashei_instructions.index(i) + 1, end='')
  print(". ", i)

print()

time.sleep(7)

print("You thank Ashei and begin heading off deeper into the mountains. Little did they know your experience eating fine cuisine in Telma's Bar at 3 AM has made you an expert at sniffing out random things. Like when you sniffed out Erica's keys from under her doormat and took 50 rupees from her basement.\n")

print("As you follow the trail of the reekfish scent, you see a huge white fluffy thing in the distance. Hold on. It's a yeti. Yeah we have those in Hyrule.")
say_to_yeto = input("What do you want to say to the yeti? \n")

print("The yeti turns around and looks down at you.")
print("Yeto: Uh? What is small Hylian doing here in front of Yeto? \n")
print("You tell Yeto about how you nearly broke your back trying to find who was taking reekfish from the Zora holds. \n")

print("Yeto: Oh, you mean fish? Yeto need fish to make soup for Yeta. Yeta sick.")
print("Yeto: Oh!! Yeto has idea. Small Hylian help Yeto make soup, and Yeto will give small Hylian lots of money! What you say? \n")

print("Alright, so now you had a chance to get some rupees just to help this big guy make soup. You mentally added another item to your 'instructions'. \n")

yeto_instructions = ashei_instructions.copy()

yeto_instructions += ['Help Yeto make soup', "Get paid enough rupees to buy a month's worth of shredded cheese"]

for i in yeto_instructions:
  print(yeto_instructions.index(i) + 1, end='')
  print(". ", i)

print()

print("You didn't really have a choice at this point. \n")

print("a. Yes, I will.")
print("b. Oh, alright.")
yeto_question = input("Yeto: Will you help Yeto, small Hylian? \n") 

print("Yeto: Oh, Yeto thanks you, small one! Now come along, we must go to Yeto house. Follow Yeto. \n")

print("Yeto pulled a board from behind a tree and handed you a smaller one. He stepped onto it, and began to sled down the mountain. You did the same, and as you made your way down the mountain, you nearly swallowed a bug and had a red rash on your head from hitting a branch. \n")

time.sleep(7)

print("You finally got down to Yeto's house. \n")

print("Yeto: Come inside, small one! Yeto will show you around. \n")

yeto_house_components = ['paintings' ,'chandeliers', 'fancy red carpets', ' a kitchen with a huge pot']

print("As you looked around you saw " + yeto_house_components[0] + ", " + yeto_house_components[1] + ", " + yeto_house_components[2] + ", and" + yeto_house_components [-1] + ".") 

print()

print("Hold on. Scratch that. \n")

time.sleep(5)

del yeto_house_components[3]

yeto_house_components.append(' a kitchen with a huge pot WITH SOUP IN IT')

print("You saw " + yeto_house_components[0] + ", " + yeto_house_components[1] + ", " + yeto_house_components[2] + ", and" + yeto_house_components [-1] + ".")

print()
print("Ah yes. Yet some more instructions.")

getting_soup_instructions = ["Drink ENTIRE POT OF SOUP in Yeto's Kitchen"]

yeto_instructions = yeto_instructions + getting_soup_instructions

for i in yeto_instructions:
  print(yeto_instructions.index(i) + 1, end='')
  print(". ", i)

time.sleep(4)

print()
yeto_components_addition = input("What else do you see in Yeto's house?")
yeto_house_components.append(yeto_components_addition)

print("You saw " + yeto_house_components[0] + ", " + yeto_house_components[1] + ", " + yeto_house_components[2] + ", "+ yeto_house_components[3] + ", and " + yeto_house_components [-1] + ".")

print()

print("Yeto: Small one help Yeto make soup in kitchen. Get Yeto ingredients. \n")

print("AARGH. Fine. Reorder the list.")
print("You already found the creature and why it was stealing fish, so that's done.")
print()

new_instructions = ['Get Yeto soup ingredients' , 'Help Yeto make soup' , "Get paid enough rupees to buy a month's worth of shredded cheese" , "Drink ENTIRE POT OF SOUP in Yeto's Kitchen" , "Tell Ashei why the fish was disappearing" , "Tell the Zora people why fish was missing from the holds"]

for i in new_instructions:
  print(new_instructions.index(i) + 1, end='')
  print(". ", i)

print()
ready_signal = input("Are you ready, hero? ")

print()

print("Yeto hands you a list of ingredients. \n")

integer_ingredients = [2,1,2,1,29,12,4,2]
float_ingredients = [0.5,0.5,0.5,0.75,0.75]
ingredient_unit = ['tbsp','','cloves','quart','ounces','ounces','ounces','tbsp','tsp','tbsp','cup','cup','cup']
ingredients = ['butter','diced onions','garlic','vegetable broth','canned pumpkin','evaporated milk','fresh goat cheese','brown sugar','salt','black pepper','half & half cream','diced carrots','diced celery']

counting_integer_ingredients = 0

while counting_integer_ingredients <= 7:
  print(str(integer_ingredients[counting_integer_ingredients]) + " " +ingredient_unit[counting_integer_ingredients] + " " + ingredients[counting_integer_ingredients])
  counting_integer_ingredients = counting_integer_ingredients + 1

counting_float_ingredients = 8
float_ingredient_numbering = 0

while counting_float_ingredients <= 12:
  print(str(float_ingredients[float_ingredient_numbering]) + " " + ingredient_unit[counting_float_ingredients] + " " + ingredients[counting_float_ingredients])
  counting_float_ingredients = counting_float_ingredients + 1
  float_ingredient_numbering = float_ingredient_numbering + 1

print()
got_ingredients = input("Did you get that, " + name + "?")

print()

print("Yeto: Get all ingredients for Yeto, and then we will make yummy soup. \n")

print("Alright, so you have a list of items to look at, and you must organize yourself so all the items are easier to find. \n")

time.sleep(4)

print("First try listing only the ingredients, without their quantity. \n")

for item in ingredients: 
  print(item)

print()

print("Now we can organize them by alphabetical order, because all heroes like alphabetical order.")

temporary_integer_sort = integer_ingredients.copy()

temporary_integer_sort.sort()

for item in temporary_integer_sort:
  print(str(item))

print()
print("No! Sort the ingredients in alphabetical order, not the numbers in numerical order!")

time.sleep(5)

temporary_float_sort = float_ingredients.copy()

temporary_float_sort.sort(reverse = True)

for item in temporary_float_sort:
  print(str(item))

print()
print("Now you're just being mean. Sort the ingredients in alphabetical order!!")
print()

time.sleep(5)

temporary_ingredient_sort = ingredients.copy()
temporary_ingredient_sort.sort()

for item in temporary_ingredient_sort:
  print(item)

print()

print("There. That's better.")
print()

time.sleep(4)

going_to_get_ingredients = input("Are you ready to collect the ingredients, hero?")
print()

print("Nevermind that now. Off we go!")
print()

print("After going around the entire mansion, through icy floors and poorly heated rooms, you find the thermostat and put it up to 28°C. That's better. You trample over to the fridge and grab some butter. You cut the onions with your Ordon Sword so aggressively that they start crying. Next, you crush garlic cloves with your bare hands, and then take some vegetable broth out of the freezer.")
print()

print("Next, you bash some pumpkins outside and then put the remains into a vacuum-sealed can. You take some milk and then put it out in the sun to evaporate it. Now, the list says 'fresh' goat cheese. You grab a nearby goat, milk it, and make cheese out of the curds. The brown sugar, salt, and black pepper were all conveniently in the pantry.")
print()

print("Let's see the last few ingredients.")
print(ingredients[10:13])
print()

print("Almost done. The half-and-half cream comes from the goat milk you got earlier, and you start attacking both a bag of carrots and a pile of celery. Diced carrots and celery. Done. Okay.")
print()

print("You go back to Yeto and show him all the ingredients. \n")

done_collecting = input("Yeto: Well done, small one! Is this all of ingredients for Yeto soup?")
print()

print("Yeto: Ah! Everything is here. Yeto will now make good soup for small human and Yeta. \n")

print("Yeto uses all the ingredients, and a very nice food processor, to start making some soup. \n")

print("Yeto: Yeto has finished putting together the important ingredients, but Yeto and small one must wait for soup to simmer. Yeto has good idea! Would small one like to play a game of Hangman? \n")

print("You're surprised Yeto even knows about Hangman. But it is a good idea, regardless.")
print()

print("a. Yes, I would like to play.")
print("b. No, thanks.")
play_hangman = input("Would you like to play Hangman?")

if play_hangman == "a":
  print("Yeto: Good, good! Small one will play Hangman with Yeto! \n")

if play_hangman == "b":
  print("Yeto: Uh? Small one must play Hangman with Yeto! Yeto will see if Yeto can beat small one at Hangman! \n")

print()
print()

def hangman():
  '''
  User attempts to guess unknown word by trying to guess all of its letters within a set number of tries

  User is shown several spaces, corresponding with letters in the unknown word. The number of tries is only decreased if the letter guessed is not in the word. If the user wins, or runs out of attempts, the game ends. 

  Parameters
  ----------
  none
  
  Returns
  ----------
  string 
    A message that tells the user the game has ended
  '''

  print("Yeto: Now, Yeto will guess word, and small one will guess its letters. If small one has all letters correct, small one wins! If small one does not get all letters in ten tries, Yeto wins. Tries only go down if small one gives incorrect letter. \n")

  start_hangman = input("Yeto: Small one ready?")

  print()

  secret_word_list = list("snowpeak")

  print("Yeto: The word in Yeto's head has " + str(len(secret_word_list))+ " letters! ")
  print()

  previous_guesses = ''
  attempts = 10
  alphabet = list("abcdefghijklmnopqrstuvwxyz")

  while attempts > 0: 
    blank_spaces = 0

    for letter in secret_word_list:
      if letter in previous_guesses:
        print (str(letter))
    
      else:
        print("-")
        blank_spaces = blank_spaces + 1
    
    if blank_spaces == 0:
      print()
      print("Yeto: Small one has guessed word in Yeto's head! Small one wins game!")
      break
    
    user_guess = (input("Yeto: Small one must try to guess letter in Yeto head."))

    previous_guesses = user_guess + previous_guesses

    if user_guess not in alphabet:
      print("Yeto: Uh? That not a letter. Try again, small one.")
    
    elif user_guess not in secret_word_list:
      print("Yeto: Small one not right. That letter not in word.")
      attempts = attempts - 1
    
    print("Yeto: Small one still has " + str(attempts) + " tries left!")

    if attempts == 0:
      print("Yeto: Uh? Small one has run out of tries. The word in Yeto head was " + ''.join(secret_word_list) + ". Yeto win.")
  
  return print("Yeto: That was nice, was it not small one? Yeto is very good at games. Yeto will see if soup is done now.")

hangman()

print()
print()

print("Yeto: Ahh!! Soup is done. Yeto is very happy. Yeto will take soup to Yeta. Come, small one! \n")

time.sleep(6)

print("You follow Yeto around until he reaches a large bedroom door. Yeto slowly opens the door, and you see another, smaller yeti sitting on an armchair facing a fireplace. That must be Yeta. \n")

say_to_yeta = input('What do you want to say to Yeta?')
print()

print("Yeta: Uh? Who is this small Hylian?")
print("Yeto: This small one! Small one help Yeto make good soup for Yeta. \n")

print("Yeta: Small one help Yeto make soup? Ah, Yeta thanks you, little one. Yeta is very sick.")
print("Yeto: Eat some of good Yeto soup. Yeta will get better.")
print()

time.sleep(4)

print("Yeta drinks some of the soup, and quickly finishes the bowl.")
print("Yeta: That is good soup! Yeta feels better already.")
print("Yeto: Yeto knew it would be good! Yeto will get you more. Small one stay here while Yeto get soup for Yeta and small one. \n")

print("Yeta: Yeta is very thankful to little one for helping Yeto make soup, but Yeta has question. How did little one meet Yeto? \n")

def yeta_mishearing():
  '''
  Displays messages to reader as Yeta 'mishears' user input and returns reader with misheard input.

  Based on the phrase selected before the function, the function returns a copy of the input phrase with a slight difference, as if Yeta misheard it and is repeating it to the user.

  Parameters
  ----------
  none 

  Returns
  ----------
  string
    Message is created, where 'user' shouts the actual phrase that was said, instead of Yeta's misheard phrase
  '''

  print("a. It's a very long story involving reekfish.")
  print("b. It's a very long story involving almost swallowing a bug.")
  print("c. It's a very long story involving making onions cry.")
  explain_to_yeta = input("Which would you like to choose?")

  if explain_to_yeta == "a":
    yeta_phrase = ['I was relaxing in Ordon','Someone named Erica told me to get up and actually do my job','I nearly froze up on the mountains']
    print()

  if explain_to_yeta == "b":
    yeta_phrase = ['I met Yeto on the mountain, where I nearly froze','He invited me to help him make soup','We sledded down the mountain, and I nearly swallowed a bug']
    print()

  if explain_to_yeta == "c":
    yeta_phrase = ['I agreed to help Yeto make soup while we were up on the mountains','He asked me to collect all the ingredients','We played Hangman']
    print()
  
  print("You explain your journey in the form of a step-by-step numerical list.")
  print()

  for i in yeta_phrase:
    print(yeta_phrase.index(i) + 1, end='')
    print(". ", i)

  new_phrase = yeta_phrase.copy()

  if explain_to_yeta == "a":
    del new_phrase[-1]
    new_phrase.append('nearly froze on the fountains')
  
  if explain_to_yeta == "b":
    del new_phrase[-1]
    new_phrase.append('nearly swallowed a rug')

  if explain_to_yeta == "c":
    del new_phrase[-1]
    new_phrase.append('played orangutan')

  print()
  print("Yeta: Uh? Little one " + new_phrase[-1] + "?")
  
  return print("You tried to raise your voice and say: " + yeta_phrase[-1] + "!!")
  
yeta_mishearing()

print()

print("Yeta: Ah, sorry, little one. Yeta's hearing is not so good with all these blankets around Yeta.")
print()

print("Yeto comes back with the soup, and you all eat some. <3")
print("Ah well, it seems like your mission is over now, " + name + ".")
print()

time.sleep(8)

print("You say goodbye to Yeto and Yeta, thank them for the soup, and get paid approximately 200 rupees in the process. Heh heh.\n")

print("Yeto takes you back up the mountain using a nifty elevator-like object, and he leaves you near the Zora's Domain. You go to the Zora people and Ashei, and tell them why the fish was going away. You tell them it won't happen again, because Yeto has a lot of soup now, and Yeta is almost better. \n")

time.sleep(3)

print("Seems like a job well done to me, hero! Let's go over all the instructions we completed.")

total_instructions = [ashei_instructions,yeto_instructions,getting_soup_instructions,new_instructions]

print()
print(total_instructions)

print()
print()
print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
