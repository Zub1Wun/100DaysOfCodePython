# 786
# Completed 2024-06-08 Sat by Zub1Wun

import pandas

# reads csv into DataFrame
NATO_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(NATO_df)
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Dictionary Comprehension. Iterates through each row, which are numbered 0 to 25.
# Each row has columns letter then code.
NATO_dict = {row.letter: row.code for (index, row) in NATO_df.iterrows()}
#print(NATO_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

coded_word = [NATO_dict[letter] for letter in word]
print(coded_word)


"""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(f"key: {key}")
    print(f"value: {value}")
    print("--------------")
print("================")

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(f"index: {index}")
    print(f"row: {row}")
    print(f"row.student: {row.student}")
    print(f"row.score: {row.score}")
    print("--------------")
    print("================")
    #Access index and row
    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""


"""
NATO_alp_dict = {letter:code for (letter,code) in NATO_alp_data.items()}
print(NATO_alp_dict)

for (index, row) in NATO_alp_data.items():
    print(row)




word = input("Enter a word: ")
print()
"""
