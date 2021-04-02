from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = input_website.get()
    mail = input_mail.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Alarm", message="Please fill out all the fields :)")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()

# ---------------------------- FIND PASSWORD ------------------------ #


def find_password():
    website = input_website.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            mail = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {mail}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No entry for {website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx="50", pady="50")

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website")
label_website.grid(row=1, column=0)
label_mail = Label(text="Email/Username")
label_mail.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)


input_website = Entry(width=28)
input_website.focus()
input_website.grid(row=1, column=1)
input_mail = Entry(width=35)
input_mail.insert(0, "mymail@gmail.com")
input_mail.grid(row=2, column=1, columnspan=2)
input_password = Entry(width=28)
input_password.grid(row=3, column=1)

button_search = Button(text="Search", command=find_password)
button_search.grid(row=1, column=2)
button_generate = Button(text="Generate", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(width=36, text="Add", command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
