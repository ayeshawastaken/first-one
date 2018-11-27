#-----------------------------------------------------------------------------
# Name:        Challenge pre-Exercise 6 (Challenge1.py)
# Purpose:     Challenge assignment with mathematical operations
#
# Author:      vonlugersbutter
# Created:     Thursday, October 18, 2018
# Updated:     Sunday, October 28, 2018
#-----------------------------------------------------------------------------

def menu():
  '''Displays the main menu
  
  '''
  print("MAIN MENU")
  print()
  print("Choose an option below:")
  print("1. Add two integers.")
  print("2. Subtract two integers.")
  print("3. Multiply two integers.")
  print("4. Divide two integers.")
  print("5. Perform number division on two floats.")
  print("6. Odd or even (figure out if the entered value is odd or even).")
  print("7. Count to zero (based on input, count either up or down to zero using a for loop).")
  print("8. Factorial!")
  print("9. nth Triangle Number!")
  print("0. Exit")
  initial_choice = input()
    
  if initial_choice == "1":
    first_add_int = int(input("Choose your first number: "))
    print()
    second_add_int = int(input("Choose your second number: "))
    print()
    print(str(first_add_int) + " + " + str(second_add_int) + " = " + str(first_add_int + second_add_int))
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
    
  
  elif initial_choice == "2":
    first_sub_int = int(input("Choose your first number: "))
    print()
    second_sub_int = int(input("Choose your second number: "))
    print()
    print(str(first_sub_int) + " - " + str(second_sub_int) + " = " + str(first_sub_int - second_sub_int))
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
    
  elif initial_choice == "3":
    first_mult_int = int(input("Choose your first number: "))
    print()
    second_mult_int = int(input("Choose your second number: "))
    print()
    print(str(first_mult_int) + " x " + str(second_mult_int) + " = " + str(first_mult_int * second_mult_int))
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
    
    
  elif initial_choice == "4":
    first_div_int = int(input("Choose your first number: "))
    print()
    second_div_int = int(input("Choose your second number: "))
    print()
    print(str(first_div_int) + " ÷ " + str(second_div_int) + " = " + str(first_div_int / second_div_int))
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "5":
    first_intdiv_int = float(input("Choose your first number: "))
    print()
    second_intdiv_int = float(input("Choose your second number: "))
    print()
    print(str(first_intdiv_int) + " // " + str(second_intdiv_int) + " = " + str(first_intdiv_int // second_intdiv_int))
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "6":
    oddeven_int = float(input("Choose your number: "))
    print()
    if (oddeven_int%2) == 0:
      print("The number is even!!")
    
    elif (oddeven_int%2) == 1:
      print("The number is odd!!")
    
    elif ((oddeven_int%2) != 0) or ((oddeven_int%2) != 1):
      print("The number is neither odd or even!!")
    
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "7":
    count_to_zero = int(input("Choose your number: "))

    if int(count_to_zero) > 0:
      for counting_down in range (count_to_zero, -1, -1):
        print(str(counting_down))
        
    elif int(count_to_zero) < 0:
      for counting_up in range (count_to_zero, 1, 1):
        print(str(counting_up))

    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "8":
    factorial_int = int(input("Choose a number from 0 to 20: "))
    print()
    
    if (factorial_int <= 20) and (factorial_int > 0):
      factorial_result = 1
      while factorial_int >= 1:
        factorial_result = factorial_result * factorial_int
        factorial_int = factorial_int - 1
      print("The factorial is " + str(factorial_result) + ".")
    
    elif factorial_int == 0:
      print("The factorial of 0 is 1.")
    
    else:
      print("Unacceptable input value.")
    
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "9":
    triangle_int = int(input("Choose a number from 0 to 20: "))
    print()
    
    if (triangle_int <= 20) and (triangle_int > 0):
      triangle_result = 1
      while triangle_int > 1:
        triangle_result = triangle_result + triangle_int
        triangle_int = triangle_int - 1
      print("The triangle number is " + str(triangle_result) + ".")
    
    elif triangle_int == 0:
      print("The triangle number of 0 is 0.")
    
    else:
      print("Unacceptable input value.")
    
    print()
    go_back = input("Press enter to go back to the main menu!")
    print("-----------------------------------------------------------------------------")
    menu()
  
  elif initial_choice == "0":
    print()
    print()
    print("Thank you and goodbye.")
  
  return

menu()
