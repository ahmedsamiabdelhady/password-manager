from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#-----------------------------CONSTANTS------------------------------------------------#
BLACK_PEARL= "#040D12"
TIBER= "#183D3D"
CUTTY_SARK= "#5C8374"
TOWER_GRAY= "#93B1A6"
#------------------------------SEARCH------------------------------------------------#
def search():
    try:
        with open("data.json", "r") as file_data:
            data= json.load(file_data)
        website= website_entry.get().title()
    except FileNotFoundError:
        messagebox.showerror(title="Data dose not exist", message=f"There is no data to show for '{website}'.")
    else:
        if website in data:
            data_to_search= data[website]
            messagebox.showinfo(title=website, message=f"Email: {data_to_search['email']}\nPassword: {data_to_search['password']}")
        else:
            messagebox.showerror(title="Data dose not exist", message=f"There is no data to show for '{website}'.")
    finally:
        website_entry.delete(0, END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
                    [random.choice(symbols) for _ in range(random.randint(2, 4))] + \
                    [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website= website_entry.get().title()
    email= email_entry.get()
    password= password_entry.get()

    new_data= {
        website:{
            "email": email,
            "password": password
        }
    }
    #popup an error
    if website == "" or password == "":
        messagebox.showerror(title= "Missing Fields", message="Required field is empty, Please, Check your input.")
    #popup a message for check
    else:
        is_ok= messagebox.askokcancel(title=website , message=f"Please check the details below:\n\nEmail/Username: '{email}'; "
                                                              f"Password: '{password}'\n\n\nWant to confirm?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data= json.load(data_file)
                    data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.config(fg=TIBER)
                email_entry.insert(0, "Example@example.com OR @Username OR Username")
# ---------------------------- UI SETUP ------------------------------- #
#setup a window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=TOWER_GRAY)
#add canvas and logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(window, width=208, height=210, bg=TOWER_GRAY, highlightthickness=0)
canvas.create_image(108, 100, image=logo)
canvas.grid(column=1, row=0)

#website label and entry
website_label = Label(text="Website:", highlightthickness=0, bg=TOWER_GRAY, fg= TIBER)
website_label.grid(column=0, row=1)

website_entry = Entry(width=34, bg=CUTTY_SARK, fg= "white", bd=0)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

#email label and entry
email_label = Label(text="Email/Username:", highlightthickness=0, bg=TOWER_GRAY, fg= TIBER)
email_label.grid(column=0, row=2)

email_entry = Entry(width=52, bg=CUTTY_SARK, fg= TIBER, bd=0)
def clear_entry(event):
    email_entry.delete(0, "end")
    email_entry.config(fg="white")
def restore_entry(event):
    email= email_entry.get()
    if email == "":
        email_entry.insert(0, "Example@example.com OR @Username OR Username")
        email_entry.config(fg=TIBER)
email_entry.insert(0, "Example@example.com OR @Username OR Username")
email_entry.bind("<FocusIn>", clear_entry)
email_entry.bind("<FocusOut>", restore_entry)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")

#password label and entry
password_label = Label(text="Password:", highlightthickness=0, bg=TOWER_GRAY, fg= TIBER)
password_label.grid(column=0, row=3)

password_entry = Entry(width=34, bg=CUTTY_SARK, fg= "white", bd=0)
password_entry.grid(column=1, row=3, sticky="w")

#button wedgits
search_button= Button(text="Search",width=14, highlightthickness=0, fg= "white", bg=TIBER, bd=0, command=search)
search_button.grid(column=2, row=1, sticky="w")

generator_button = Button(text="Generate Password", highlightthickness=0, fg= "white", bg=TIBER, bd=0, command= password_generate)
generator_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=44, highlightthickness=0, fg= "white", bg=TIBER, bd=0, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()