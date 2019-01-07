#-----------------------------------------------------------------------------
# Name:       Challenge3 (Challenge3.py)
# Purpose:    Preparation for completing Assignment 2	
#
# Author:      vonlugersbutter
# Created:     Saturday, December 29, 2018
# Updated:     Sunday, January 6, 2019
#-----------------------------------------------------------------------------
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

print('All output is shown on output.txt.')

hamlet_file = open('hamlet.txt', 'r')
hamlet_file_contents = hamlet_file.readlines()
hamlet_file.close()

def add_all_numbers(file_contents):
  '''
  Returns sum of all numbers in file

  Identifies all numbers in the given file, and then finds and returns their sum

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	integer
		The sum of all the numbers in the file

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned sum is not an integer
	'''
  
  if not isinstance(file_contents, list):
    raise TypeError('The file contents are not a list, as expected.')

  sum_of_numbers = 0
  for lines in file_contents:
    for character in lines:
      if character.isdecimal():
        sum_of_numbers = sum_of_numbers + int(character)
  
  logging.debug(sum_of_numbers)
  
  if not isinstance(sum_of_numbers, int):
    raise TypeError('The sum of numbers in the file is not an integer, as expected.')
  
  return sum_of_numbers

numbers = ("The sum of all the numbers in Shakespeare's Hamlet is " + str(add_all_numbers(hamlet_file_contents)) + ".")

logging.debug(numbers)

file = open('output.txt', 'w')
file.write(numbers + "\n")
file.close()

def count_vowels(file_contents):
  '''
  Returns the number of vowels in file

  Identifies all vowels in the given file, and then returns how many there are

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	integer
		The number of vowels in the file

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned value is not an integer
	'''
	
	if not isinstance(file_contents, list):
	  raise TypeError('File contents were not in a list, as expected.')
	
  sum_of_vowels = 0 
  vowels = 'aeiouy'
  vowel_list = list(vowels)
  
  logging.debug(vowel_list)
  
  for lines in file_contents:
    for character in lines:
      if character in vowel_list:
        sum_of_vowels = sum_of_vowels + 1 
  
  logging.debug(sum_of_vowels)
  
  if not isinstance(sum_of_vowels, int):
    raise TypeError('The number of vowels is not an integer, as expected.')
  
  return sum_of_vowels

vowels_message = ("The total number of vowels in Shakespeare's Hamlet is " + str(count_vowels(hamlet_file_contents)) + ".")

logging.debug(vowels_message)

file = open('output.txt', 'a')
file.write(vowels_message + "\n")
file.close()

def count_consonants(file_contents):
  '''
  Returns the number of consonants in file

  Identifies all consonants in the given file, and then returns how many there are

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	integer
		The number of consonants in the file

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned value is not an integer
	'''
	
	if not isinstance(file_contents, list):
	  raise TypeError('The file contents are not in a list, as expected.')
	
  sum_of_consonants = 0 
  consonants = 'bcdfghjklmnpqrstvwxz'
  consonant_list = list(consonants)
  
  logging.debug(consonant_list)
  
  for lines in file_contents:
    for character in lines:
      if character in consonant_list:
        sum_of_consonants = sum_of_consonants + 1 
  
  if not isinstance(sum_of_consonants, int):
    raise TypeError('The number of consonants found was not an integer, as expected.')
  
  return sum_of_consonants

consonant_message = ("The total number of consonants in Shakespeare's Hamlet is " + str(count_consonants(hamlet_file_contents)) + ".")

file = open('output.txt', 'a')
file.write(consonant_message + "\n")
file.close()

def count_nonalphanum(file_contents):
  '''
  Returns the number of non-letter or number characters in file

  Identifies all the characters in the given file that are not either letters or numbers, and then returns how many there are

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	integer
		The number of non-alphanumeric characters in the file

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned value is not an integer
	'''
	if not isinstance(file_contents, list):
	  raise TypeError('File contents are not in the form of a list, as expected.')
	
  sum_of_nonalphanum = 0 
  for lines in file_contents:
    for character in lines:
      if not character.isalnum():
        sum_of_nonalphanum = sum_of_nonalphanum + 1 
        
  logging.debug(sum_of_nonalphanum)
  
  if not isinstance(sum_of_nonalphanum, int):
    raise TypeError('The number of non-alphanumeric characters is not an integer, as expected.')
  
  return sum_of_nonalphanum

nonalphanum_message = ("The total number of characters that are not letters or numbers in Shakespeare's Hamlet is " + str(count_nonalphanum(hamlet_file_contents)) + ".")

file = open('output.txt', 'a')
file.write(nonalphanum_message + "\n")
file.close()

def find_last_letter(file_contents):
  '''
  Returns the last letter in every line of the file

  Takes that last characters from every line, and continues to check upstream of the line until it finds the last letter, which it returns in a list

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	list
		List of all the last letters in every line of the file

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned value is not an list
	'''
	if not isinstance(file_contents, list):
	  raise TypeError('File contents are not in the form of a list, as expected.')
	
  last_letters = []
  unneeded_characters = ['\n','!','?','.',',', ' ']
  for line in file_contents:
    if len(line) > 1:
      if (line[-1]).isalpha:
        last_letters.append(line[-1])
      if (line[-2]) in unneeded_characters:
        last_letters.append(line[-3])
  logging.debug(last_letters)
  
  if not isinstance(last_letters, list):
    raise TypeError('The returned list of last letters is not a list, as expected.')
  
  return last_letters

last_letter_word = ' '.join(find_last_letter(hamlet_file_contents))
last_letter_word = last_letter_word.replace('\n','')

file = open('output.txt', 'a')
file.write("Below is a list of all the letters that end lines in Shakespeare's Hamlet. \n")
file.write(last_letter_word + '\n')
file.close()

def remove_new_lines(file_contents):
'''
Returns file content without new line characters

Finds and deletes any \n characters found in the file content

Parameters
----------
file_contents : list
	The contents of a given file, in the form of a list

Returns
-------
string
	The file contents without the \n character

Raises
------
TypeError
	If the file contents parameter is not a list
	If the returned value is not a string
'''
  if not isinstance(file_contents, list):
    raise TypeError('The file contents are not a list, as expected.')
file_contents = ' '.join(file_contents).replace('\n','').split()

for line in file_contents:
  characters = list(line)
  logging.debug(characters)

return file_contents

no_new_line_file = open('hamlet-no-newline.txt', 'w')
for line in remove_new_lines(hamlet_file_contents):
  no_new_line_file.write(line)
no_new_line_file.close()

def sort_alpha_lines(file_contents):
  '''
    Sorts all lines in file by alphabetical order
  
    Sorts the lines in a given line using their first letter, which is then returned as a list of all the lines.
  
    Parameters
  	----------
  	file_contents : list
  		The contents of a given file, in the form of a list
  
  	Returns
  	-------
  	list
  		All the lines in the original file, but in alphabetical order
  
    Raises
  	------
  	TypeError
  		If the file contents parameter is not a list
  		If the returned file is not a list
  	'''
    
    if not isinstance(file_contents, list):
      raise TypeError('The file contents are not a list, as expected.')

  file_contents.sort()
  
  logging.debug(file_contents)
  
  if not isinstance(file_contents, list):
    raise TypeError('Function did not return a list, as expected.')
  
  return file_contents
  
alpha_line_file = open('hamlet-alpha-by-line.txt', 'w')
for line in sort_alpha_lines(hamlet_file_contents):
  alpha_line_file.write(line + "\n")
alpha_line_file.close()

def sort_alpha_words(file_contents):
  '''
    Returns all the words in the file in alphabetical order
  
    Sorts all the individual words in a file, and returns them as a list
  
    Parameters
  	----------
  	file_contents : list
  		The contents of a given file, in the form of a list
  
  	Returns
  	-------
  	list
  		All the words in the original file, in alphabetical order
  
    Raises
  	------
  	TypeError
  		If the file contents parameter is not a list
  		If the returned words are not in a list
  	'''
    
  if not isinstance(file_contents, list):
    raise TypeError('The file contents are not a list, as expected.')

  file_contents = ' '.join(file_contents).replace('\n','').lower().split()
  
  file_contents.sort()
  
  logging.debug(file_contents)
  
  if not isinstance(file_contents, list):
    raise TypeError('The returned file contents after alphabetization of words is not in a list, as expected.')
  
  return file_contents

alpha_word_file = open('hamlet-alpha-by-word.txt', 'w')
for line in sort_alpha_words(hamlet_file_contents):
  alpha_word_file.write(line + "\n")
alpha_word_file.close()
  
def group_words_by_letter(file_contents):
  '''
  Groups all of the words in the file by alphabetical order

  Groups all of the words in a file in a dictionary, with the key as the starting letter, and the value as a list of the words

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	dictionary
		The returned dictionary with the words grouped in order

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the returned object is not a dictionary
	'''
  
  if not isinstance(file_contents, list):
    raise TypeError('The file contents are not a list, as expected.')
  
  file_contents = ' '.join(file_contents).replace('\n','').lower().split()
  
  file_contents.sort()
  
  logging.debug(file_contents)

  word_dictionary = {}
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for letter in alphabet:
    list_of_words = []
    for word in file_contents:
      if word.startswith(letter.upper()) or word.startswith(letter.lower()):
        list_of_words.append(word)
        word_dictionary[letter] = list_of_words

  logging.debug(word_dictionary)
  
  if not isinstance(word_dictionary, dict):
    raise TypeError('Returned object of grouping words by letter was not a dictionary, as expected.')
  
  return word_dictionary

file = open('output.txt', 'a')
file.write('Below is a list of all the words in Hamlet, in a dictionary in alphabetical order.')
file.write(group_words_by_letter(hamlet_file_contents))
file.close()

def frequency_of_letter(file_contents, letter):
  '''
  Finds the frequency of a given letter in the file

  Finds the frequency of the letter, given in the parameters, in the given file contents

  Parameters
	----------
	file_contents : list
		The contents of a given file, in the form of a list

	Returns
	-------
	integer
		The frequency in the file of a given letter

  Raises
	------
	TypeError
		If the file contents parameter is not a list
		If the letter parameter is not in the alphabet
		If the returned value is not an integer
	'''
  if not letter.isalpha():
    raise TypeError('Letter entered is not in the alphabet, as required.')
    
  if not isinstance(file_contents, list):
    raise TypeError('File contents are not in a list, as expected.')

  frequency = 0 
  for line in file_contents:
    for character in line:
      if character == letter:
        frequency = frequency + 1 
  logging.debug(frequency)
  
  if not isinstance(frequency, int):
    raise TypeError('Frequency of letter is not an integer, as expected.')
  
  return frequency

file = open('output.txt','a')
file.write("Here is the number of times the letter 'E' shows in Hamlet. \n")
file.write(str(frequency_of_letter(hamlet_file_contents, 'E'))+ '\n')
file.write("And here is the number of times the letter 'e' shows in Hamlet. \n")
file.write(str(frequency_of_letter(hamlet_file_contents, 'e')) + '\n')
file.close()
