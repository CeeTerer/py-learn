from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# -----------------------------SEARCH---------------------------------------------#


def search():
    website = website_name.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            website_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in website_data:
            website_password = website_data[website]["password"]
            website_email = website_data[website]["email"]
            messagebox.showinfo(message=f"Your email:{website_email}\n "
                                        f"Your password: {website_password}", title=website)
            pyperclip.copy(website_password)
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_name.get().title()
    username = username_name.get()
    password_input = password.get()
    new_data = {
        website: {
            "email": username,
            "password": password_input
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password_input) == 0:
        messagebox.showinfo(title=website, message="Please fill in all fields")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_name.delete(0, END)
            password.delete(0, END)
            website_name.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", )
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_name = Entry(width=32, highlightthickness=0)
website_name.grid(column=1, row=1)
website_name.focus()

username_name = Entry(width=50, highlightthickness=0)
username_name.grid(column=1, row=2, columnspan=2)
username_name.insert(0, "cynthiachep8@gmail.com")

password = Entry(width=50, highlightthickness=0)
password.grid(column=1, row=3, columnspan=2)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", highlightthickness=0, width=13, command=search)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=43, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
