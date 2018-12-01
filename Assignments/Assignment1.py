#-----------------------------------------------------------------------------
# Name:        Assignment 1 (Assignment1.py)
# Purpose:     Display understanding of Python basics, formatting, documentation, and assertions
#
# Author:      vonlugersbutter
# Created:     Sunday, October 28, 2018
# Updated:     Sunday, November 11, 2018
#-----------------------------------------------------------------------------

# r is included before each string to make program ignore backslash and oblique pairing

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

name = input("Forgive me, Hero of Hyrule. I ask your name once again.")

# To allow for delays in printing
import time 
print()

# Collection of name variable
print("You have awoken, " + name + ". Go now, to Hyrule.")

time.sleep(1)
print(".")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)

# introduction
print("You look around groggily, and Jackie is shaking you to wake you up.")
print()
print("Jackie: " + name + "! " + name + "! Wake up, it's early in the morning!!")
print()
time.sleep(2)
print("You remember now. You and Jackie had snuck into Telma's Bar at 3 AM last night.")
print("Jackie had quietly sipped soy milk while you proceeded to chug all the NORMAL milk in the fridge.")
time.sleep(1)
print()
print("Staggering up to the pantry, you had grabbed the bag of Black Diamond shredded cheese and aggressively stuffed fistfuls of brie into your face.")
print("Jackie looked on in horror.")
print()
time.sleep(4)

print("After you got up to see the sun rising, Jackie went home, while you put all the money for the milk and cheese onto Telma's counter.")
print()
time.sleep(2)
print("!!!")
print("You didn't have any more rupees left!! You had spent all of it on milk and shredded cheese!!")

# central variable rupee is set to zero to set premise for program
rupees = 0

print()
time.sleep(4)

print("Oh well, even heroes are broke sometimes...")
print("Erica approaches you.")
print()
print("Erica: " + name + "! Where have you been all this time?! I was looking for you this morning!")

# question posed to user to break text and pause reading
print("a. I was at Telma's Bar, drinking milk.")
print("b. I was liberating most of the Gerudo Desert.")
print("c. I was just about to go to sleep, and then I ended up on my roof, and that's what happened.")
after_bar = input()

print("Erica: What? Oh, nevermind that! " + name + ", the princess is coming to Ordon Village! The princess of Hyrule!!")
print("Jackie joins you two.")
print()
print("Jackie: Are you telling " + name + " about the arrival of the princess? It's true, she's coming to Ordon Village, and it's her birthday!")
print("Erica: I'm getting her a bouquet! It's already been tied with a bow.")
print("Jackie: I'm getting her a stone tablet with ancient runes on it.")

time.sleep(1)
print(".")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)

print("Erica: !!! Wait a minute, " + name + "!! You didn't get anything for the princess, did you?!")
print("Jackie: Oh no! How will you buy the princess a present now?")
print("Erica: " + name + " needs to impress the princess with a gift. How many rupees do you have?")
print()
time.sleep(1)

print("You show Erica your empty wallet.")
print()

print("Erica: Oh dear. Well then, it seems that you will have to get some more money.")
print("Jackie: I know what we can do! You can play the minigames at Jasmine's Game Emporium to get some more rupees!")

print()
print("a. That's nice. I'd love to play.")
print("b. That sounds terrible. I hate minigames.")
print("c. I have no opinion on this.")
going_to_Jasmine = input("How does that idea sound?")
print()

if going_to_Jasmine == "a":
  print("Erica: I knew you'd like it!")

if going_to_Jasmine == "b":
  print("Erica: Oh, be quiet. You don't have much of a choice.")

if going_to_Jasmine == "c":
  print("Erica: Well then, we'll decide for you. After all, you have to impress the princess.")

print("Jackie: Off you go to Jasmine's Game Emporium! Go on and win, " + name + "!!")
print("Erica: Win at least 150 rupees, okay " + name + "? That way we can buy the princess a proper gift.")
print("Your goal is 150 rupees. Good luck, hero.")
print()
time.sleep(2)

# end of introduction

print("Here you find yourself in Jasmine's Game Emporium.")
print()

print("Jasmine: Ah, " + name + "! How good it is to see you! Are you here to win some prizes?")
print("Jasmine: What’s that? You need to get money to buy the princess a gift? Well, that’s perfect! Step right up, " + name + ", and play one of Jasmine’s games!")
print()

# begin defining main function of the program
def jasmine_main_menu():
  '''
  Central menu with all the minigame options

  Prints all the minigame options available for user for them to select to proceed

  Parameters
  ----------
  none
  
  Returns
  ----------
  none
  '''
  print()
  print()
  print("JASMINE GAME EMPORIUM MENU")
  print()
  print("1. Arithmetic Game")
  print("2. Guess the Animal")
  print("3. Cho Han Bakuchi (Odd or Even Dice Game)")
  print("4. Hangman")
  print("5. Fighting a monster!")
  print("6. Guess the Place")
  print("7. Unscrambling words")
  print("8. ???")
  print()

  return

# the assertion below will break, because the function is void
# assert jasmine_main_menu() == "JASMINE GAME EMPORIUM MENU", 'Function is void; expected no return'

# user can only play a total of 3 minigames
minigame_limit = 3

def rupee_awarder(rupees_awarded):
  '''
  Awards rupees to the user if they win the games manifested in any of the minigame functions.

  If the user wins any minigame, they are awarded with a set number of rupees. This would change the rupee variable value and congratulate the user. This action must be considered several times throughout the program, and hence, in the interest of facilitating the programming process, will only be done once here. 

  Parameters
  ----------
  rupees_awarded : integer
    The value of rupees won by the user, which is added to the initial rupee value to recieve the returned rupee value. 

  Returns
  ----------
  string
    A message congratulating the user and the final rupee variable value after the user has won the given minigame. 
  '''

  # Python assumes that variables are local unless otherwise specified, and this variable rupees is meant to be the global variable, not a local one. 
  global rupees 

  rupees = rupees + rupees_awarded

  return ("Jasmine: Congratulations! You have won " + str(rupees_awarded) + " rupees for winning the game!! You now have " + str(rupees) + " rupees.") 

rupee_awarder_check = rupee_awarder(20)

# the assertion below will break, because the function returns a message about winning and the rupee value
# assert rupee_awarder(20) == "Jasmine: Congratulations! You have won." , "Expected message to user about rupees"

# the assertion below will work and not show an error, but has been commented out
# assert isinstance (rupee_awarder_check, str), 'Expects a string in the form of a message to the user'

# the assertion below will break, since the function returns a string
# assert isinstance (rupee_awarder_check, int), 'Expects a string in the form of a message to the user'

def arithmetic_game():
  '''
  Simple Arithmetic computation game

  User is asked 3 questions related to adding, subtracting, multiplying, or dividing numbers. If the user is correct all 3 times, they are returned with an increase in the rupees variable. 

  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''

  print("You selected the Arithmetic Game!")
  print()
  
  print("Jasmine: Excellent choice! Alright, let's begin.")
  time.sleep(1)

  arithmetic_game_points = 0

  first_arithmetic_answer = int(input(("Jasmine: Here is your first question. What is 53 plus -26?")))
  print()

  if first_arithmetic_answer == int(53+-26):
    print("Jasmine: Incredible! You got the answer, well done, " + name + ".")
    arithmetic_game_points = arithmetic_game_points + 1

  else:
    print("Jasmine: Nope, that's not correct.")

  print()
  second_arithmetic_answer = int(input("Jasmine: Alright, here's your second question. What is 19 times 34?"))

  if second_arithmetic_answer == int(19*34):
    print("Jasmine: Wow, great job, " + name + "! That's correct.")
    arithmetic_game_points = arithmetic_game_points + 1

  else: 
    print("Jasmine: No, that's not correct.")
  
  print()
  third_arithmetic_answer = int(input("Jasmine: Now for your last question! What is 1512 divided by 28?"))

  if third_arithmetic_answer == int(1512/28):
    print("Jasmine: Correct! I knew you'd get it, " + name + "!")
    arithmetic_game_points = arithmetic_game_points + 1
  
  else:
    print("Jasmine: Oh no, " + name + "... I'm afraid that's not correct.")
  
  if arithmetic_game_points == 3:
    print()
    print (rupee_awarder(50))
    print()
  if arithmetic_game_points != 3:
    print()
    print("Jasmine: Oh dear. " + name + ", I'm afraid you got " + str(arithmetic_game_points) + "points. You lose the game.")
  
  print("Jasmine: The Arithmetic Game is now over.")
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()

  return

def guess_the_animal(): 
  '''
  User attempts to guess a mystery animal using hints from yes or no questions

  Mystery animal is set, and then user selects from given questions, to which answers are returned as hints. If the user guesses the mystery animal correctly, an increase in the rupee variable is returned. 
  
  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''
  
  print("You selected Guess the Animal!")
  print()
  print("Jasmine: Okay, I will think of an animal, and you must guess what the animal is by asking me three yes or no questions.")

  mystery_animal = str("raccoon")
  print()

  print("Jasmine: I've thought of an animal! Try guessing what it is.")
  print()
  print("a. Is it a mammal?")
  print("b. Does it have feet?")
  print("c. Is it loud?")
  print("d. Does it make platypus noises?")
  print()

  first_question = input("Which question would you like to ask?")

  if first_question == "a":
    print()
    print("Jasmine: Yes, it is a mammal!")
  
  if first_question == "b":
    print()
    print("Jasmine: Yes, of course it does.")

  if first_question == "c":
    print()
    print("Jasmine: It is only loud when it desires to be. <3")
  
  if first_question == "d":
    print()
    print("Jasmine: No, but I know someone that does.")
  
  print()
  print("Jasmine: Go ahead and guess the animal. It's okay if you don't get it, because you still have two more questions to ask.")
  print()

  first_guess = input("What do you think the mystery animal is?")

  if first_guess == mystery_animal:
    print("Jasmine: Incredible!! You got it right!")
    print()
    print (rupee_awarder(60))
    print()
  
  else: 
    print("Jasmine: I'm sorry, " + name + ", you'll have to keep trying.")
    print()

    print("Jasmine: Try asking another question!")
    print("a. Does it have a big nose?")
    print("b. Can it climb trees?")
    print("c. Can it fly?")
    print("d. Does it have five fingers?")
    print()

    second_question = input("Which question would you like to ask?")

    if second_question == "a":
      print()
      print("Jasmine: No, it does not.")
      print()

    if second_question == "b":
      print()
      print("Jasmine: Yes, and very well at that!")
    
    if second_question == "c":
      print()
      print("Jasmine: No, it cannot fly.")
    
    if second_question == "d":
      print()
      print("Jasmine: Yes, it does have five fingers!")
    
    print()
    print("Jasmine: Go ahead and guess the animal. It's okay if you don't get it, because you still have one more question to ask.")
    print()

    second_guess = input("What do you think the mystery animal is?")

    if second_guess == mystery_animal:
      print("Jasmine: Incredible! You got it right!")
      print()
      print(rupee_awarder(60))
      print()
    
    else:
      print("Jasmine: I'm sorry, " + name + ", you'll have to keep trying.")
      print()

      print("Jasmine: Try asking another question!")
      print("a. Is it fluffy?")
      print("b. Does it eat people?")
      print("c. Does it like cotton candy?")
      print("d. Does it like cleaning its food?")
      print()

      third_question = input("Which question would you like to ask?")

      if third_question == "a":
        print()
        print("Jasmine: Oh yes, it's very fluffy!")
      
      if third_question == "b":
        print()
        print("Jasmine: No, silly! It doesn't eat people!")
      
      if third_question == "c":
        print()
        print("Jasmine: Yes, it loves cotton candy!")
      
      if third_question == "d":
        print()
        print("Jasmine: Yes, it loves to clean its food, even though that may have disastorous consequences.")
      
      print()
      print("Go ahead and guess the animal. This is your last chance, so answer carefully!")
      print()

      third_guess = input("What do you think the mystery animal is?")
      
      if third_guess == mystery_animal:
        print("Jasmine: Incredible! You got it right!")
        print()
        print(rupee_awarder(60))
        print()
      
      else: 
        print("Jasmine: I'm sorry, but that's still not correct, and that's the end of the game.")
        print()
        
  print("Jasmine: The Guess the Animal game is now over.")
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()
    
  return

def cho_han_bakuchi():
  '''
  User guesses whether or not the sum of the results of two dice rolls will be odd or even.

  User guesses odd or even, and then 2 random integers from 1 to 6, inclusive, are generated. If the sum of these integers matches the user's guess, they are returned with an increase in the rupee variable value. 

  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''

  print("You selected Cho Han Bakuchi, the odd or even dice game!")
  print()

  print("Jasmine: Good choice! Alright, I will explain how the game works. Before I roll two dice, you guess whether their sum will be odd or even. If your guess matches the sum of the two dice, you win! Go ahead and guess.")
  print()

  print("a. Odd")
  print("b. Even")
  cho_han_guess = input("Which one do you guess?")
  print()

  if cho_han_guess == "a":
    print("Jasmine: You guessed odd? I’m going to roll the dice now!")
    cho_han_guess_value = 1
    print()
  
  if cho_han_guess == "b":
    print("Jasmine: You guessed even? I’m going to roll the dice now!")
    cho_han_guess_value = 0
    print()
  
  import random
  cho_han_first = random.randint(1,6)
  cho_han_second = random.randint(1,6)

  print("The numbers on the dice are " + str(cho_han_first) + " and " + str(cho_han_second) + ".")
  print()

  cho_han_result = cho_han_first + cho_han_second

  print("Jasmine: That adds up to " + str(cho_han_result) + "!")

  if (cho_han_result%2) == cho_han_guess_value:
    print()
    print (rupee_awarder(40))
    print()
  
  else: 
    print()
    print("Jasmine: I'm sorry, but you lost the game, " + name + "...") 
  
  print("Jasmine: The Cho Han Bakuchi game is now over.")
  print("You have " + str(rupees) + " rupees.")

  jasmine_main_menu()

  global minigame_limit
  minigame_limit = minigame_limit - 1

  return

def hangman():
  '''
  User tries to guess a mystery word by guessing its letters in a set number of attempts.

  User guesses letters of a given mystery word, which are then outputted. If the user guesses all the letters within 10 attempts, they are returned with an increase in the rupee variable.

  Parameters
  ----------
  none
  
  Returns
  ----------
  none
  '''
  print("You selected Hangman!")
  print()

  print("Jasmine: Alright, now I will think of a word, and you will have to guess all the letters of that word in 10 tries. The number of tries only goes down if you get a letter wrong. If you guess a letter that you have already guessed before, your number of attempts does not go down. Good luck!")
  print()

  secret_word = str("incendio")
  print("Jasmine: The word I am thinking of has " + str(len(secret_word)) + " letters!")

  guess_storage = ""
  attempts = 10

  while attempts > 0:
    blank_spaces = 0

    for letter in secret_word:
      if letter in guess_storage:
        print (str(letter))
      
      else: 
        print("-")
        blank_spaces = blank_spaces + 1

    if blank_spaces == 0:
      print()
      print(rupee_awarder(80))
      print()
      break
    
    guess = input("Jasmine: Try guessing a letter in the word!")

    guess_storage = guess + guess_storage
    if guess not in secret_word:
      attempts = attempts - 1
      print("Jasmine: That letter is not in the word I am thinking of!")
    
    print ("Jasmine: You still have " + str(attempts) + " tries left. Guess carefully!")

    if attempts == 0:
      print("Jasmine: I'm sorry, but you didn't get the word in 10 tries. The word was actually incendio!")

  print("Jasmine: The Hangman Game is now over.")
  print("You have " + str(rupees) + " rupees.")

  jasmine_main_menu()

  global minigame_limit
  minigame_limit = minigame_limit - 1

  return

def fighting_monster():
  '''
  User battles a monster by answering questions about integer and modulo division.

  User must answer questions about integer and modulo division, and if their answers are correct, the monster HP is seen going down. If the answers are incorrect, then the user HP decreases. If the user defeats the monster, they are given an increase in the rupee value.

  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''

  print("You selected the Fighting a Monster Game!")
  print()

  print("Jasmine: Oh? Well then, I shall unleash a monster!!")
  print()

  print("!!! A huge Bullbo comes out of nowhere, and it sure looks angry!")
  print()

  print("Jasmine: Both your HP and the Bullbo HP has been set to 30. I hope you know how to divide, " + name + "!")
  print()

  user_hp = 30
  bullbo_hp = 30

  print("To defeat the Bullbo, you must answer a series of questions.")

  while (user_hp > 0 and bullbo_hp > 0):
    print()
    first_question = int(input("Quickly! What is 365 divided by 11? Round your answer DOWN to the nearest integer!"))

    if first_question == (365//11):
      print("Excellent work! You can see the Bullbo HP decreasing!")
      print()
      for bullbo_hp_down in range (bullbo_hp, bullbo_hp-16, -5):
        print (str(bullbo_hp_down))
      bullbo_hp = bullbo_hp - 15
    
    elif first_question != (365/11): 
      print("Oh no! That's incorrect! Your HP is decreasing!")
      print()
      for user_hp_down in range (user_hp, user_hp-16, -5):
        print (str(user_hp_down))
      user_hp = user_hp - 15
      
    print()
    second_question = int(input("Now, what is the remainder when one divides 365 by 11?"))

    if second_question == (365%11):
      print("Excellent work! You can see the Bullbo HP decreasing!")
      print()
      for bullbo_hp_down in range (bullbo_hp, bullbo_hp-16, -5):
        print (str(bullbo_hp_down))
      bullbo_hp = bullbo_hp - 15
    
    elif second_question != (365%11): 
      print("Oh no! That's incorrect! Your HP is decreasing!")
      print()
      for user_hp_down in range (user_hp, user_hp-16, -5):
        print (str(user_hp_down))
      user_hp = user_hp - 15
    
    print()
    third_question = int(input("Finally, what is 365 divided by 20? Round DOWN to the nearest integer!"))

    if third_question == (365//20):
      print("Excellent work! You can see the Bullbo HP decreasing!")
      print()
      for bullbo_hp_down in range (bullbo_hp, bullbo_hp-16, -5):
        print (str(bullbo_hp_down))
      bullbo_hp = bullbo_hp - 15
    
    elif third_question != (365/20): 
      print("Oh no! That's incorrect! Your HP is decreasing!")
      print()
      for user_hp_down in range (user_hp, user_hp-16, -5):
        print (str(user_hp_down))
      user_hp = user_hp - 15
  
  print()
  print("Jasmine waved her hand, and the bullbo slowly goes back to an invisible corner of the game emporium.")

  if user_hp == 0:
    print()
    print("Jasmine: I'm afraid you lost, " + name + ". But, to be fair, it was certainly difficult.")
  
  if bullbo_hp == 0:
    print()
    print("Jasmine: ...")
    print("Jasmine: That was certainly impressive, " + name + ".")
    print()
    print (rupee_awarder(90))
    print()

  print("Jasmine: The Fighting A Monster game is now over.")
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()
    
  return

def guess_the_place():
  '''
  User guesses a region of Hyrule using answers to yes or no questions.

  The user asks three questions, to which answers are returned that give hints about a given place in Hyrule. If the user guesses the place correctly, they are returned with an increase in the rupee value.

  Parameters
  ----------
  none
  
  Returns
  ----------
  none
  '''
  print("You selected Guess the Place!")
  print()
  print("Jasmine: Now, I will think of some place in Hyrule, and you have to guess what it is by asking me three yes or no questions. Here we go.")

  mystery_place = str("Hyrule Castle Town")
  print()

  print("Jasmine: I've thought of a region in Hyrule! Try guessing what it is.")
  print()
  print("a. Is it home to Princess Agitha?")
  print("b. Are there Gorons there?")
  print("c. Is it a rural place?")
  print("d. Does it have Zora people?")
  print()

  first_question = input("Which question would you like to ask?")

  if first_question == "a":
    print()
    print("Jasmine: Yes, it is! You can sell her golden bugs there for lots of rupees!")
  
  if first_question == "b":
    print()
    print("Jasmine: Yes, the Gorons often sell hot spring water and other goods there.")

  if first_question == "c":
    print()
    print("Jasmine: No, it is probably the least rural region in Hyrule.")
  
  if first_question == "d":
    print()
    print("Jasmine: No, Zora people rarely visit this region. ")
  
  print()
  print("Jasmine: Go ahead and guess the place I'm thinking of. It's okay if you don't get it, because you still have two more questions to ask.")
  print()

  first_guess = input("What do you think the mystery place is?")

  if first_guess == mystery_place:
    print("Jasmine: Incredible!! You got it right!")
    print()
    print (rupee_awarder(60))
    print()
  
  else: 
    print("Jasmine: I'm sorry, " + name + ", you'll have to keep trying.")
    print()

    print("Jasmine: Try asking another question!")
    print("a. Is the Princess of Hyrule there?")
    print("b. Is Malo Mart there?")
    print("c. Is it south of Ordon Village?")
    print("d. Can you get your shoes polished there?")
    print()

    second_question = input("Which question would you like to ask?")

    if second_question == "a":
      print()
      print("Jasmine: Yes, she is!")
      print()

    if second_question == "b":
      print()
      print("Jasmine: Yes, but only after you donate a thousand rupees for them to build a franchise there.")
    
    if second_question == "c":
      print()
      print("Jasmine: Nope, it's not south of it.")
    
    if second_question == "d":
      print()
      print("Jasmine: Yes, I know a boy there who will shine your shoes for 10 rupees.")
    
    print()
    print("Jasmine: Go ahead and guess the place. It's okay if you don't get it, because you still have one more question to ask.")
    print()

    second_guess = input("What do you think the mystery place is?")

    if second_guess == mystery_place:
      print("Jasmine: Incredible! You got it right!")
      print()
      print(rupee_awarder(60))
      print()
    
    else:
      print("Jasmine: I'm sorry, " + name + ", you'll have to keep trying.")
      print()

      print("Jasmine: Try asking another question!")
      print("a. Can you give charity there?")
      print("b. Is it beside Lake Hylia?")
      print("c. Can you get your fortune read there?")
      print("d. Are there lots of cats there?")
      print()

      third_question = input("Which question would you like to ask?")

      if third_question == "a":
        print()
        print("Jasmine: Yes; an old sage asks you for donations and wishes you love, though they say if you donate enough, he will give you a heart piece.")
      
      if third_question == "b":
        print()
        print("Jasmine: Nope, it's not beside Lake Hylia.")
      
      if third_question == "c":
        print()
        print("Jasmine: Yes, but the legitimacy of the readings is questionable.")
      
      if third_question == "d":
        print()
        print("Jasmine: Oh yes! You can pick them up and they are just small and fluffy and squish.")
      
      print()
      print("Go ahead and guess the place. This is your last chance, so answer carefully!")
      print()

      third_guess = input("What do you think the mystery animal is?")
      
      if third_guess == mystery_place:
        print("Jasmine: Incredible! You got it right!")
        print()
        print(rupee_awarder(60))
        print()
        
  print("Jasmine: The Guess the Place game is now over.")
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()
    
  return

def unscrambling_words():
  '''
  User unscrambles the letters in given words.

  User is asked to unscramble the letters in three given words. If the user answers two out of three correctly, they are returned an increase in the rupee value.

  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''
  print("You have selected the Unscrambling Words Game!")
  print()

  print("Jasmine: Now, I shall show you a word with its letters scrambled, and you have to tell me the unscrambled word. They are hard to guess, and we shall see how you do. If you get 2 out of 3 words correct, you wil get a prize! Remember to answer in ALL CAPITALS!!")

  first_word = str(APHRODITE)
  second_word = str(HIEROGLYPHICS)
  third_word = str(MOZZARELLA)
  unscrambling_points = 0

  print()
  first_word_guess = input("Jasmine: What do you think this word is? HARPTDOEI") 
  print()

  if first_word_guess == first_word:
    print("Jasmine: Amazing! You got it right!")
    unscrambling_points = unscrambling_points + 1
  
  else:
    print("Jasmine: No, I'm afraid that's not correct.")
  
  print()
  second_word_guess = input("Jasmine: What do you think this word is? PCIEYRSGOLHHI") 
  print()

  if second_word_guess == second_word:
    print("Jasmine: Amazing! You got it right!")
    unscrambling_points = unscrambling_points + 1
  
  else:
    print("Jasmine: No, I'm afraid that's not correct.")
  
  print()
  third_word_guess = input("Jasmine: What do you think this word is? PCIEYRSGOLHHI") 
  print()

  if third_word_guess == third_word:
    print("Jasmine: Amazing! You got it right!")
    unscrambling_points = unscrambling_points + 1
  
  else:
    print("Jasmine: No, I'm afraid that's not correct.")
  
  if unscrambling_points >= 2:
    print()
    print("Jasmine: You did it! You won the Unscrambling Game.")
    print()
    print(rupee_awarder(80))
    print()

  else: 
    print()
    print("Jasmine: I'm sorry, " + name + ", but you didn't win the game...")
  
  print("Jasmine: The Unscrambling Words game is now over.")
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()
    
  return

def communist_propaganda():
  '''
  User is given a choice as to whether or not they are willing to chant propaganda repeatedly.

  User is asked whether or not they will chant propaganda slogans, equal in magnitude to their rupee count plus five. If the user agrees to this, they are returned with an increase in the rupee value. 

  Parameters
  ----------
  none

  Returns
  ----------
  none
  '''

  print("Jasmine looks around the Emporium to make sure no one is there.")
  print()
  
  time.sleep(2)
  print("Jasmine: ...")
  print("Jasmine: " + name + ", I've been raised in Ordon Village, and know everything about it. However, this village doesn't know something about me.")
  print("Jasmine: I'm telling you, this whole Hyrule princess and monarchy thing is some wacked out conspiracy. I have seen passed these lies, and have discovered the truth.")
  print()

  time.sleep(2)
  print("Jasmine: The true answer is communism. There can be no other system.")
  print()

  time.sleep(2)
  print("Jasmine: If you help me, I will pay you well.")
  print()

  print("a. Yes")
  print("b. No")
  supporting_communism = input("Will you help Jasmine?")
  print()

  if supporting_communism == "a":
    print("Jasmine: I knew I could count on your help. Now go, " + name + "! Go and tell the people of our system!")
    print()
    
    print("You go out into the streets of Ordon Village, and scream at the top of your lungs:")

    for screaming_in_streets in range (0, rupees+5, 1):
      print("THE GENTLE LABOURER SHALL NO LONGER SUFFER.")
      print("WORKERS OF HYRULE, UNITE!")
      print("YOU HAVE NOTHING TO LOSE BUT YOUR CHAINS!")
      print()

    print("You go back inside to Jasmine's Game Emporium.")
    print()

    print("Jasmine: Well done, " + name + ". Though the people might not listen, I shall reward you regardless.")
    print()
    print (rupee_awarder(100))
    print()
    
  elif supporting_communism == "b":
    print()
    print("Jasmine: Oh? Well, I trust that you will stay silent about my opinions then.")
    print()
  
  print("You have " + str(rupees) + " rupees.")

  global minigame_limit
  minigame_limit = minigame_limit - 1

  jasmine_main_menu()

  return

# actually runs the main menu function
jasmine_main_menu()

while minigame_limit > 0:
  minigame_choice = int(input("Which minigame would you like to play? You can play a total of 3 minigames."))
  print()
  print()

  if minigame_choice == 1:
    arithmetic_game()

  if minigame_choice == 2:
    guess_the_animal()
  
  if minigame_choice == 3:
    cho_han_bakuchi()

  if minigame_choice == 4:
    hangman()
  
  if minigame_choice == 5:
    fighting_monster()
  
  if minigame_choice == 6:
    guess_the_place()
  
  if minigame_choice == 7:
    unscrambling_words()
  
  if minigame_choice == 8:
    communist_propaganda()

if minigame_limit == 0:
  print("Jasmine: Now hold on just a minute! You've already played 3 minigames. That means you've played enough for today.")
  print("Jasmine: Alright, see you later then, " + name + ".")
  print()

  comments = input("Do you have anything to say to Jasmine as you leave?")

  print("You are now outside.")
  print()

  print("Jackie: " + name + "!! Did you win 150 rupees?!")
  print("You show Jackie a total of " + str(rupees) + " rupees.")
  print()

  if rupees >= 150:
    print("Jackie: Did you get enough rupees? Yes? Hooray! You did it, we knew you could!!")
    print()

    time.sleep(2)
    print("Erica runs to you both from the Ordon Village entrance.")
    print()

    print("Erica: The princess is coming!! I saw her from the village gates!!!")
    print("Erica: Do you have 150 rupees? You do? Hooray!! Here, I have the perfect gift you can buy: a raccoon with a bow made of cotton candy!!")
    print()

    time.sleep(2)
    print("Erica: I have to give you " + str(rupees-150) + " rupees in change.")
    print()
    print("You got the cute racoon with a bow made of cotton candy!")
    print()

    print("Jackie: Awww, he's so cute.")

    time.sleep(2)
    print("Erica: The princess is here! Quick, everyone, your presents!")
    print()

    print("The princess, in her carriage with Hylian guards behind her, steps down to greet the people of Ordon Village.")
    print()

    print("Erica: Princess of Hyrule, we welcome you to Ordon Village. We have all prepared gifts for your birthday!")
    print()

    print("Princess Kavya: Oh, thank you! That's so kind of you.")
    print()

    time.sleep(4)
    print("Jasmine gives the princess a yellow and black scarf.")
    print("Princess Kavya: Thank you so much! The colors are so pretty. <3")
    print()

    time.sleep(2)
    print("Jackie gives the princess a stone tablet with ancient runes on it.")
    print("Princess Kavya: This is amazing! I can't even read the runes since they are so small! This should be an artifact.")
    print()

    time.sleep(2)
    print("Erica gives the princess a bouquet of flowers.")
    print("Princess Kavya: How pretty! They smell so nice.")
    print()

    time.sleep(3)
    print("You give the princess a raccoon with a bow made of cotton candy.")
    print("Princess Kavya: A raccoon, with a bow of cotton candy? Wow!! He's so cute~~~ 	(ﾉ´ヮ`)ﾉ*: ･ﾟ")
    print()

    time.sleep(4)
    print("Princess Kavya: " + name + ", this is the best present I've ever gotten! And now, to give you something in return:")

    print()
    print("You got the green Hero's cap!")
    print()

    print("Princess Kavya: I hope you like it, " + name + "! It is the cap that must be worn by the Hero of Hyrule.")
    print()

    time.sleep(5)
    print("And so, the Hero of Hyrule made the Princess' birthday the best one she had ever had. Good work, hero.")
    print()

    print("Farewell, " + name + ". Your adventure will continue in another assignment.")
    print("GAME OVER")
  
  if rupees < 150:
    print("Jackie: " + name + "!! Did you get enough rupees? No? Oh no, this is terrible!")
    print()

    time.sleep(2)
    print("Erica runs to you both from the Ordon Village entrance.")
    print()

    print("Erica: The princess is coming!! I saw her from the village gates!!!")
    print("Erica: Do you have 150 rupees? You don't? Oh no, what will you get the princess now?!?!")
    print()

    time.sleep(2)
    print("Erica: AAAAAAAA!!! The princess is here! Quick, everyone, your presents!")
    print()

    print("The princess, in her carriage with Hylian guards behind her, steps down to greet the people of Ordon Village.")
    print()

    print("Erica: Princess of Hyrule, we welcome you to Ordon Village. Almost all of us have prepared gifts for your birthday!")
    print()

    print("Princess Kavya: Oh, thank you! That's so kind of you.")
    print()

    time.sleep(4)
    print("Jasmine gives the princess a yellow and black scarf.")
    print("Princess Kavya: Thank you so much! The colors are so pretty. <3")
    print()

    time.sleep(2)
    print("Jackie gives the princess a stone tablet with ancient runes on it.")
    print("Princess Kavya: This is amazing! I can't even read the runes since they are so small! This should be an artifact.")

    time.sleep(2)
    print("Erica gives the princess a bouquet of flowers.")
    print("Princess Kavya: How pretty! They smell so nice.")

    time.sleep(3)
    print("You stare at the princess with less emotion than a brick.")
    print()

    print("Erica: Your Highness, please forgive " + name + ". They could not get you a gift.")

    time.sleep(4)
    print("Princess Kavya: It's quite alright. This is still a very nice birthday, thanks to all of you. <3")

    time.sleep(5)
    print("And so, the Hero of Hyrule ate too much milk and cheese to be able to get the princess a present. Oh well, at least she wasn't angry about it. Good work, hero.")
    print()

    print("Farewell, " + name + ". Your adventure will continue in another assignment.")
    print("GAME OVER")
