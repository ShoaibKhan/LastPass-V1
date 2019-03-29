from tkinter import *
from password_generator import *

lower_checked = 0
upper_checked = 0
num_checked = 0
spec_checked = 0

def info_popup():
    win = Toplevel()
    win.wm_title("More Info")

    l = Label(win, text="In order to generate a unique and secure password, please enter your username, and master-password. \n Tips on creating a secure password: \n 1. Choose the max-length of characters allowed \n 2. Select all the special password options that the website allows (ie: special characters, capitals, numbers, etc.) ", fg="#00FF00",bg='Black')
    l.grid(row=0, column=0)

    close = Button(win, text="Close", command=win.destroy,bg="Red", fg="Black")
    close.grid(row=1, column=0)

    win.configure(background='Black')


def set_text(entry, text):
    entry.config(state=NORMAL)
    entry.delete(1.0, END)
    entry.insert("end", text)
    entry.config(state=DISABLED)
    entry.update()


def display_passowrd(event):
    if lower_state.get():
        lower_checked = 1
    else:
        lower_checked = 0
    if upper_state.get():
        upper_checked = 1
    else:
        upper_checked = 0
    if nums_state.get():
        num_checked = 1
    else:
        num_checked = 0
    if special_char_state.get():
        spec_checked = 1
    else:
        spec_checked = 0

    website = entry_website.get()
    user_name = entry_user.get()
    master_password = entry_master_pass.get()
    length = entry_passwrd_len.get()
    length = int(length)

    if not (website and user_name and master_password and (length >= 8 and length <= 20) and (lower_checked or upper_checked or num_checked or spec_checked)):
        return

    password = generate_password(website, user_name, master_password, length, lower_checked, upper_checked, num_checked, spec_checked)
    set_text(psswrd_generated, password)
    print("Secure Password Generated!")


root = Tk()

lower_state, upper_state, nums_state, special_char_state = IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)

lower = Checkbutton(root, text="Lowercase", fg="#00FF00",bg="Black", variable=lower_state)
upper = Checkbutton(root, text="Uppercase", fg="#00FF00",bg="Black", variable=upper_state)
nums = Checkbutton(root, text="Numbers", fg="#00FF00",bg="Black", variable=nums_state)
special_char = Checkbutton(root, text="Special Characters", fg="#00FF00", bg="Black", variable=special_char_state)


lower.grid(row=6, column=0)
upper.grid(row=6, column=1)
nums.grid(row=7, column=0)
special_char.grid(row=7, column=1)

label_website = Label(root, text="Domain name: ", fg="#00FF00", bg='Black')
entry_website = Entry(root)
label_website.grid(row=0, column=0)
entry_website.grid(row=0, column=1)

label_user = Label(root, text="Username: ", fg="#00FF00", bg='Black')
entry_user = Entry(root)
label_user.grid(row=1, column=0)
entry_user.grid(row=1, column=1)

label_master_pass = Label(
    root, text="Master password: ", fg="#00FF00", bg='Black')
entry_master_pass = Entry(root, show="*")
label_master_pass.grid(row=2, column=0)
entry_master_pass.grid(row=2, column=1)

label_passwrd_len = Label(
    root, text="Password length desired: ", fg="#00FF00", bg='Black')
entry_passwrd_len = Entry(root)
label_passwrd_len.grid(row=4, column=0)
entry_passwrd_len.grid(row=4, column=1)

button_generate = Button(root, text="Generate", height=3,width=15, bg="Red", fg="Black")
psswrd_generated = Text(root, state=DISABLED, height=5, width=16)

button_generate.bind("<Button-1>", display_passowrd)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="More Info", command=info_popup)
menubar.add_cascade(label="Help", menu=filemenu)
root.config(menu=menubar)

button_generate.grid(row=5, column=0)
psswrd_generated.grid(row=5, column=1)

root.title("Wut are vulnerabilities?")
root.configure(background='Black')

root.mainloop()
