#-----------------------------------------------------------------------------
# Name:        Exercise 1 (Exercise1.py)
# Purpose:     Show understanding of operators and values
#
# Author:      vonlugersbutter
# Created:     Tuesday, October 9, 2018
# Updated:     Wednesday, October 10, 2018
#-----------------------------------------------------------------------------

#printing words and sentences, as strings
print('Erica is a squish, and she said "Hello" today!')

#adding floats
print(25+25)

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
#the order of operations is as follows:
#brackets
#exponents
#muliplication, division, integer division, and modulo operator (left to right)
#addition and subtraction (left to right)

#an equation that uses all of the above operators
print(int(21%40//5-6+(5**3/9)))
# = int(21%40//5-6+(125/9))
# = int(21%40//5-6+13.89)
# = int(21//5-6+13.89)
# = int(4-6+13.89)
# = int(11.89)
# = 11
#-----------------------------------------------------------------------------
