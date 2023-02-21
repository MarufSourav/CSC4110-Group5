"""Group Project 1
Matthew Krol START version 1, 2/8/23
"""
from tkinter import *
import tkinter.font as font
import csv
import os
import re
import pyperclip

#Create list
data=[]

#Setting up GUI
root = Tk(className='Group Project 1')
import_frame = Frame(root, background='red')
store_frame = Frame(root, background='red')
search_frame = Frame(root, background='red')
delete_frame = Frame(root, background='red')
root.geometry("500x500")
root.configure(bg='red')
quit_font = font.Font(family='Comic Sans', size=20, weight='bold')
root_button_font = font.Font(family='Comic Sans', size=16, weight='bold')

#Variables for entries
name_var = StringVar()
position_var = StringVar()
ssn_var = StringVar()
address_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
skill_var = StringVar()
file_var = StringVar()
search_var = StringVar()
delete_var = StringVar()

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
    if not check_position(position):
        return
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
    """This fucntion imports data"""
    #Destroy Entry and Label for double clicks
    destroy_children(store_frame)
    destroy_children(search_frame)
    destroy_children(import_frame)
    destroy_children(delete_frame)
    import_frame.pack()
    #Create label and entry for file name
    Label(import_frame, text="Enter file name", background="red").pack()
    file_entry=Entry(import_frame, textvariable=file_var)
    file_entry.focus_set()
    file_entry.pack()
    #create button to submit file name
    sub_btn=Button(import_frame, text = 'Submit file', command =lambda: [open_file(),
    destroy_children(import_frame), sub_btn.destroy()])
    sub_btn.pack(pady=10)

    #set file name back to nothing
    file_var.set("")

def search_data():
    """This fucntion searches data"""
    #Destroying old widgets
    destroy_children(store_frame)
    destroy_children(search_frame)
    destroy_children(import_frame)
    destroy_children(delete_frame)

    search_frame.pack()
    #create Entry and Label for search
    Label(search_frame, text="Search", background="red").pack()
    search_entry=Entry(search_frame, textvariable=search_var)
    search_entry.focus_set()
    search_entry.pack()
    #create search buttons
    search_name_btn = Button(search_frame, text="Search Name", command=lambda:[search_name(),
    destroy_children(search_frame), search_name_btn.destroy(),search_position_bt.destroy(),
    search_ssn_btn.destroy(),search_email_btn.destroy(),search_skill_btn.destroy()])
    search_name_btn.pack(pady=5)
    search_position_bt=Button(search_frame,text="Search Position",command=lambda:[search_position(),
    destroy_children(search_frame), search_name_btn.destroy(),search_position_bt.destroy(),
    search_ssn_btn.destroy(),search_email_btn.destroy(),search_skill_btn.destroy()])
    search_position_bt.pack(pady=5)
    search_ssn_btn=Button(search_frame,text="Search SSN",command=lambda:[search_ssn(),
    destroy_children(search_frame), search_name_btn.destroy(),search_position_bt.destroy(),
    search_ssn_btn.destroy(),search_email_btn.destroy(),search_skill_btn.destroy()])
    search_ssn_btn.pack(pady=5)
    search_email_btn=Button(search_frame,text="Search Email",command=lambda:[search_email(),
    destroy_children(search_frame), search_name_btn.destroy(),search_position_bt.destroy(),
    search_ssn_btn.destroy(),search_email_btn.destroy(),search_skill_btn.destroy()])
    search_email_btn.pack(pady=5)
    search_skill_btn=Button(search_frame,text="Search Skill",command=lambda:[search_skill(),
    destroy_children(search_frame), search_name_btn.destroy(),search_position_bt.destroy(),
    search_ssn_btn.destroy(),search_email_btn.destroy(),search_skill_btn.destroy()])
    search_skill_btn.pack(pady=5)

def delete_data():
    """This fucntion will delete the data"""
    destroy_children(store_frame)
    destroy_children(search_frame)
    destroy_children(import_frame)
    destroy_children(delete_frame)

    delete_frame.pack()
    #Creating Label and Entry for deleting
    Label(delete_frame, text="Delete this row from the list by SSN", background="red").pack()
    search_entry=Entry(delete_frame, textvariable=delete_var)
    search_entry.focus_set()
    search_entry.pack()

    #Create button to delete ssn
    delete_ssn_btn=Button(delete_frame,text="Delete", command=lambda:[delete_snn(),
    destroy_children(delete_frame)])
    delete_ssn_btn.pack(pady=5)

def delete_snn():
    """This funcion will delete the row from the table"""
    ssn_delete = delete_var.get()
    if not check_ssn(ssn_delete):
        return
    flag=True
    for ssn in data:
        if ssn_delete == ssn[2]:
            temp_ssn = ssn
            data.remove(ssn)
            flag=False
    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("SSN not found")
        file_window.geometry("400x100")
        Label(file_window, text="That SSN was not found").pack()
        #Set variable back to empty
        delete_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("This SSN deleted")
        file_window.geometry("800x100")
        Label(file_window, text=temp_ssn).pack()
        delete_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(temp_ssn))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()


def search_name():
    """This function will search name"""
    #Get name from entry
    name_serach = search_var.get()
    flag=True
    name_list=[]
    #search data for name
    for name in data:
        if name_serach == name[0]:
            name_list.append(name)
            flag=False
    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("Name search not found")
        file_window.geometry("400x100")
        Label(file_window, text="That name was not found").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("Name search found")
        file_window.geometry("800x100")
        for name in name_list:
            Label(file_window, text=name).pack()
        search_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(name_list))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()

def search_position():
    """This function will search position"""
    #Get name from entry
    position_serach = search_var.get()
    check_position(position_serach)
    position_list=[]
    flag=True
    #search data for position
    for position in data:
        if position_serach == position[1]:
            position_list.append(position)
            flag=False

    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("Position search not found")
        file_window.geometry("400x100")
        Label(file_window, text="That position was not found").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("Position search found")
        file_window.geometry("800x800")
        for position in position_list:
            Label(file_window, text=position).pack()
        search_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(position_list))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()

def search_ssn():
    """Searching for ssn number"""
    ssn_serach = search_var.get()
    if not check_ssn(ssn_serach):
        return
    ssn_list=[]
    flag=True
    #search data for position
    for ssn in data:
        if ssn_serach == ssn[2]:
            ssn_list.append(ssn)
            flag=False

    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("SSN search not found")
        file_window.geometry("400x100")
        Label(file_window, text="That SSN was not found").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("SSN search found")
        file_window.geometry("600x100")
        for ssn in ssn_list:
            Label(file_window, text=ssn).pack()
        search_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(ssn_list))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()

def search_email():
    """Function to search for an email address in data"""
    email_search = search_var.get()
    if not check_email(email_search):
        return
    email_list=[]
    flag=True
    for email in data:
        if email_search == email[4]:
            email_list.append(email)
            flag=False
    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("Email search not found")
        file_window.geometry("400x100")
        Label(file_window, text="That Email was not found").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("Email search found")
        file_window.geometry("600x100")
        for email in email_list:
            Label(file_window, text=email).pack()
        search_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(email_list))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()

def search_skill():
    """Function to search for an email address in data"""
    skill_search = search_var.get()
    skill_search_list =['Office', 'Python', 'Sales', 'Leader', 'Networking', 'Business']
    if skill_search not in skill_search_list:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("Skill search not found")
        file_window.geometry("400x100")
        Label(file_window, text="That is not a skill\nPlease enter a correct skill").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    skill_list=[]
    flag=True
    for skill in data:
        if skill_search == skill[6]:
            skill_list.append(skill)
            flag=False
    if flag:
        #Print window with not found
        file_window = Toplevel(root)
        file_window.title("Skill search not found")
        file_window.geometry("400x100")
        Label(file_window, text="No one has that skill").pack()
        #Set variable back to empty
        search_var.set("")
        Button(file_window, text="Quit", command=file_window.destroy).pack()
    else:
        #print window with found
        file_window = Toplevel(root)
        file_window.title("Skill search found")
        file_window.geometry("800x800")
        for skill in skill_list:
            Label(file_window, text=skill).pack()
        search_var.set("")
        Button(file_window, text="Copy", command=pyperclip.copy(str(skill_list))).pack()
        Button(file_window, text="Quit", command=file_window.destroy).pack()

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

def destroy_children(frame):
    """Destroy children of a frame"""
    for widget in reversed(frame.winfo_children()):
        widget.destroy()
    frame.pack_forget()

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
    if re.match(r"\(\d{3}\)\d{3}-\d{4}",phone):
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

def check_position(position):
    """Checking if position is correct"""
    position_check_list = ['Helper', 'Manager', 'Assistant Manager', 'Staff', 'Employee']
    for position_check in position_check_list:
        if position_check == position:
            return True
    position_window = Toplevel(root)
    position_window.title("email error")
    position_window.geometry("450x50")
    Label(position_window, text="The position was not the correct\n\
            Please try again (Manager, Assistant Manager, Helper, Staff, Employee)").pack()
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

def store_data_entry():
    """Creating an entry for storing data"""

    #Destroy widgets in frames
    destroy_children(store_frame)
    destroy_children(search_frame)
    destroy_children(import_frame)
    destroy_children(delete_frame)

    store_frame.pack()
    #create Labels and Entry for store data
    Label(store_frame, text="Enter Name", background="red").pack()
    name_entry=Entry(store_frame, textvariable=name_var)
    name_entry.focus_set()
    name_entry.pack(pady=2)

    Label(store_frame, text="Enter position", background="red").pack(pady=2)
    Entry(store_frame, textvariable=position_var).pack(pady=2)

    Label(store_frame, text="Enter ssn", background="red").pack(pady=2)
    Entry(store_frame, textvariable=ssn_var).pack(pady=2)

    Label(store_frame, text="Enter address", background="red").pack(pady=2)
    Entry(store_frame, textvariable=address_var).pack(pady=2)

    Label(store_frame, text="Enter email", background="red").pack(pady=2)
    Entry(store_frame, textvariable=email_var).pack(pady=2)

    Label(store_frame, text="Enter phone number, ex (888)555-4545", background="red").pack(pady=2)
    Entry(store_frame, textvariable=phone_var).pack(pady=2)

    Label(store_frame, text="Enter skill", background="red").pack(pady=2)
    Entry(store_frame, textvariable=skill_var).pack(pady=2)

    #Make submit button, and clear all entries and labels
    sub_all_btn=Button(store_frame,text='Submit all',command=lambda:[add_data(),
    destroy_children(store_frame), sub_all_btn.destroy()])
    sub_all_btn.pack(pady=10)

#Creating buttons
Button(root, text='Quit', bg='#022CC8',fg='#52FD44', font=quit_font,
       command=root.destroy).place(x=420, y=445)
Button(root, text='Store', bg='#022CC8',fg='#52FD44',font=root_button_font,
       command=store_data_entry).place(x=20, y=20)
Button(root, text='Import', bg='#022CC8',fg='#52FD44',font=root_button_font,
       command=import_data).place(x=20, y=80)
Button(root, text='Search', bg='#022CC8',fg='#52FD44',font=root_button_font,
       command=search_data).place(x=20, y=140)
Button(root, text='Delete', bg='#022CC8',fg='#52FD44', font=root_button_font,
       command=delete_data).place(x=20, y=200)


#Making Main run
root.mainloop()

#Group Project 1
#Matthew Krol END version 5, 2/20/23
