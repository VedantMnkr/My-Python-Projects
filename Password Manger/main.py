from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #





def pass_gen():
    """
    Generates Random passwords containg lowercase/uppercase alphabets, numericals and symbols .
    """

    pass_chrs_nums = "1234567890"
    pass_chrs_alpha_low = "qwertyuioplkjhgfgfddsazxcvbnm"
    pass_chrs_alpha_up = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    pass_chrs_syms = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

    pass_len = random.randint(12, 16)

    pass_chrs_nums = random.sample(pass_chrs_nums, 3)
    pass_chrs_syms = random.sample(pass_chrs_syms, 3)
    pass_chrs_alpha_up = random.sample(pass_chrs_alpha_up, 3)
    pass_chrs_alpha_low = random.sample(pass_chrs_alpha_low, pass_len - 9)

    password_entry.delete("0", "end")
    
    pass_key = pass_chrs_nums + pass_chrs_syms + pass_chrs_alpha_low + pass_chrs_alpha_up
    random.shuffle(pass_key)
    pass_key = "".join(pass_key)

    password_entry.insert(0, pass_key)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    '''
    Saves the credintials to the json file.
    '''
    website = website_entry.get()
    username = name_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showerror(
            title="Invalid Details", message="Don't keep any enteries empty\nPlease enter all the details")
        return

    status = messagebox.askyesno(
        "Confirmation", f"Save the Details ?\nURL : {website}\nUsername : {username}\npassword : {password}")
    if status:
        pass
    else:
        return

    new_creds = {
        "username": username,
        "password": password
    }
    


    try:
        with open("saved_password.json", "r+") as f:
            json_obj = json.load(f)

    except Exception as err:
        messagebox.showerror(title= err.__doc__ ,message = err)
        
        print("File 'saved_password' doesn't exist")

        new_creds = {website : {
        "username": username,
        "password": password
        }}

        with open("saved_password.json", "w") as f:
            json.dump(new_creds, f, indent=3)

        messagebox.showinfo(title= "Acknowlegment", message= "A new file saved_password.json is created.")
        print("Created new 'saved_password.json' file")

    
    else:
        json_obj[website] = new_creds
        with open('saved_password.json', "w") as f:
            f.write(json.dumps(json_obj, indent= 3 ))

    website_entry.delete(0, "end")
    name_entry.delete(0, "end")
    password_entry.delete(0, "end")

    msg = f'''Password Saved succesfully
    URL : {website}
    Username : {username}
    password : *****{password[-3:]}
    '''
    messagebox.showinfo(title="Details Added", message=msg)


# ---------------------------- SEARCH ------------------------------- #



def search():
    try:
        _website = website_entry.get()
        with open("saved_password.json", 'r+') as f:
            obj = json.load(f)
  
    except FileNotFoundError:
            messagebox.showerror(title="Oops!!", message="Looks like you have not started saving passwords yet!")
    
    else:
        if _website in obj:
            username = obj[_website]["username"]
            password = obj[_website]["password"]
            messagebox.showinfo(title= _website, message= f"Username : {username}\nPassword : {password}")
        else:
            messagebox.showerror(title= "Something went wrong !", message= f'{_website} is not found in saved passwords')




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title(" - - - Personal Password Manager - - - ")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
icon_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=icon_img)


name_label = Label(text="Username")
password_label = Label(text="Password")
website_label = Label(text="Website URL")


website_entry = Entry(width=36)
name_entry = Entry(width=56)
password_entry = Entry(width=36)


gen_button = Button(text="Generate Password", width=15, command=pass_gen)
add_button = Button(text="Add to Manager", width=47, command=save_pass)
search_button = Button(text= "Search", width= 15, command= search)


canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=1, sticky=W)
name_label.grid(row=2, column=0)
name_entry.grid(row=2, column=1, columnspan=2, sticky=W)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, sticky=W)
gen_button.grid(row=3, column=2, sticky=E)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row = 1, column= 2, sticky= E)


website_entry.focus()
window.mainloop()

