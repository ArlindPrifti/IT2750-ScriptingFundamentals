#######################################
# IT 2750 - Lab 02                    #
# Generate a secure password          #
# Author: Arlind Prifti               #
# S#: S01235792                       #
#######################################

# Import libraries needed for this lab
import random
import string

# Define a method generatePassword that:
# - Has the following parameters:
#   + length -> int, length of password to be created
#   + upper -> bool, True means include uppercase letters, False means
#              do not include uppercase letters
#   + lower -> bool, True means include lowercase letters, False means
#              do not include lowercase letters
#   + numbers -> bool, True means include numbers, False means
#                do not include numbers
#   + symbols -> bool, True means include symbols, False means
#                do not include symbols
# [You will have to define parameters in the function below - Remove this comment line placeholder!]
def generatePassword(length, upper, lower, numbers, symbols):
    # Create local variables for the set of characters that can be used
    # and the new password that will be returned from the function
    chars = ""
    newPassword = ""

    # Use if statements and the string.ascii_ constants to add the various
    # character sets to the local variable tracking what characters to be
    # used (https://docs.python.org/3/library/string.html, see "String 
    # constants" for reference)

    
    if upper:
        chars += string.ascii_uppercase

    if lower:
        chars += string.ascii_lowercase

    if numbers:
        chars += string.digits

    if symbols:
        chars += string.punctuation
    
    # There is an error if the string chars is empty, if so, instruct the user
    if (upper == False) and (lower == False) and (numbers == False) and (symbols == False):
        return('\n There is an empty string error, and you must use at least one of the following: \n  * Upper case letters \n  * Lower case letters \n  * Numbers \n  * Symbols\n\n Please restart the programm\n')
        
        # Or raise an exception
        # raise Exception('\n There is an error and you must use at least one of the following: \n  * Upper case letters \n  * Lower case letters \n  * Numbers \n  * Symbols\n\n Please restart the programm\n')
    
    # Test chars string
    # print(chars)
    
    # Create a loop (of any type) to add a random character from the set of
    # characters (hint: using random.choice(...)) to the new password
    # placeholder variable
    
    for i in range(length):
        newPassword += random.choice(chars)

    # Return the new password as the function's return value
    return newPassword

# Print a welcome message
print('====================================================')
print('==== WELCOME TO THE ULTIMATE PASSWORD GENERATOR ====')
print('====================================================')

# Ask the user how long of a password they want
print('How long should the password be? ')
length = int(input())

# Ask the user if they want to use uppercase, lowercase, numbers
# and symbols in separate input statements. Remember to properly
# handle variable types! (hint: bool(...) converts to bool, 
# int(...) converts to int, str(...) converts to string)

print("UPPERcase letters? 1 = Yes, 0 = No: ")
upper = bool(int(input()))

print("lowercase letters? 1 = Yes, 0 = No: ")
lower = bool(int(input()))

print("numbers? 1 = Yes, 0 = No: ")
numbers = bool(int(input()))

print("symbols? 1 = Yes, 0 = No: ")
symbols = bool(int(input()))

# Test user inputs
# print('Length ' + str(length) + ' UpperCase ' + str(upper) + ' LowerCase ' + str(lower) + ' Numbers ' + str(numbers) + ' Symbols ' + str(symbols))

# Call the generatePassword function and pass in the user's choices
# and display the return value to the user
print('----------------------------------------------------')
print('Generating password...')
print('----------------------------------------------------')


print("Your new password is: " + generatePassword(length, upper, lower, numbers, symbols))
print('====================================================')
