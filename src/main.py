import tkinter
from tkinter import *


window = Tk(className=" Shopping List")
window.geometry("1000x1000")

user_entered_input = StringVar()
Entry(window, textvariable=user_entered_input).pack()

Label(window, text='Add items to your list').pack()

Button(window, text='Ok', command=lambda: add_shopping_list()).pack()

output_display = Text(window, state="disabled", height=50, width=80, bg="light yellow", foreground="black")
output_display.pack()

Button(window, text='Clear List', command=lambda: clear_output_box()).place(x=455, y=735)


def clear_output_box():
    output_display.config(state=NORMAL)
    output_display.delete('1.0', END)


def add_shopping_list():
    output_display.config(state=NORMAL)
    output_display.insert(tkinter.END, f"{user_entered_input.get()}\n")
    output_display.config(state=DISABLED)


window.mainloop()

