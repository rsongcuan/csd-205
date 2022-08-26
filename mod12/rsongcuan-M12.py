# Ryan Songcuan, 10/10/21, Module 12 Assignment
# submission for Module 10 Assignment
# Create a program that performs file processing activities

import os

# Prompt user for the directory they'd like to save file
path = os.getcwd()
print(f"\nYour current directory is {path}.\nWould you like to save your file here?")
answer = input("Please enter 'y' for yes or 'n' to choose a different directory.\t")
if answer == 'n':
	new_path = input("Please enter the path to the directory you'd like to save to: ")
	try:
		os.chdir(new_path)
		print(f"We will save your file to {new_path}.")
	except FileNotFoundError:
		print("This was not a valid entry. We will save the file to your current directory.")
elif answer == 'y':
	print("We will save the file to your current directory.")
else:
	print("This was not a valid entry. We will save to your current directory.")

# Prompt user for filename
filename = input("\nEnter the filename : ")
new_filename = f'{filename}.txt'
print(f"Your file will be saved as {new_filename}.")

# Write user data to file
with open(new_filename, 'w') as f:
	name = input("\nEnter your name: ")
	address = input("Enter your address: ")
	phone = input("Enter your phone number, including the area code: ")
	f.write(f"{name}, {address}, {phone}")

# Read back the file contents
with open(new_filename, 'r') as file_object:
	contents = file_object.read()

print("Your file has been saved. Please review the contents below to validate it is correct.")
print(contents)