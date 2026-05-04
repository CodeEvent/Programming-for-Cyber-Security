

















#WEEK 2, part 1.2, Exercise 3 – Fibonacci Sequence (10 marks)
# Write a program which will print out the first 20 terms of the Fibonacci series where the next
# term in the sequence is the sum of the previous two terms.


#--------Start Code-------------------------------------#
# fibonacci_series = [0, 1]
#
# for i in range(2, 20):
#     next_term = fibonacci_series[i - 1] + fibonacci_series[i - 2]
#     fibonacci_series.append(next_term)
#
# for val in fibonacci_series:
#     print(val, end=' ')
#---------End Code------------------------------------#

#2.	Week 4 Part 2.1 Caesar Cipher (15 marks)
# Part 2.1 Caesar Cipher
# The Caesar Cipher is a classic encryption cipher which encrypts data by rotating the plaintext
# alphabet by a given shift. Details can be found at https://chici.org/studies/awa/caesar.php
# Write a function encrypt with the following signature
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# def encrypt(plaintext, k):
# #Your code here
# return ciphertext
# Where plaintext is the string to be encrypted and k is the shift. Your function should return the
# ciphertext (encrypted plaintext) to the caller.


#---------Start Code------------------------------------#

# Function to encrypt the input message using Caesar Cipher
# def shift_text(plain_text, shift_factor):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     encoded_text = ''
#
#     # Loop through each character in the input text
#     for current_char in plain_text:
#         if current_char.isalpha():  # Only encrypt letters
#             # Find the position of the character in the alphabet
#             char_position = alphabet.index(current_char.lower())
#             # Apply the shift to get the new position
#             new_position = (char_position + shift_factor) % 26
#             # Get the corresponding character after shifting
#             shifted_char = alphabet[new_position]
#
#             # If the original character was uppercase, convert it back to uppercase
#             if current_char.isupper():
#                 shifted_char = shifted_char.upper()
#
#             encoded_text += shifted_char  # Add to the encrypted text
#         else:
#             # Non-alphabet characters are added unchanged
#             encoded_text += current_char
#
#     return encoded_text
#
#
# # Get user input for the message and shift amount
# user_input_text = input("Enter the text to encrypt: ")
# shift_value = int(input("Enter the shift value (k): "))
#
# # Call the shift_text function to encrypt the message
# resulting_cipher = shift_text(user_input_text, shift_value)
#
# # Output the encrypted message
# print(f"Encrypted result: {resulting_cipher}")

#---------End Code------------------------------------#

#3. Week 4 Part 2.2 Creating the password hashes (15 marks)
# Part 2.2 Creating the password hashes
#
# 1. Use a while loop to enter a few usernames and corresponding passwords.
# 2. Use the hashlib library to compute password hashes and store usernames, and password
# hashes in two different lists. You can use following code to compute hashes:
# from hashlib import sha256
# input_password = input('Enter Password')
# hashed_password = sha256(input_password.encode('utf-8')).hexdigest(

#---------Start Code------------------------------------#
# from hashlib import sha256
#
#     # Function to hash the user input password
#
#
# def generate_password_hash(user_pwd):
#     return sha256(user_pwd.encode('utf-8')).hexdigest()
#
#
# # Lists to store usernames and their corresponding password hashes
# accounts = []
# hashed_pwds = []
#
# # While loop to repeatedly ask for usernames and passwords until the user decides to stop
# while True:
#     # Input for username and password
#     user_input_name = input("Enter a username: ")
#     user_input_pwd = input("Enter a password: ")
#
#     # Hash the entered password and add the username and hashed password to the lists
#     hashed_password = generate_password_hash(user_input_pwd)
#     accounts.append(user_input_name)
#     hashed_pwds.append(hashed_password)
#
#     # Ask the user if they want to add another user or stop
#     continue_input = input("Do you want to add another user? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break
#
# # Print out the usernames and their hashed passwords for verification
# print("\nStored Usernames and Password Hashes:")
# for i in range(len(accounts)):
#     print(f"Username: {accounts[i]}, Hashed Password: {hashed_pwds[i]}")

#---------End Code------------------------------------#




#4.	Week 4 Part 2.3 Verifying the password (15 marks)
# Part 2.3 Verifying the password
# 1. Use the password hashes created in part 2.2.
# 2. Input username and password from a user
# 3. Using functions, compute the hash of the password and match it with the stored hash of the
# corresponding user.
# 4. Print if the password is correct or not.


#--------Start Code-------------------------------------#
# from hashlib import sha256
#
#
# # Function to hash the user input password
# def generate_password_hash(user_pwd):
#     return sha256(user_pwd.encode('utf-8')).hexdigest()
#
#
# # Example data: usernames and their associated password hashes
# accounts = ["Raman", "bob", "Ermand"]
# hashed_pwds = [
#     sha256("UWSProgramming1".encode('utf-8')).hexdigest(),
#     sha256("secretpass".encode('utf-8')).hexdigest(),
#     sha256("Giovanni2025".encode('utf-8')).hexdigest()
# ]
#
#
# # Function to validate the entered password by comparing its hash
# def validate_user_credentials(user, entered_pwd):
#     # Check if the user exists
#     if user in accounts:
#         # Find the user's index in the accounts list
#         account_idx = accounts.index(user)
#         # Generate the hash for the entered password
#         entered_pwd_hash = generate_password_hash(entered_pwd)
#
#         # Compare the entered password hash with the stored password hash
#         if entered_pwd_hash == hashed_pwds[account_idx]:
#             return "Access granted. Password is correct."
#         else:
#             return "Access denied. Incorrect password."
#     else:
#         return "User not found."
#
#
# # Prompt the user to enter their username and password
# user_input_name = input("Enter your username: ")
# user_input_pwd = input("Enter your password: ")
#
# # Validate the credentials
# auth_result = validate_user_credentials(user_input_name, user_input_pwd)
# print(auth_result)

#---------End Code------------------------------------#


#5.	Week 5 Part 2.2 Checking if a password has been hacked (15 marks)
# Part 2.2
# Write a Python program to check if the password is secure and has not been hacked. The file
# contains a username and password pair (one pair per line separated by a comma). Read the file to
# get the username, password pair, split the pair to get the password, calculate the hash, and check it
# using API if the password is secure or not. The example file contains username, password pair as
# given below
# Username1, password1
# Usernam2, password2
# Username3,password3
# For this exercise, You can use the "Have I Been Pwned" API
# (https://haveibeenpwned.com/API/v3) to check if a password has been leaked?
# import requests
# # If you don’t have requests package, install it in PyCharm: File-Settings-ProjectnameIntrepreter
# import hashlib
# password="password"
# password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
# print(password_hash)
# response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")
# print(response.status_code)
# print(response.text)
# # hashes will get a list of all hashes but from 6th character
# hashes = [line.split(':') for line in response.text.splitlines()]
# print(hashes)


#--------Start Code-------------------------------------#
# import hashlib
# import requests
#
#
# # Function to check if a password is secure using the "Have I Been Pwned" API
# def is_password_secure(user_password):
#     # SHA-1 hash of the password (uppercase as required by the API)
#     hashed_password = hashlib.sha1(user_password.encode('utf-8')).hexdigest().upper()
#
#     # Get the first 5 characters of the hashed password (API format)
#     response = requests.get(f"https://api.pwnedpasswords.com/range/{hashed_password[:5]}")
#
#     if response.status_code == 200:
#         # Get the list of hashes from the response, starting from the 6th character
#         hash_list = [line.split(':') for line in response.text.splitlines()]
#
#         # Check if the full hash of the password exists in the list
#         for hash_suffix, count in hash_list:
#             if hash_suffix == hashed_password[5:]:
#                 return f"Password '{user_password}' has been pwned {count} times!"
#
#         # If password is not found in the response, it has not been pwned
#         return f"Password '{user_password}' is secure and has not been pwned."
#     else:
#         return f"Error: Unable to check password. Status code {response.status_code}."
#
#
# # Function to read the username and password pairs from a file
# def check_passwords_from_file(file_path):
#     # Open and read the file
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Strip newline and split the username and password
#             username, password = line.strip().split(',')
#
#             # Check if the password is secure
#             result = is_password_secure(password)
#             print(f"Username: {username} - {result}")
#
#
# # Example usage:
# file_path = "user_passwords.txt"  # Replace with your actual file path
# check_passwords_from_file(file_path)
#---------End Code------------------------------------#


# 6.	Week 6 Part 1 Exercise 2 Command line arguments (15 marks)
# Create a file arguments.py and using the argparse module, write a program that accepts
# 2 integers and an arithmetic operator as command line arguments and returns the result of
# the operation, For a command line call of:
# python arguments.py 4 3 /
# your program would return 1.3333333333333333. Your program should provide help to
# the user on what values to enter.

#
#--------Start Code-------------------------------------#
# def perform_calculation(num1, num2, operation):
#     # Perform operation based on the given operator
#     if operation == "+":
#         return num1 + num2  # Addition
#     elif operation == "-":
#         return num1 - num2  # Subtraction
#     elif operation == "*":
#         return num1 * num2  # Multiplication
#     elif operation == "/":
#         if num2 == 0:
#             return "Error: Division by zero"
#         else:
#             return num1 / num2  # Division
#     else:
#         return "Error: Unsupported operation"  # Handle unsupported operators
#
#
# if __name__ == "__main__":
#     # Set up the argument parser to handle command-line arguments
#     parser = argparse.ArgumentParser(description="Perform arithmetic operations using command-line arguments.")
#
#     # Add arguments for the two numbers and the operator
#     parser.add_argument("first_number", type=int, nargs="?", help="First number")
#     parser.add_argument("second_number", type=int, nargs="?", help="Second number")
#     parser.add_argument("operation", type=str, nargs="?", help="Operation (+, -, *, /)")
#
#     # Parse the command-line arguments provided by the user
#     args = parser.parse_args()
#
#     # If arguments are missing, prompt the user for input
#     if args.first_number is None or args.second_number is None or args.operation is None:
#         print("Command-line arguments are missing. Please enter the values interactively.")
#         args.first_number = int(input("Enter the first number: "))
#         args.second_number = int(input("Enter the second number: "))
#         args.operation = input("Enter the operator (+, -, *, /): ")
#
#     # Call the function to perform the operation
#     result = perform_calculation(args.first_number, args.second_number, args.operation)
#
#     # Print the result of the operation
#     print("Result:", result)
#---------End Code------------------------------------#


# 7.	Week 7 Part 3 Implementation of Binary Search (15 marks)

# Write a Python program for binary searching.
# The program should have a binarySearch() function that takes a list and an element
# as parameters and returns the index of the element if found, otherwise -1.


#--------Start Code-------------------------------------#
# Define the function for binary search
# def binarySearch(sorted_list, target):
#     # Initialize the start and end indices for the search range
#     start_index = 0
#     end_index = len(sorted_list) - 1
#
#     # Perform the search while the range is valid
#     while start_index <= end_index:
#         # Calculate the middle index
#         middle_index = (end_index + start_index) // 2
#
#         # Check if the middle element matches the target
#         if sorted_list[middle_index] == target:
#             return middle_index  # Element found, return its index
#         # If target is greater, ignore the left half
#         elif sorted_list[middle_index] < target:
#             start_index = middle_index + 1
#         # If target is smaller, ignore the right half
#         else:
#             end_index = middle_index - 1
#
#     # Element is not present in the list
#     return -1
#
# # Example usage
# sorted_list = [2, 7, 46, 52, 88, 100]  # Input list (must be sorted)
# target = 15  # Element to search for
#
# # Perform binary search
# result_index = binarySearch(sorted_list, target)
#
# # Output the result
# if result_index != -1:
#     print(f"Target is present at index {result_index}")
# else:
#     print("Target is not present in the sorted list")
#---------End Code------------------------------------#
