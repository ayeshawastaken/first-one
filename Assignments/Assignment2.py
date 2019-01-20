#-----------------------------------------------------------------------------
# Name: Assignment2 (Assignment2.py)
# Purpose: Display understanding of concepts such as string manipulation, files, dictionaries, lists, tuples, and logging
#
# Author: vonlugersbutter
# Created: Monday, January 14, 2019
# Updated: Friday, January 18, 2019
#-----------------------------------------------------------------------------

# References
# Coelho, P. (1992). The Alchemist. (Alan R. Clark). Retrieved January 7, 2019, from http://www.metaphysicspirit.com/books/The%20Alchemist.pdf
# Hinton, S.E. (n.d.). The Outsiders. Retrieved January 7, 2019, from http://nisbah.com/summer_reading/the-outsiders_se_hinton.pdf 
# Saint-Exupéry, A. The Little Prince. Retrieved January, 7, 2019, from http://www.yoanaj.co.il/uploadimages/The_Little_Prince.pdf  

import random

import logging
logging.basicConfig(filename='debug.txt', filemode='w',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

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

stories_file = open('story.txt', 'r')
stories_file_contents = stories_file.readlines()
stories_file.close()

name = input('Ah, I think this may be the last time I ask you this. How long ago it was when I first asked you, but you have always been patient with my forgetfulness. This time, I promise you, I shall not forget. What is your name, hero? ')
logging.debug(name)
print()

print('After you see a segment of text, hit enter to make it continue. ')

print("You sighed softly, and ran your finger across the foggy, cold window. Even the Hero of Hyrule needed some quiet. Straining every movement, you got up from the windowsill, strode slowly to your bookshelf as if in a waking dream.")
input()

print("You smiled imperceptibly at the books on the shelves, finally choosing three. They were your favourite, heavy with the scent of old binding. Paulo Coelho's the Alchemist, Antoine de Saint-Exupery's the Little Prince, and S.E. Hinton's the Outsiders. How nice.")
input()

print("You turned the cover of the Alchemist, and set the first page in place, and read:")

for line in stories_file_contents[0:5]:
  print(line, end='')
input()

print()
print("You hear a loud knock at the door. ")
print("a. Go away! >:( ")
print("b. Erica, if that's you, leave me alone!")
print("c. What?")
at_the_door = input('What do you want to say to whoever is at the door?')
print()

if at_the_door == 'a':
  print("Erica: OPEN UP, " + name.upper() + "!!")

elif at_the_door == 'b':
  print("Erica: >:(")

elif at_the_door == 'c':
  print("Erica: It's me!")

print()
print("You walked up to the door an opened it to see Erica, Jasmine, and Jackie. As they rushed in, Erica started talking to you about how we should play word games.")
print("Jasmine: Oh, are you reading these books? We could play the word games with the words in these books. \n")
input()

print("Jackie: That sounds good! Will you play, " + name + "? \n")

print("a. Sure.")
print("b. No thanks. ")
play_games = input("Which one would you like to pick?")
print()

if play_games == 'a':
  print("Jackie: Okay, let's think of something to play!")

if play_games == 'b':
  print("Erica: >:( ")

print()
print("Jasmine: I have a wheel of 4 year old brie that's been sitting in my closet for a while. Whoever wins can have that. \n")
print("Four year old brie? A connoisseur like you of ancient 3 AM delicacies could never say no. You agreed to play.")

input()

print("Erica: Alright, " + name + ". You get to play 4 games. If you win 3 out of the 4, you get the wheel of brie. Okay? Let's get started.")

input()

minigames_played = 0
minigames_won = 0
try_and_except_file = open('try-and-except.txt','w')

while minigames_played <= 4:
  
  def main_menu():
    '''
    Shows user well-formatted main menu
  
    Shows user list of minigame options that can be selected; used as a home screen for the minigames
  
    Parameters
  	----------
  	None
  
  	Returns
  	-------
  	None
  
    Raises
  	------
  	TypeError
  	  If the user inputs something that has characters that are not numeric
  	ValueError
  		If the user inputs a number that is not within the selection range
  	'''
    main_menu_options = ['1. Word Cho Han Bakuchi', '2. Sort Lines Game', '3. Hangman', '4. Make your own Dictionary', '5. Word Scramble', '6. When did it happen?' , '7. ???']
    
    for item in main_menu_options:
      print(item)
    
    which_game = input("Which minigame would you like to play?")
    for character in which_game:
      if not character.isdecimal():
        raise TypeError('Inputted values were not numeric characters, as expected.')
    
    if not int(which_game) >= 1 and int(which_game) <= 7:
      raise ValueError('Inputted values not in defined range.')
    
    print()
    
    if which_game == '1':
      word_cho_han_bakuchi(stories_file_contents)
    
    elif which_game == '2':
      sort_lines_game(stories_file_contents)
      
    elif which_game == '3':
      hangman(stories_file_contents)
    
    elif which_game == '4':
      make_your_own_dictionary(stories_file_contents)
    
    elif which_game == '5':
      word_scramble(stories_file_contents)
    
    elif which_game == '6':
      when_did_it_happen(stories_file_contents)
    
    elif which_game == '7':
      cannibalism(stories_file_contents)
    
    return
  
  def word_cho_han_bakuchi(file_contents):
    '''
    User guesses if word has odd or even number of letters
  
    Finds number of letters in random letter from file contents, and asks user to guess if the number of letters is odd or even. If the user is correct, an increase in the minigames_won value is executed.
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	Exception
  		If the user enters an input that is not one of the choices
  		If the odd and even calculation goes wrong
  	'''
    print("Jasmine: Ok, so in this game, you guess if a random word from any of the books will have an odd or even number of letters. If you are correct, you get a point! Let's play. \n")
    
    print('a. Odd')
    print('b. Even')
    odd_or_even = input("Which one do you think the number of letters in the word will be?")
    
    if odd_or_even == 'a':
      guess_value = 1
    
    if odd_or_even == 'b':
      guess_value = 0
    
    else:
      raise Exception('Input not from given values.')
    
    file_contents = ' '.join(file_contents).replace('\n','').lower().split()
    if not isinstance(file_contents, list):
      raise TypeError('File contents not in list as expected.')
    
    random_word = file_contents[random.randint(0, len(file_contents))]
    
    print('The random word is ' + random_word + ".")
    
    if not isinstance(len(random_word)%2, int):
      raise Exception('Odd and even calculation went wrong')
    
    if len(random_word)%2 == guess_value:
      print("Jasmine: You guessed right! You win, " + name + "!")
      global minigames_won 
      minigames_won = minigames_won + 1
    
    elif len(random_word)%2 != guess_value:
      print("Jasmine: Oh no, " + name + ". You didn't get it right.")
    
    return game_ender()
  
  def sort_lines_game(file_contents):
    '''
    User guesses if number of words that start with a random letter will be odd or even
  
    Lines that start with a particular letter are appended to a list in the value of a dictionary key of their respective letter. User then guesses if the number of lines under a random key will be odd or even. If user is correct, they are awarded with an increase in the minigames_won value.
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	  If the number of lines in a dictionary value is not an integer
  	Exception
  		If the user enters an input that is not one of the choices
  	'''
    print("Jackie: For this game, I'll take all the lines in the story, and then sort them into little bins, each with a letter on it. So, if one of the lines starts with the letter 'a', it'll go in the 'a' bin. Your job is to guess whether or not the number of lines in a random bin is odd or even. Ok?")
    input()
    
    print("Jackie: Ok, I shall sort the lines into the bins.")
    
    line_bins = {'a':[], 'b':[], 'c':[], 'd':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
    for key in line_bins.keys():
      for line in file_contents:
        if line.startswith(key.upper()) or line.startswith(key.lower()):
          line_bins.get(key,'').append(line)
    
    logging.debug(line_bins)
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)
    random_letter = alphabet_list[random.randint(0, len(alphabet_list) +1 )]
    if not isinstance(file_contents, list):
      raise TypeError('File contents not in list as expected.')
    
    print("Jackie: Alright, now I'm done sorting all the lines into bins. ")
    print("Jackie: What do you think about the number of lines in the bin for the letter " + random_letter + "?")
    
    logging.debug(random_letter)
    
    print('a. Odd')
    print('b. Even')
    odd_or_even = input("Which one do you think the number of lines in the bin will be?")
    
    if odd_or_even == 'a':
      guess_value = 1
    
    elif odd_or_even == 'b':
      guess_value = 0
    
    else:
      raise Exception('Input was not in the choices listed.')
    
    lines_in_random_bin = line_bins.get(random_letter, "")
    
    logging.debug(lines_in_random_bin)
    
    number_of_lines_in_bin = len(lines_in_random_bin)
    
    logging.debug(number_of_lines_in_bin)
    if not isinstance(number_of_lines_in_bin, int):
      raise TypeError("Number of lines in value not an integer as expected.")
    
    print("Jackie: The number of lines in the bin for that letter is " + str(number_of_lines_in_bin) + ".")
    
    if number_of_lines_in_bin%2 == guess_value:
      print("Jackie: You won the game! Good job, " + name + "!")
    
      global minigames_won
      minigames_won = minigames_won + 1
    
    elif number_of_lines_in_bin%2 != guess_value:
      print("Jackie: Oh, " + name + ". You didn't win.")
    
    return game_ender()
  
  def hangman(file_contents):
    '''
    User guesses the letters of a word in a set number of tries.
    
    The number of letters in a random word from the given file contents is shown to the user, and they are asked to guess the letters. If the user guesses a letter in the word, it is shown. If the user guesses the word in 10 tries or less, they are rewarded with an increase in the minigames_won value. 
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	  If the letter entered is not a string
  	  If the letter entered is not a letter 
  	'''
    print("Erica: Let's play hangman! Here, give me the books, and I'll pick a random word from them and give you 10 chances to guess its letters. The chances only get decreased if you get the letter wrong. Let's play! \n")
    
    file_contents = ' '.join(file_contents).replace('\n','').lower().split()
    if not isinstance(file_contents, list):
      raise TypeError('File contents not in list as expected.')
    
    word_is_long = False
    
    while word_is_long == False:
      secret_word = file_contents[random.randint(0, len(file_contents))]
      
      logging.debug(len(secret_word))
      
      if len(secret_word) >= 4:
        word_is_long = True
      
      else:
        word_is_long = False
    
      logging.debug(secret_word)
    
    for character in secret_word:
      if not character.isalpha():
        secret_word = secret_word.replace(character, '')
    
    print("Erica: Ok, I'll make some spaces for you to guess the letters on this nice paper I just found!")
    print("Erica: The word I found has " + str(len(secret_word)) + " letters.")
    
    list_of_previous_guesses = []
    chances = 10
    
    while chances > 0:
      blank_spaces = 0
      
      for letter in secret_word:
        if letter in list_of_previous_guesses:
          print(letter + ' ', end='')
        
        else:
          print('_ ',end='')
          blank_spaces = blank_spaces +1
      
      if blank_spaces == 0:
        print()
        print("Erica: You did it, " + name + "! You won the game!")
        
        global minigames_won
        minigames_won = minigames_won + 1
        break
      
      print()
      print()
      guess = input("Erica: Go ahead and try to guess a letter in the word.")
      if not isinstance(guess, str):
        raise TypeError('Guess is not string as expected.')
      for character in guess:
        if not character.isalpha():
          raise TypeError('Character entered is not a letter.')
      
      if guess in list_of_previous_guesses:
        print("Erica: You've already guessed that letter!")
      
      elif guess not in secret_word:
          chances = chances - 1
          print("Erica: Nope! That's not in the word.")
      
      list_of_previous_guesses.append(guess)
  
      print("Erica: You have " + str(chances)+ " tries left.")
      
      if chances == 0:
        print()
        print("Erica: Heh. You didn't get the word; it was actually " + str(secret_word)+ '.')
    
    return game_ender()
  
  def make_your_own_dictionary(file_contents):
    '''
    User assigns definitions to given words
  
    A dictionary is created using random words from the given file contents and user inputted definitions. The user is then asked to identify a word from its given definition. If the user is correct, they are awarded with an increase in the minigames_won value.
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	Exception
  		If the user enters an input that is not a string
  	'''
    print("Jasmine: Okie so now, you must make a custom dictionary. However, the game will be revealed to you a bit later. Write the definitions for five words. \n")
    input()
    
    definitions = 0
    custom_dictionary = []
    
    while definitions < 5:
      file_contents = ' '.join(file_contents).replace('\n','').lower().split()
      if not isinstance(file_contents, list):
        raise TypeError('File contents were not in list, as expected.')
      
      random_word = file_contents[random.randint(0, len(file_contents))]
      random_word = random_word.lower()
      
      inputted_definition = input('What do you want to write for the definition of this word?: ' + random_word)
      if not isinstance(inputted_definition, str):
        raise TypeError("Inputted information was not in a string, as expected.")
      
      word_definition_tuple = (random_word, inputted_definition)
      logging.debug(word_definition_tuple)
      custom_dictionary.append(word_definition_tuple)
      
      definitions = definitions + 1
      
      logging.debug(definitions)
    
    print("Jasmine: Ok! <3 You've written 5 definitions.")
    print("Jasmine: Now, what is the word that matches this inputted definition? \n")
    
    random_word_definition_pair = custom_dictionary[random.randint(0,len(custom_dictionary) +1 )]
    word, definition = random_word_definition_pair
    print(definition)
    print()
    
    for character in word:
      if not character.isalpha:
        word = word.replace(character, '')
    
    word_guess = input('What do you think the word that corresponds to that definition is? ')
    
    logging.debug(word_guess)
    logging.debug(word)
    
    if word_guess == word:
      print("Jasmine: Wow, " + name + "! You won the game! I'm so proud. <3")
      
      
      global minigames_won
      minigames_won = minigames_won + 1
    
    elif word_guess != word:
      print("Jasmine: Oh no, " + name + "... I'm afraid that's not the right answer. The real word was " + word + ".")
    
    return game_ender()
    
  def word_scramble(file_contents):
    '''
    User unscrambles given words from the file contents
  
    The letters of a random word from the file contents is taken and scrambled randomly. The user must then correctly unscramble 4 out of 5 given words to be awarded with an increase in the minigames_won value.
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	  If the user enters an input that is not a string
  	ValueError
  	  If the length of the word given is too short
  	'''
    print("Jackie: Okay, so I'll get a couple of random words from the stories, and scramble them. You unscramble them. If you get 4 out of the 5 correct, you win!")
    
    words_answered = 0 
    word_scramble_points = 0
    
    while words_answered <= 5:
      file_contents = ' '.join(file_contents).replace('\n',' ').split(' ')
      if not isinstance(file_contents, list):
        raise TypeError('File contents not in list, as expected.')
      
      logging.debug(file_contents)
      random_word = file_contents[random.randint(0, len(file_contents))]
      
      if len(random_word) < 4:
        random_word = file_contents[random.randint(0, len(file_contents))]
      
      elif len(random_word) >= 4:
        random_word.lower()
        
        if not len(random_word) >= 4:
          raise ValueError("Word used to scramble is too short.")
          
        for character in random_word:
          if not character.isalpha():
            random_word = random_word.replace(character,'')
        
        logging.debug(random_word)
        original_word = random_word
    
        random_word = list(random_word)
        random_word_jumbled = random.sample(random_word, len(random_word)) 
        ''.join(random_word_jumbled)
    
        logging.debug(random_word_jumbled)
        
        for item in random_word_jumbled:
          print(item,end='')
    
        print()
        user_guess = input('Jackie: What do you think this word unscrambled is? ')
        if not isinstance(user_guess, str):
          raise TypeError('Inputted value is not string, as expected.')
        
        if user_guess == original_word:
          word_scramble_points = word_scramble_points + 1
          print("\nJackie: Nicely done! You now have " + str(word_scramble_points) + " points.")
        
        elif user_guess != original_word:
          print("\nJackie: Oh, you didn't get that right, " + name + ". ")
          print("You now have " + str(word_scramble_points) + " points.")
        
        print("Jackie: Let's try another word. \n")
        words_answered = words_answered +1
    
    print("Jackie: You've guessed 5 words.")
    
    if word_scramble_points >= 4:
      print("Jackie: You won the game! Good job, " + name + "!")
      global minigames_won
      minigames_won = minigames_won + 1 
    
    elif word_scramble_points < 4:
      print("Jackie: You didn't win the game, " + name + "...")
    
    return game_ender()
    
  def when_did_it_happen():
    '''
    User guesses or lists the dates of important events
  
    A dictionary of important events and their dates is created, from which the user must guess the dates of specific events. If the user gets the dates of 2 out of 3 events correct, they are awarded with an increase in the minigames_won value.
  
    Parameters
  	----------
  	None
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the user enters an input that is not an integer
  	'''
    print("Erica: HON HON HON")
    print("Erica: You have picked the very game I thought you would, and you shall surely be defeated!")
    
    important_events = {"Erica's Birthday" : (22,4,2003),"Tlatelolco Massacre" : (2,10,1968), "Stock Market Crash of 2008" : (29,9,2008),"End of the South African Apartheid" : (27,4,1994),"the Queen signs the Constitution of Canada" : (17,4,1982)}
    print("\nErica: Now, this game has nothing to do with the three books. I have a list of dates of important events in mind. I will give you the name of the event, and you tell me its date. If you get 2 out of 3 of them correct, you win.\n")
    
    dates_answered = 0 
    when_did_it_happen_points = 0
    while dates_answered < 3:
      print("\nErica: When did the following event take place?")
      event = random.choice(list(important_events.keys()))
      print(event)
      
      date_of_event = important_events.get(event, '')
      
      logging.debug(date_of_event)
      
      day,month,year = date_of_event
      
      inputted_day = int(input("Enter the day of the event, like the day of May 5 would be 5: "))
      if not isinstance(inputted_day, int):
        raise TypeError('Inputted value was not an integer, as expected.')
      
      inputted_month = int(input("Enter the month of the event, like the month of May 7 would be 5: "))
      if not isinstance(inputted_month, int):
        raise TypeError('Inputted value was not an integer, as expected.')
        
      inputted_year = int(input("Enter the year of the event, like the year of May 7 2003 would be 2003: "))
      if not isinstance(inputted_year, int):
        raise TypeError('Inputted value was not an integer, as expected.')
        
      print()
    
      if inputted_day == day and inputted_month == month and inputted_year == year:
        when_did_it_happen_points = when_did_it_happen_points + 1 
        print("Erica: You got it right!")
      
      else: 
        print("Erica: Nope, " + name + ". That's not correct.")
      
      if when_did_it_happen_points == 1:
        print("You now have " + str(when_did_it_happen_points) + " point.")
      
      elif when_did_it_happen_points != 1:
        print("You now have " + str(when_did_it_happen_points) + " points.")
      
      del important_events[event]
      dates_answered = dates_answered + 1
    
    print("\nErica: Alright, let's see how many points you got. \n")
    
    if when_did_it_happen_points >= 2:
      print("Erica: You won the game, " + name + "!")
    
      global minigames_won
      minigames_won = minigames_won +1
    
    elif when_did_it_happen_points < 2:
      print("Erica: Nope, hon hon, you didn't win, " + name + "!") 
    return game_ender()
  
  def cannibalism(file_contents):
    '''
    User answers a series of word game problems
  
    User answers three questions based on manual manipulation of words and lines from the given file contents. If the user gets at least 2 out of 3 questions correct, they are awarded with an increase in the minigames_won value.
  
    Parameters
  	----------
  	file_contents : list 
  	  The lines of the content in a given file, organized into a list with each line as a separate item
  
  	Returns
  	-------
  	function
  	  Returns the game ending function, which leads the user into the home screen main menu
  
    Raises
  	------
  	TypeError
  	  If the file contents are not in a list
  	  If the user enters an input that is not a string
  	'''
    print("Jackie: Now, an idea must be explored.")
    print("Erica: Is cannibalism truly viable as a legality?")
    print("Jasmine: It is plausible, since it would solve three global problems that plague mankind... \n")
    print("World Hunger")
    print("Overpopulation")
    print("Ruining the Environment \n")
    
    if not isinstance(file_contents, list):
  	  raise TypeError('File contents are not in list, as expected. ')
    
    input()
    print("Erica: There is only one way to confirm the viability of it. To see if someone can survive with severed limbs.")
    print("The three turn to look at you, and that is the last thing you saw. \n")
    
    print("You wake up and blink. You look around, and see nothing but a huge field. Hyrule field.")
    print("Erica: This is the only way we can test a system leading to the uprise of mankind!")
    input()
    
    print("\nYou see three Morpheels coming towards you, and you run. \n")
    
    user_morpheel_points = 0
    
    reverse_line = file_contents[6]
    logging.debug(reverse_line)
    
    actual_reverse = ''.join(reversed(reverse_line))
    actual_reverse = list(actual_reverse)
    del actual_reverse[0]
    actual_reverse = ''.join(actual_reverse)
    logging.debug(actual_reverse)
    
    print(reverse_line)
    user_reverse = input("Take the line above, and reverse all of its letters and characters. ")
    if not isinstance(user_reverse, str):
      raise TypeError('Inputted information was not a string, as expected. ')
  
    logging.debug(user_reverse)
    
    if actual_reverse == user_reverse:
      print("You dodged one of the Morpheels! Good job not dying.")
      user_morpheel_points = user_morpheel_points + 1
    
    elif actual_reverse != user_reverse:
      print("Well, you almost lost one of your limbs. Keep running!")
    
    ends_with_line = file_contents[8]
    logging.debug(ends_with_line)
    ends_with_line = ends_with_line.split(' ')
    ends_with_word = ends_with_line[1]
    logging.debug(ends_with_word)
    
    print()
    print(ends_with_word)
    user_ends_with = input("\nType in a word that starts with the same letter as the word above ends with. ")
    if not isinstance(user_ends_with, str):
      raise TypeError('Inputted information was not a string, as expected. ')
    
    actual_letter = ends_with_word[-1]
    logging.debug(actual_letter)
    
    if user_ends_with.startswith(actual_letter):
      print("Well done! You got it right and dodged another Morpheel.")
    
      user_morpheel_points = user_morpheel_points + 1
    
    elif not user_ends_with.startswith(actual_letter):
      print("Yikes. An arm almost off.")
    
    uppercase_line = file_contents[3]
    logging.debug(uppercase_line)
    
    print()
    print(uppercase_line)
    
    user_upper = input("Take the line above and capitalize all of its letters. ")
    if not isinstance(user_upper, str):
      raise TypeError('Inputted information was not a string, as expected. ')
    
    uppercase_line = uppercase_line.upper()
    uppercase_line = list(uppercase_line)
    del uppercase_line[-1]
    uppercase_line = ''.join(uppercase_line)
    logging.debug(uppercase_line)
    logging.debug(user_upper)
    print()
    
    if user_upper == uppercase_line:
      print("Nicely done! Another Morpheel dodged.")
    
      user_morpheel_points = user_morpheel_points + 1
    
    elif user_upper != uppercase_line:
      print("Oof. Almost lost an arm there.")
    
    input()
    print("Jasmine stepped in front of the Morpheels, calming them, and slowly led them into Lake Hylia nearby.")
    
    if user_morpheel_points >= 2:
      print("Erica: Well then, we can safely say that cannibalism is a viable idea and that most people would not die under such circumstances. Well done, " + name + "!")
    
      global minigames_won
      minigames_won = minigames_won + 1
    
    elif user_morpheel_points < 2:
      print("Erica: Well, I guess people won't be able to survive with cannibalism as a system. Oh well. You lost the game anyway, " + name + ".")
    
    return game_ender()
  
  def game_ender():
    '''
    Informs user of end of minigame
  
    Shows user that the minigame is over, how many minigames they have won, and how many they have played thus far. Then, the user is returned 
  
    Parameters
  	----------
  	None
  
  	Returns
  	-------
  	function
  	  Returns the main menu function
  
    Raises
  	------
  	TypeError
  	  If the number of minigames won is not an integer
  	  If the number of minigames played is not an integer
  	'''
    global minigames_played
    global minigames_won
    
    if not isinstance(minigames_played, int):
      raise TypeError('Minigame value is not integer, as expected.')
    
    if not isinstance(minigames_won, int):
      raise TypeError('Minigame value is not integer, as expected.')
    
    minigames_played = minigames_played + 1
    print("\nYou have played " + str(minigames_played) + " minigames so far.")
    print("You now have won " + str(minigames_won) + ' minigames.')
    print("The minigame is now over. Press enter to return to the main menu.")
    input()
    
    return main_menu()
  
  try:
    # would break since game_ender() does not use parameters 
    try_and_except_file.write(game_ender(200))
    
    # word_scramble() cannot use strings as parameters
    try_and_except_file.write(word_scramble('yeetus'))
    
    # cannibalism() cannot use integers as parameters, needs a list
    try_and_except_file.write(cannibalism(13))
    
    # the statement below would actually work
    try_and_except_file.write(word_scramble(['Paulo', 'Coelho','is','good','at','writing']))
    
    # the statement below would also work, as hangman() requires lists as parameters
    try_and_except_file.write(hangman(['Paulo', 'Coelho','is','good','at','writing']))
  
  except Exception as e:
    print("One of the tested functions as not run properly: " + str(e))
  
  main_menu()

print("\nErica: Alright. You've played 4 minigames. Let's see how you did.")

if minigames_won >= 3:
  logging.debug(minigames_won)
  
  print("\nJasmine: Good job, " + name + "! You won " + str(minigames_won) + " minigames, so you win the wheel of brie.")
  print("And so, you and the brie went on to become the best of friends. You laughed together, cried together, watched sunsets together...")
  print()
  certification = "This hearby certifies that the Hero of Hyrule has legal rights to this giant piece of brie"
  certification = certification.upper()
  
  logging.debug(certification)
  
  print(certification.center(35,' '))
  congratulation = ("Ordon Village congratulates " + name + "for owning this piece of cheese.")
  print(congratulation.ljust(35,' '))
  
  logging.debug(congratulation)
  
if minigames_won < 3:
  print("\nJasmine: Oh no, " + name + ". You won " + str(minigames_won) + " minigames, so you don't get the wheel of brie.")
  print("Then, as your friends left, you felt a bitter tear slide across your cheek, and it fell softly on the tattered parchment of your books.")

print("Your adventure may not continue after this, hero. Let it be known that though your time in Hyrule was short, it was wonderful all the same. I asked you to awaken, and now I ask you to sleep. Farewell, for we may not see each other again...")
print("\nGAME OVER")
