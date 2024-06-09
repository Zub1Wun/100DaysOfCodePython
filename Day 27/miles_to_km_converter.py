#786
#Completed by Zub1Wun on 2024-06-09 Sunday

from tkinter import *

def calculate_conversion():
    miles = float(miles_input_entry.get())
    km = round(miles*1.609,2)
    conversion_output_label.config(text=f"{km}")


window = Tk()
window.title("Zub1Wun's Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

#Entry
miles_input_entry = Entry(width=10)
miles_input_entry.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

#Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

#Label
conversion_output_label = Label(text="0", font=("Arial", 18, "bold"))
conversion_output_label.grid(column=1, row=1)
conversion_output_label.config(padx=10, pady=10)

#Label
km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

#Button
calculate_button = Button(text="Calculate", command=calculate_conversion)
calculate_button.grid(column=1, row=2)


window.mainloop()