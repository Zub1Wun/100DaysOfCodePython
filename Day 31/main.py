#Zub1Wun - Day 31 Flash Card App
# from https://www.udemy.com/course/100-days-of-code/learn/lecture/20944508#overview
# STARTED 2024-06-23 Sun 05:23
# COMPLETED 2024-06-23 Sun 09:05

from random import choice
from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
max_W = 800
max_H = 526
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

# TODO : You'll need to use pandas to access the CSV file and
#  generate a data frame. To get all the words/translation rows
#  out as a list of dictionaries e.g. [{french_word: english_word},
#  {french_word2: english_word2}, {french_word3: english_word3}]
# TODO : DataFrame.to_dict(orient="records")
french_dict = data.to_dict(orient="records")
current_card = {}


def pick_random():
    # TODO : Pick a random French word/translation and put the word into the
    #  flashcard. Every time you press the ❌ or ✅ buttons,
    #  it should generate a new random word to display.
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(french_dict)
    french_word = current_card["French"]
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    eng_word = current_card["English"]
    canvas.itemconfig(word_text, text=eng_word, fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

def know_card():
    global current_card, french_dict
    print(len(french_dict))
    french_dict.remove(current_card)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False) #index=False stops
    pick_random()

def notknow_card():
    pass


window = Tk()
window.title("Zub1Wun's FlashCard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=max_W, height=max_H)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(max_W / 2, max_H / 2, image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  #setting highlightthickness removes border
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=know_card)
button_right.grid(row=1, column=0)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=pick_random)
button_wrong.grid(row=1, column=1)
pick_random()
window.after(3)

# TODO : When the user presses on the ✅ button, it means that they
#  know the current word on the flashcard and that word should be
#  removed from the list of words that might come up.
# TODO : The updated data should be saved to a new file called
#  words_to_learn.csv
# TODO : The next time the program is run, it should check if
#  there is a words_to_learn.csv file. If it exists, the program
#  should use those words to put on the flashcards. If the
#  words_to_learn.csv does not exist (i.e., the first time the
#  program is run), then it should use the words in the french_words.csv
#  We want our flashcard program to only test us on things we don't know.
#  So if the user presses the ✅ button, that means the current card
#  should not come up again.
#
# TODO : The remove() method can remove elements from a list. e.g.
#  https://www.w3schools.com/python/ref_list_remove.asp
# TODO :  You can create a new csv file from a dictionary using
#  DataFrame.to_csv() e.g.
#  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
# TODO : If you don't want to create an index for the new csv,
#  you can set the index parameter to False.
#  e.g. data.to_csv("filename.csv", index=False)

window.mainloop()

# TODO :
