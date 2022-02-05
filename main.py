from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def on_button_click():
    input_text = input.get()
    answer = str(int(input_text) * 1.6)
    answer_label.config(text=answer)


input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)
answer_label.config(padx=20, pady=20)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=on_button_click)
button.grid(column=1, row=2)


window.wait_window()