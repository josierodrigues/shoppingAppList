import tkinter
from tkinter import *
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')

conn.commit()

cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('john', 'password'))

conn.commit()
conn.close()

total_price = 0
total_price_label = Label

def show_main_window():
    global total_price_label
    window = Tk(className=" Shopping List App")

    window.geometry("1000x1000")

    Button(window, text="Profile", command=lambda: go_to_profile()).pack()

    user_entered_item = StringVar()
    Entry(window, textvariable=user_entered_item).pack()

    Label(window, text='Item Name').pack()

    user_entered_quantity = StringVar()
    Entry(window, textvariable=user_entered_quantity).pack()

    Label(window, text='Quantity').pack()

    user_entered_price = StringVar()
    Entry(window, textvariable=user_entered_price).pack()

    Label(window, text='Price').pack()

    Button(window, text='Ok', command=lambda: add_shopping_list(output_display, user_entered_item, user_entered_price, user_entered_quantity)).pack()

    total_price_display = StringVar(value=total_price)
    # total_price_display = int(total_price)
    total_price_label = Label(window, text='Total price: 0')
    total_price_label.pack()

    Button(window, text='Clear List', command=lambda: clear_output_box(output_display)).pack()

    output_display = Text(window, state="disabled", height=50, width=80, bg="light yellow", foreground="black")
    output_display.pack()


    window.mainloop()


def open_window_login():
    login_window = Tk(className=" Login")
    login_window.geometry("600x600")
    Label(login_window, text="Login: ").pack()
    mandatory_name_entry = Entry(login_window, width=20)
    mandatory_name_entry.pack()
    Label(login_window, text="Password: ").pack()
    mandatory_password_entry = Entry(login_window, width=20)
    mandatory_password_entry.pack()
    Button(login_window, text="Login", command=lambda: validate_and_open_main_window(login_window, mandatory_name_entry, mandatory_password_entry, input_error_label)).pack()
    input_error_label = Label(login_window, text="Information Required", state = DISABLED, disabledforeground = login_window.cget('bg'))
    input_error_label.pack()

    login_window.mainloop()


def validate_and_open_main_window(login_window, mandatory_name_entry, mandatory_password_entry, input_error_label):
    if mandatory_name_entry.get() and mandatory_password_entry.get():
        # the user entered data in the mandatory entry: proceed to next step
        login_window.destroy()
        show_main_window()
    else:
        # the mandatory field is empty
        # print("Information Required")
        input_error_label['state'] = "normal"
        mandatory_name_entry.focus_set()


def go_to_profile():
    profile_window = Tk(className=" Profile")
    profile_window.geometry("500x500")
    Label(profile_window, text="Name").pack()
    Label(profile_window, text="Email").pack()
    profile_window.mainloop()


def clear_output_box(output_display):
    global total_price_label
    global total_price
    output_display.config(state=NORMAL)
    output_display.delete('1.0', END)
    total_price = 0
    total_price_label.config(text="Total price: {}".format(total_price))


def add_shopping_list(output_display, user_entered_item, user_entered_price, user_entered_quantity):
    global total_price
    global total_price_label
    output_display.config(state=NORMAL)
    output_display.insert(tkinter.END, f"{user_entered_item.get()} {user_entered_quantity.get()} {user_entered_price.get()}\n")
    output_display.config(state=DISABLED)
    total_price += int(user_entered_price.get()) * int(user_entered_quantity.get())
    total_price_label.config(text="Total price: {}".format(total_price))
    total_price_label.config(state=DISABLED)


# open_window_login()
show_main_window()


