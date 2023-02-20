"""Group Project 1
Matthew Krol START version 1, 2/8/23
"""
from tkinter import *
import tkinter.font as font
import csv
import os
import re

#Create list
data=[]

#Setting up GUI
root = Tk(className='Group Project 1')
root.geometry("500x500")
root.configure(bg='red')
myFont = font.Font(family='Comic Sans', size=20, weight='bold')

#Variables for entries
name_var = StringVar()
position_var = StringVar()
ssn_var = StringVar()
address_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
skill_var = StringVar()
file_var = StringVar()

def add_data():
    """This function stores the data"""
    add_data_list = []
    #Grabs the entries
    name = name_var.get()
    position = position_var.get()
    ssn = ssn_var.get()
    address = address_var.get()
    email = email_var.get()
    phone = phone_var.get()
    skill = skill_var.get()
    #checks for entries if correct
    if not check_ssn(ssn):
        return
    if not check_email(email):
        return
    if not check_phone(phone):
        return
    #add to a temp list
    add_data_list.append(name)
    add_data_list.append(position)
    add_data_list.append(ssn)
    add_data_list.append(address)
    add_data_list.append(email)
    add_data_list.append(phone)
    add_data_list.append(skill)
    #Set the variables back to empty
    name_var.set("")
    position_var.set("")
    ssn_var.set("")
    address_var.set("")
    email_var.set("")
    phone_var.set("")
    skill_var.set("")

    data.append(add_data_list)

def import_data():
    """This fucntion collects data"""
    #Create label and entry for file name
    file_label=Label(text="Enter file name", background="red")
    file_label.place(x=90, y=0)
    file_entry=Entry(root, textvariable=file_var)
    file_entry.focus_set()
    file_entry.place(x=90, y = 20)
    #create button to submit file name
    sub_btn=Button(root, text = 'Submit file', command =lambda: [open_file(),
        clear_entry(file_entry),clear_label(file_label), sub_btn.place_forget()])
    sub_btn.place(x=90, y=50)
    #set file name back to nothing
    file_var.set("")

def search_data():
    """This fucntion searches data"""
    pass

def delete_data():
    """This fucntion will delete the data"""
    pass

def file_error_window():
    """Open an error window"""
    # Toplevel object which will
    # be treated as a new window
    file_window = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    file_window.title("File Not Found")

    # sets the geometry of toplevel
    file_window.geometry("400x50")

    # A Label widget to show in toplevel
    Label(file_window, text ="The File was not found, Try again").pack()

def clear_entry(entry):
    """To handle clearing an entry"""
    entry.destroy()

def clear_label(label):
    """To heandle clearing labels"""
    label.destroy()

def check_ssn(ssn):
    """Checking if ssn is right"""
    if ssn.isnumeric() and len(ssn) == 9:
        return True
    ssn_window = Toplevel(root)
    ssn_window.title("ssn error")
    ssn_window.geometry("400x50")
    Label(ssn_window, text="The ssn was not the correct format\nTry with just numbers").pack()
    return False

def check_phone(phone):
    """Check if phone is correct format"""
    if re.match("\(\d{3}\)\d{3}-\d{4}",phone):
        return True
    phone_window = Toplevel(root)
    phone_window.title("phone number error")
    phone_window.geometry("400x50")
    Label(phone_window, text="The phone number was not the correct format\n\
            Try in the format of (888)555-4545").pack()
    return False

def check_email(email):
    """Check if email is correct"""
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        return True
    email_window = Toplevel(root)
    email_window.title("email error")
    email_window.geometry("400x50")
    Label(email_window, text="The email was not the correct format\n\
            Please try again").pack()
    return False


def open_file():
    """Open file and get data"""
    #get file name from entry
    file_name = file_var.get()
    #Get location of file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    #try to open file and import data, otherwise print error
    try:
        file = open(os.path.join(__location__, file_name),'r', encoding="utf-8")
        imported_data = csv.reader(file)
        for row in imported_data:
            data.append(row)
        file.close()
    except FileNotFoundError:
        file_error_window()

#Making Entry
def store_data_entry():
    """Creating an entry for storing data"""
    name_label=Label(text="Enter Name", background="red")
    name_label.place(x=90, y=0)
    name_entry=Entry(root, textvariable=name_var)
    name_entry.focus_set()
    name_entry.place(x=90, y = 20)

    position_label=Label(text="Enter position", background="red")
    position_label.place(x=90, y=40)
    position_entry=Entry(root, textvariable=position_var)
    position_entry.place(x=90, y = 60)

    ssn_label=Label(text="Enter ssn", background="red")
    ssn_label.place(x=90, y=80)
    ssn_entry=Entry(root, textvariable=ssn_var)
    ssn_entry.place(x=90, y = 100)

    address_label=Label(text="Enter address", background="red")
    address_label.place(x=90, y=120)
    address_entry=Entry(root, textvariable=address_var)
    address_entry.place(x=90, y = 140)

    email_label=Label(text="Enter email", background="red")
    email_label.place(x=90, y=160)
    email_entry=Entry(root, textvariable=email_var)
    email_entry.place(x=90, y = 180)

    phone_label=Label(text="Enter phone number, ex (888)555-4545", background="red")
    phone_label.place(x=90, y=200)
    phone_entry=Entry(root, textvariable=phone_var)
    phone_entry.place(x=90, y = 220)

    skill_label=Label(text="Enter skill", background="red")
    skill_label.place(x=90, y=240)
    skill_entry=Entry(root, textvariable=skill_var)
    skill_entry.place(x=90, y = 260)

    #Make submit button, and clear all entries and labels
    sub_all_btn=Button(root,text='Submit all',command =lambda:[add_data(), clear_entry(name_entry),
    clear_entry(position_entry), clear_entry(ssn_entry), clear_entry(address_entry),
    clear_entry(email_entry),clear_entry(phone_entry),clear_entry(skill_entry),
    clear_label(name_label),clear_label(position_label),clear_label(ssn_label),
    clear_label(address_label),clear_label(email_label),clear_label(phone_label),
    clear_label(skill_label), sub_all_btn.place_forget()])
    sub_all_btn.place(x=90, y = 300)

#Creating buttons
quit_btn = Button(root, text='Quit', bg='#022CC8',fg='#52FD44', command=root.destroy)
store_btn = Button(root, text='Store', bg='#022CC8',fg='#52FD44', command=store_data_entry)
collect_btn = Button(root, text='Collect', bg='#022CC8',fg='#52FD44', command=import_data)
search_btn = Button(root, text='Search', bg='#022CC8',fg='#52FD44', command=search_data)

quit_btn['font'] = myFont


#Making the button display
quit_btn.place(x=420, y=445)
store_btn.place(x=20, y=20)
collect_btn.place(x=20, y=80)
search_btn.place(x=20, y=140)


#Making Main run
root.mainloop()

#Group Project 1
#Matthew Krol END version 2, 2/8/23

for employee in data:
    print(employee, "\n")
