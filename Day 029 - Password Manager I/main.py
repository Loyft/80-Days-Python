from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Alarm", message="Please fill out all the fields :)")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {mail} \nPassword: {password} \nSave?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {mail} | {password} \n")
                input_website.delete(0, END)
                input_password.delete(0, END)
                input_website.focus()


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


input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)
input_mail = Entry(width=35)
input_mail.insert(0, "mymail@gmail.com")
input_mail.grid(row=2, column=1, columnspan=2)
input_password = Entry(width=28)
input_password.grid(row=3, column=1)

button_generate = Button(text="Generate", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(width=36, text="Add", command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
