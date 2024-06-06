#786
#Completed by Zub1Wun on 2024-06-06 Thursday
#Day 24 of 100 Days of Code: The Complete Python Pro Bootcamp, by Angela Yu of AppBrewery on Udemy

#TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

# TODO : read all invited names and place in list for processing.

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.read().split("\n")
    print(names)

# TODO : read starting letter, find [NAME] replace with name in list, print out new letter in OUTPUT.

with open("Input/Letters/starting_letter.txt") as letter_template_file:
    template = letter_template_file.read()
    for name in names:
        new_letter = template.replace("[name]",name)
        new_file_name = f"{name}.txt"
        # check if exists? If it does not then write (What if it does exist?)
        if not os.path.exists(f"Output/{new_file_name}"):
            with open(f"Output/ReadyToSend/{new_file_name}", "w") as new_file:
                new_file.write(f"{new_letter}")