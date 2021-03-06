#-----------------------------------------------------------------------------
# Name:        Exercise 2 (Exercise2.py)
# Purpose:     Introduction to Variables and input
#
# Author:      vonlugersbutter
# Created:     Wednesday, October 10, 2018
# Updated:     Wednesday, October 10, 2018
#-----------------------------------------------------------------------------

#using inputs

description_of_erica = input('Type something about Erica! :')
print('Is this really how you feel about Erica?: ' + description_of_erica)

#adding floats
user_adding_input = input('Pick a number to add to 25!')
print("Here's your answer:")
print(int(user_adding_input)+int(25))
print()
  
view_choice = input("Do you want to see all my work on order of operations? (yes or no)")
if view_choice == 'yes':
  #subtracting floats
  print(30-10)
  
  #multiplying floats
  print(2*5)
  
  #dividing floats
  print(10/5)
  
  #integer division, which only shows the whole number value of the result
  print(13//4)
  
  #modulo operator, which shows the remainder of a quotient
  print(13%4)
  
  #showing the difference between int() and float() => int only includes whole number value
  print(int(3/4))
  print(float(3/4))
  
  print()
  
  #-----------------------------------------------------------------------------
  #finding order of operations
  
  print(3+4*5) #multiplication and division come before addition and subtraction
  print(3-4+1) #addition and subtraction are left to right
  print(12/4*5) #multiplication and division are left to right
  print()

  print(8*5//4)
  print(5//4*8) #multiplication, division, and integer division are left to right
  print()
  
  print(23%11//5)
  print((23%11)//5)
  print(23%(11//5)) #modulo done first
  print(5//23%11)
  print((5//23)%11)
  print(5//(23%11)) #integer division done first
  #multiplication, division, integer division, and modulo operator are all left to right
  print()
  
  print(53//23**2)
  print((53//23)**2)
  print(53//(23**2)) #exponent has higher precedence than the above
  print()
  
  print(3**(1+1)) #brackets have highest precedence
  print()
  
  #-----------------------------------------------------------------------------
  #an equation that uses all of the above operators
  print(int(21%40//5-6+(5**3/9)))
  # = int(21%40//5-6+(125/9))
  # = int(21%40//5-6+13.89)
  # = int(21//5-6+13.89)
  # = int(4-6+13.89)
  # = int(11.89)
  # = 11
  print()
  
  conclusion1 = 'The order of operations is as follows:'
  conclusion2 = 'Brackets'
  conclusion3 = 'Exponents'
  conclusion4 = 'Muliplication, division, integer division, and modulo operator (left to right)'
  conclusion5 = 'Addition and subtraction (left to right)'
  print(conclusion1)
  print(conclusion2)
  print(conclusion3)
  print(conclusion4)
  print(conclusion5)
  
  print()
  print("Alright, I'll do one more operation with you.")
  user_adding_input2 = input('Pick any integer.')
  user_adding_input3 = input("Pick another integer, and I'll divide them")
  print("Here's the answer:")
  print(float(user_adding_input2)/float(user_adding_input3))
  print()
  print("And here's the answer, but without its decimals.")
  print(float(user_adding_input2)//float(user_adding_input3))
  print()
  print("And here's the remainder you get when dividing the two numbers you gave me.")
  print(float(user_adding_input2)%float(user_adding_input3))
  print()
  print("That's all!")
  
  #-----------------------------------------------------------------------------
  print('Thanks for looking at my program!!')
  
if(view_choice) == 'no':
  print("You're no fun. I wanted to show you my program.")
  name = input("What's your name?")
  print("You're mean, "+ name + ".")
  print("Alright, I'll do one more operation with you.")
  user_adding_input2 = input('Pick any integer.')
  user_adding_input3 = input("Pick another integer, and I'll divide them")
  print("Here's the answer:")
  print(float(user_adding_input2)/float(user_adding_input3))
  print()
  print("And here's the answer, but without its decimals.")
  print(float(user_adding_input2)//float(user_adding_input3))
  print()
  print("And here's the remainder you get when dividing the two numbers you gave me.")
  print(float(user_adding_input2)%float(user_adding_input3))
  print()
  print("That's all!")
