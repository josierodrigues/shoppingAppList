import tkinter
from tkinter import *
from tkinter import messagebox

import black

window = Tk(className=" Shopping List")
window.geometry("1000x1000")


# homepage = Tk(className=" Homepage")
# homepage.geometry("700x700")


# class MainWindow(homepage):
#     def initUI(self):
#         # same as before
#         self.taskLayout = window.QStackedLayout()
#         self.setMainLayout(self.taskLayout)
#         # same as before
#
#     def setMainLayout(self, layout):
#         today = self.todayWidget()
#         next_week = self.nextWeekWidget()
#         calendar_widget = self.calendarWidget()
#
#         layout.addWidget(today)
#         layout.addWidget(next_week)
#         layout.addWidget(calendar_widget)



def clear_output_box():
    output_display.config(state=NORMAL)
    output_display.delete('1.0', END)


def add_shopping_list():
    print()
    output_display.config(state=NORMAL)
    output_display.insert(tkinter.END, f"{a.get()}\n")
    output_display.config(state=DISABLED)


def homepage():
    msg = messagebox.showinfo("User Login", "Welcome to Shopping List! Enter login details below.")


homepage_window = Message(homepage, command=homepage())


a = StringVar()
Label(window, text='Add items to your list').pack()
Entry(window, textvariable=a).pack()
button_add = Button(window, text='Ok', command=lambda: add_shopping_list()).pack()
# button_add.place(x=400, y=50)


output_display = Text(window, state="disabled", height=50, width=80, bg="light yellow", foreground="black")
output_display.pack()
button_clear = Button(window, text='Clear List', command=lambda: clear_output_box())
button_clear.place(x=455, y=735)


window.mainloop()
