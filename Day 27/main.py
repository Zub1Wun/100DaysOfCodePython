from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0,column=0)
my_label.config(padx=)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(row=3, column=3)










window.mainloop()