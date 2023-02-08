#Group Project 1
#Matthew Krol START version 1, 2/8/23
from tkinter import *
import tkinter.font as font
import csv
import os

#Setting up GUI
root = Tk(className='Group Project 1')
root.geometry("500x500")
root.configure(bg='red')
myFont = font.Font(family='Helvetica', size=20, weight='bold')

store_data_var = StringVar()

def add_data():
    """This function stores the data"""
    #Creates the entry box
    data = store_data_var.get()
    print(data)
    store_data_var.set("")
    

def import_data():
    """This fucntion collects data"""
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'assests/employees.csv'),'r', encoding="utf-8")
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
    file.close()

def search_data():
    """This fucntion searches data"""
    pass

def delete_data():
    """This fucntion will delete the data"""
    pass

def clear_entry(entry):
    """To handle clearing an entry"""
    entry.destroy()



#Making Entry
def store_data_entry():
    """Creating an entry for storing data"""
    store_entry=Entry(root, textvariable=store_data_var)
    store_entry.focus_set()
    store_entry.place(x=90, y = 20)
    sub_btn=Button(root, text = 'Submit', command =lambda: [add_data(), clear_entry(store_entry), sub_btn.place_forget()])
    sub_btn.place(x=250, y = 20)

#Creating buttons
quit_btn = Button(root, text='Quit', bg='#022CC8',fg='#52FD44', command=root.destroy)
store_btn = Button(root, text='Store', bg='#022CC8',fg='#52FD44', command=store_data_entry)
collect_btn = Button(root, text='Collect', bg='#022CC8',fg='#52FD44', command=import_data)

quit_btn['font'] = myFont


#Making the button display
quit_btn.place(x=420, y=445)
store_btn.place(x=20, y=20)
collect_btn.place(x=20, y=80)


#Making Main run
root.mainloop()

#Group Project 1
#Matthew Krol END version 1, 2/8/23
