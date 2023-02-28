######################################
# IT 2750 - Lab 01                   #
# Hello from python!                 #
# Author:  Arlind Prifti             #
######################################

####################################################
# Part 1: Creating variables and using expressions #
####################################################

# Create two variables. Make one equal to 67 and one to 13.

spam = 67
eggs = 13


# Add the two variables and display it to the user

dinner = spam + eggs
print("\nPart 1: Add two variables")
print(dinner)

# Subtract the two variables and display it to the user

dinner = spam - eggs
print("\nPart 1: Subtracting two variables")
print(dinner)

# Multiply the two variables and display it to the user

dinner = spam * eggs
print("\nPart 1: Multiplying two variables")
print(dinner)

# Divide the two variables and display it to the user

dinner = spam / eggs
print("\nPart 1: Dividing two variables")
print(dinner)

######################################################
# Part 2: Accepting user input and using expressions #
######################################################

# Replace each variable with user input. Ask the user
# to enter a number for each variable

spam = int(input("\n\nPlease enter a number for spam:"))
eggs = int(input("Please enter a number for eggs:"))

# Add the two variables and display it to the user

print("\nPart 2: Adding two variables:")
dinner = spam + eggs
print(dinner)

# Subtract the two variables and display it to the user

print("\nPart 2: Subtracting2 two variables:")
dinner = spam - eggs
print(dinner)

# Multiply the two variables and display it to the user

print("\nPart 2: Multiplying two variables:")
dinner = spam * eggs
print(dinner)

# Divide the two variables and display it to the user

print("\nPart 2: Dividing two variables:")
dinner = spam / eggs
print(dinner)

###################################################################
# Part 3: Accepting user input and using expressions with strings #
###################################################################

# Replace each variable with user input. Ask the user
# to enter a string for each variable

spam = input("\n\nPlease enter a STRING for spam:")
eggs = input("Please enter a STRING for eggs:")

# Join the two strings together and display them to the user

print("\nPart 3: Concat (Add)")
dinner = spam + eggs
print(dinner)

# Repeat the first string three times and display to the user

print("\nPart 3: Repeat spam three times:")
dinner = spam * 3
print(dinner)

# Repeat the second string three times and display to the user

print("\nPart 3: Repeat eggs three times:")
dinner = eggs * 3
print(dinner)

############################################################
# Congrats! Now, test the assignment and submit to GitHub! #
############################################################
