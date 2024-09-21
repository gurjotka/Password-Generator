from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password generator project

def generate_password():

    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    symbols_list = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    numbers_list = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.askokcancel(title="Error", message="Hey!!! You can't leave things empty!!!!")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')
            messagebox.askokcancel(title="Save Done", message="Your email and password details are saved in the .json file")

# ---------------------------- SEARCH --------------------------------- #

def find_password():
    webpage = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data=json.load(data_file)
            
    except FileNotFoundError:
        messagebox.askokcancel(title="Error", message="File doesn't exist")

    else:
        if webpage not in data:
            messagebox.askokcancel(title="Error", message="website doesn't exist")

        else:
            email = data[webpage]['email']
            password = data[webpage]['password']
            messagebox.askokcancel(title=webpage, message=f"Email: {email},\nPassword: {password}")



        


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas= Canvas(width=200, height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "abc@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

pass_button = Button(text="Generate Password", width=15, command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)




    

window.mainloop()