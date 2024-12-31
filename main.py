import pyperclip
from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password():
    password_entry.delete(0, END)
    password = generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password_to_file():
    website_name = website_entry.get().strip().lower()
    email_or_username = email_or_username_entry.get().strip()
    password = password_entry.get().strip()

    if website_name == "" or password == "" or email_or_username == "":
        messagebox.showinfo(
            title="Oops! Something's Missing",
            message="All fields are required! Please fill in the details and try again. 😊"
        )
        return

    new_data = {
        website_name: {
            "email": email_or_username,
            "password": password
        }
    }

    is_ok = messagebox.askokcancel(
        title=f"🔐 Save {website_name.capitalize()} Credentials?",
        message=(
            f"Here’s what you’ve entered:\n\n"
            f"📧 Email/Username: {email_or_username}\n"
            f"🔒 Password: {password}\n\n"
            "Would you like to save these details?"
        )
    )

    if is_ok:
        try:
            with open("password_manager.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                    if not isinstance(data, dict):
                        raise ValueError("Invalid file structure.")
                except (json.JSONDecodeError, ValueError):
                    data = {}
        except FileNotFoundError:
            with open("password_manager.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(
                    title="Vault Created!",
                    message="Your password vault was created, and the details have been saved securely. 🎉"
                )
        else:
            data.update(new_data)

            with open("password_manager.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(
                    title="Details Updated!",
                    message=f"Your credentials for '{website_name}' have been saved successfully! 🚀"
                )
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_name = website_entry.get().strip().lower()
    try:
        with open("password_manager.json", "r") as data_file:
            try:
                data = json.load(data_file)
            except json.JSONDecodeError:
                messagebox.showwarning(
                    title="Corrupt File",
                    message="Your password vault seems to be empty or corrupted. Please add some credentials to reset it!"
                )
                return

        login_data = data[website_name]
    except FileNotFoundError:
        messagebox.showwarning(
            title="Oops! File Missing",
            message="It seems like your password vault is empty. Add some credentials to get started!"
        )
    except KeyError:
        messagebox.showwarning(
            title="No Match Found",
            message=f"Couldn't find any details for '{website_name}'. Maybe check your spelling or add it to the vault?"
        )
    else:
        messagebox.showinfo(
            title=f"🔑 {website_name.capitalize()} Details",
            message=(
                f"Here are your saved credentials:\n\n"
                f"📧 Email: {login_data['email']}\n"
                f"🔒 Password: {login_data['password']}\n\n"
                "Stay secure! 😊"
            )
        )
    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
search_data_btn = Button(text="Search", command=find_password)
search_data_btn.grid(column=2, row=1, sticky="EW")

label_email_or_username = Label(text="Email/Username:")
label_email_or_username.grid(column=0, row=2)

email_or_username_entry = Entry()
email_or_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_or_username_entry.insert(0, "")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_btn = Button(text="Generate Password", command=generate_random_password)
generate_password_btn.grid(column=2, row=3, sticky="EW")

add_password_btn = Button(text="Add", width=35, command=save_password_to_file)
add_password_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
