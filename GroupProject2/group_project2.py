""""Group Project 2 Revsion 1 3/13/23"""
from tkinter import *
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import messagebox

import json
import os
import time
import re
from datetime import date, datetime
from PIL import Image, ImageTk


__location__ = os.path.dirname(os.path.realpath(__file__))
ORDER_NUMBER = 0
file = open(os.path.join(__location__,"logs/Order_File.txt"),
    mode="a+", encoding="utf-8")
file.write(f"Today's Date: {str(date.today())}\n")
file.close()
employee_name = "No one"
class PizzaApp(tk.Tk):
    """Class for Pizza app"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Group Project 2")
        self.geometry("1000x1000")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, ClockPage, CustomerPage, ManagerPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        with open(os.path.join(__location__,"logs/employeeslog.txt"),
            mode="a+", encoding="utf-8") as emp_file:
            emp_file.write(f"{employee_name} logged into: {page_name}\n")
            emp_file.close()
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame,PizzaApp):
    """Starting page for the pizza application"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="blue")
        #get image link
        self.clock =(os.path.abspath(os.path.join(__location__, "assests/timeclock.png")))
        self.menu =(os.path.abspath(os.path.join(__location__, "assests/menu.png")))
        self.exit =(os.path.abspath(os.path.join(__location__, "assests/exit.png")))
        self.manager =(os.path.abspath(os.path.join(__location__, "assests/manager.png")))
        self.customer =(os.path.abspath(os.path.join(__location__, "assests/customer.png")))
        self.login =(os.path.abspath(os.path.join(__location__, "assests/login.png")))
        # Open image using PIL
        self.clock = Image.open(self.clock)
        self.clock = self.clock.resize((200,200))
        self.menu = Image.open(self.menu)
        self.menu = self.menu.resize((200,200))
        self.exit = Image.open(self.exit)
        self.exit = self.exit.resize((200,200))
        self.manager = Image.open(self.manager)
        self.manager = self.manager.resize((200,200))
        self.customer = Image.open(self.customer)
        self.customer = self.customer.resize((200,200))
        self.login = Image.open(self.login)
        self.login = self.login.resize((200,200))

        # Convert the PIL image object to a Tkinter PhotoImage object
        self.clock = ImageTk.PhotoImage(self.clock)
        self.menu = ImageTk.PhotoImage(self.menu)
        self.exit = ImageTk.PhotoImage(self.exit)
        self.manager = ImageTk.PhotoImage(self.manager)
        self.customer = ImageTk.PhotoImage(self.customer)
        self.login = ImageTk.PhotoImage(self.login)

        # Create a button widget with the image
        tk.Button(self, text='TIME CLOCK', image=self.clock,compound='top',bg='blue',borderwidth=0,
            command=lambda:controller.show_frame("ClockPage")).place(x=400,y=50)
        tk.Button(self, text="MENU", image=self.menu,compound='top',bg='blue',borderwidth=0,command=
            lambda: self.log_in_fn("MenuPage")).place(x=400,y=700)
        tk.Button(self, text="Manager",image=self.manager,compound='top',bg='blue',borderwidth=0,
            command=lambda: self.log_in_fn("ManagerPage")).place(x=700,y=400)
        tk.Button(self, text="Exit",image=self.exit,compound='top',bg='blue',borderwidth=0,
            command=self.exit_program).place(x=800,y=775)
        tk.Button(self, image=self.customer,compound='top',bg='blue',borderwidth=0,
            text="Customer",command=lambda:self.log_in_fn("CustomerPage")).place(x=100,y=400)
        tk.Button(self, image=self.login,compound='top',bg='blue',borderwidth=0,
            text="Login",command=self.login_page).place(x=0,y=775)

        label=tk.Label(self,bg="blue",text="BLUE LATERN\nPIZZA APP",font=(controller.title_font,30))
        label.place(x=380,y=475)
    def log_in_fn(self, frame):
        """Function to determine if someone is logged in"""
        if employee_name == "No one":
            messagebox.showerror("Login", "Must be logged in.")
            return
        else:
            self.controller.show_frame(frame)
    def exit_program(self):
        """Exiting the program"""
        #Add logging
        with open(os.path.join(__location__,"logs/employeeslog.txt"),
            mode="a+", encoding="utf-8") as emp_file:
            emp_file.write(f"You have exited the program for today {str(date.today())}\n\n\n\n")
            emp_file.close()
        self.controller.destroy()

    def login_page(self):
        """Page for logging in"""
        #Create the window for logging in
        self.login_win = tk.Toplevel()
        self.login_win.title("Log in")
        self.login_win.geometry("200x100")
        self.login_win.configure(background = "blue")

        emp_label = Label(self,bg="blue", text="Enter your 4 digit employee pin")
        emp_label.pack()
        self.emp_pin = Entry(self.login_win, width=10)
        self.emp_pin.focus_set()
        self.emp_pin.pack()
        Button(self.login_win, text="Log in", command=self.login_page_log).pack()
        Button(self.login_win, text="Quit", command=self.login_win.destroy).pack()

    def login_page_log(self):
        """Fucntion to give a success message after logging in"""
        if self.validate_pin() == 1:
            with open(os.path.join(__location__,"logs/employeeslog.txt"),
                mode="a+", encoding="utf-8") as emp_file:
                emp_file.write(f"{employee_name} has successfully logged in.\n")
                emp_file.close()
            messagebox.showinfo("Logged in", f"{employee_name} has logged in successfully")
            self.login_win.destroy()
        else:
            return

    def validate_pin(self):
        """Validating the Pin"""
        n = 0
        global employee_name
        if self.emp_pin.get() == "":
            messagebox.showerror("Error", "Invalid pin. Please try again.")
            return
        #make sure pin is valid by searching for employee number in employee file
        with open(os.path.join(__location__,"logs/employees.txt"), 'r', encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if self.emp_pin.get() in line:
                    employee_name = re.split(r'\s+(?=\d)|(?<=\d)\s+', line)[0]
                    n = 1
        self.emp_pin.delete(0,END)
        #invalid pin error message
        if n != 1:
            messagebox.showerror("Error", "Invalid pin. Please try again.")
            return n
        return n


class MenuPage(StartPage):
    """Menu page for the pizza application"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='blue')

        global order_box
        self.piz_frame = tk.Frame(self)
        self.sid_frame = tk.Frame(self)
        order_box = tk.Listbox(self)
        self.menu_start()

    def menu_start(self):
        """Menu Start"""
        #Boolean variables
        global pep, ham, bacon, sausage, mushroom, green_pepper, onion, banana_pepper
        global small,medium,large,deep_dish, round, thin_crust, pizza_sauce,alfredo_sauce,bbq_sauce
        global breadstick
        global carryout, pick_up, delivery

        pep = tk.BooleanVar(name="Pepperoni")
        ham= tk.BooleanVar(name="Ham")
        bacon = tk.BooleanVar(name="Bacon")
        sausage = tk.BooleanVar(name="Sausage")
        mushroom = tk.BooleanVar(name="Mushroom")
        green_pepper = tk.BooleanVar(name="Green Pepper")
        onion = tk.BooleanVar(name="Onion")
        banana_pepper = tk.BooleanVar(name="Banana Pepper")
        deep_dish = tk.BooleanVar(name="Deep Dish")
        round = tk.BooleanVar(name="Round")
        thin_crust = tk.BooleanVar(name="Thin Crust")
        pizza_sauce = tk.BooleanVar(name="Pizza Sauce")
        alfredo_sauce = tk.BooleanVar(name="Alfredo Sauce")
        bbq_sauce = tk.BooleanVar(name="BBQ Sauce")
        small = tk.BooleanVar(name="Small")
        medium = tk.BooleanVar(name="Medium")
        large = tk.BooleanVar(name="Large")
        breadstick = tk.BooleanVar(name="Breaksticks")
        carryout = tk.BooleanVar(name="Carryout")
        pick_up = tk.BooleanVar(name="Pickup")
        delivery = tk.BooleanVar(name="Delivery")

        global toppings, size, sauce, pizza, side, order_type, order_box
        toppings = [pep, ham, bacon, sausage, mushroom, green_pepper, onion, banana_pepper]
        size = [small,medium,large]
        pizza = [deep_dish,round,thin_crust]
        sauce = [pizza_sauce,alfredo_sauce,bbq_sauce]
        side = [breadstick]
        order_type = [carryout,pick_up,delivery]


        #Button images
        self.customer =(os.path.abspath(os.path.join(__location__, "assests/customer.png")))
        self.add_item =(os.path.abspath(os.path.join(__location__, "assests/add_item.png")))
        self.submit_order =(os.path.abspath(os.path.join(__location__, "assests/submit_order.png")))
        self.exit =(os.path.abspath(os.path.join(__location__, "assests/exit.png")))
        self.delete_item =(os.path.abspath(os.path.join(__location__, "assests/delete_item.png")))

        self.customer = Image.open(self.customer)
        self.customer = self.customer.resize((190,160))
        self.add_item = Image.open(self.add_item)
        self.add_item = self.add_item.resize((190,160))
        self.submit_order = Image.open(self.submit_order)
        self.submit_order = self.submit_order.resize((190,160))
        self.exit = Image.open(self.exit)
        self.exit = self.exit.resize((190,160))
        self.delete_item = Image.open(self.delete_item)
        self.delete_item = self.delete_item.resize((190,160))

        self.customer = ImageTk.PhotoImage(self.customer)
        self.add_item = ImageTk.PhotoImage(self.add_item)
        self.submit_order = ImageTk.PhotoImage(self.submit_order)
        self.exit = ImageTk.PhotoImage(self.exit)
        self.delete_item = ImageTk.PhotoImage(self.delete_item)

        #Order List
        scroll_bar = tk.Scrollbar(self,orient="vertical")
        scroll_bar.place(x=250,y=30)
        order_box.config(width=45,height=48,borderwidth=0,
            yscrollcommand=scroll_bar.set)
        order_box.place(x=0,y=29)

        #Main Buttons
        tk.Checkbutton(self,variable=carryout, text="Carryout", font=14,
            command=self.carryout_fn).place(x=0,y=0)
        tk.Checkbutton(self,variable=pick_up, text="Pick Up",font=14,
            command=self.pickup_fn).place(x=88,y=0)
        tk.Checkbutton(self,variable=delivery, text="Delivery",font=14,
            command=self.delivery_fn).place(x=173,y=0)

        tk.Button(self, text="Pizza",width=10,command=self.pizza_frame).place(x=275,y=30)
        tk.Button(self, text="Sides",width=10,command=self.side_frame).place(x=275,y=60)

        tk.Button(self, image=self.customer,compound="top",text="Customer",
            command=lambda: self.controller.show_frame("CustomerPage")).place(x=0,y=810)
        tk.Button(self, image=self.add_item,compound="top",
            text="Add Item", command=self.add_item_fn).place(x=200,y=810)
        tk.Button(self, image=self.delete_item,compound="top",text="Delete Item",
            command=self.delete_item_fn).place(x=400,y=810)
        tk.Button(self, image=self.submit_order,compound="top",text="Submit Order",
            command=self.submit_order_fn).place(x=600,y=810)
        tk.Button(self, image=self.exit,compound="top",
            text="Exit", command=self.exit_fn).place(x=800,y=810)

    def pizza_frame(self):
        """Pizza fram for menu"""
        global PIZZA_FRAME_VAR
        global SIDE_FRAME_VAR
        PIZZA_FRAME_VAR = True
        SIDE_FRAME_VAR=False
        self.destroy_children(self.sid_frame)
        self.piz_frame.configure(bg='blue',width=640,height=780)
        self.piz_frame.place(x=360,y=30)
        #get image link
        self.pep =(os.path.abspath
            (os.path.join(__location__, "assests/pep.png")))
        self.ham =(os.path.abspath
            (os.path.join(__location__, "assests/ham.png")))
        self.bacon =(os.path.abspath
            (os.path.join(__location__, "assests/bacon.png")))
        self.sausage =(os.path.abspath
            (os.path.join(__location__, "assests/sausage.png")))
        self.mushroom =(os.path.abspath
            (os.path.join(__location__, "assests/mushroom.png")))
        self.green_pepper =(os.path.abspath
            (os.path.join(__location__, "assests/green_pepper.png")))
        self.onion =(os.path.abspath
            (os.path.join(__location__, "assests/onion.png")))
        self.banana_pepper =(os.path.abspath
            (os.path.join(__location__, "assests/banana_pepper.png")))

        # Open image using PIL
        self.pep = Image.open(self.pep)
        self.pep = self.pep.resize((50,50))
        self.ham = Image.open(self.ham)
        self.ham = self.ham.resize((50,50))
        self.bacon = Image.open(self.bacon)
        self.bacon = self.bacon.resize((50,50))
        self.sausage = Image.open(self.sausage)
        self.sausage = self.sausage.resize((50,50))
        self.mushroom = Image.open(self.mushroom)
        self.mushroom = self.mushroom.resize((50,50))
        self.green_pepper = Image.open(self.green_pepper)
        self.green_pepper = self.green_pepper.resize((50,50))
        self.onion = Image.open(self.onion)
        self.onion = self.onion.resize((50,50))
        self.banana_pepper = Image.open(self.banana_pepper)
        self.banana_pepper = self.banana_pepper.resize((50,50))


        # Convert the PIL image object to a Tkinter PhotoImage object
        self.pep = ImageTk.PhotoImage(self.pep)
        self.ham = ImageTk.PhotoImage(self.ham)
        self.bacon = ImageTk.PhotoImage(self.bacon)
        self.sausage = ImageTk.PhotoImage(self.sausage)
        self.mushroom = ImageTk.PhotoImage(self.mushroom)
        self.green_pepper = ImageTk.PhotoImage(self.green_pepper)
        self.onion = ImageTk.PhotoImage(self.onion)
        self.banana_pepper = ImageTk.PhotoImage(self.banana_pepper)

        #Topping buttons
        pep_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Pepperoni",variable=pep,onvalue=1,
            offvalue=0,compound="top",bd=0,image=self.pep)
        pep_btn.place(x=175,y=0)
        ham_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Ham",variable=ham,onvalue=1,
            offvalue=0,compound="top",bd=0,image=self.ham)
        ham_btn.place(x=250,y=0)
        bac_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Bacon",variable=bacon,onvalue=1,
            offvalue=0,compound="top",bd=0,image=self.bacon)
        bac_btn.place(x=325,y=0)
        saus_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Sausage",variable=sausage,onvalue=1,
            offvalue=0,compound="top",bd=0,image=self.sausage)
        saus_btn.place(x=400,y=0)
        mush_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Mushroom",variable=mushroom,onvalue=1
            ,offvalue=0,compound="top",bd=0,image=self.mushroom)
        mush_btn.place(x=175,y=75)
        gp_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Green Pepper",variable=green_pepper,
            onvalue=1,offvalue=0,compound="top",bd=0,image=self.green_pepper)
        gp_btn.place(x=250,y=75)
        onion_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Onion",variable=onion,onvalue=1,
            offvalue=0,compound="top",bd=0,image=self.onion)
        onion_btn.place(x=325,y=75)
        bp_btn=tk.Checkbutton(self.piz_frame,bg='blue',text="Banana Pepper",variable=banana_pepper,
            onvalue=1,offvalue=0,compound="top",bd=0,image=self.banana_pepper)
        bp_btn.place(x=400,y=75)

        #Type buttons
        tk.Checkbutton(self.piz_frame,bg='blue', text="Deep Dish", variable=deep_dish, onvalue=1,
            offvalue=0, bd=0, command=self.deep_dish_pizza).place(x=0,y=0)
        tk.Checkbutton(self.piz_frame,bg='blue', text="Round", variable=round, onvalue=1,
            offvalue=0, bd=0, command=self.round_pizza).place(x=0,y=20)
        tk.Checkbutton(self.piz_frame,bg='blue', text="Thin Crust", variable=thin_crust, onvalue=1,
            offvalue=0, bd=0, command=self.thin_crust_pizza).place(x=0,y=40)
        #Sauce buttons
        tk.Checkbutton(self.piz_frame,bg='blue', text="Pizza Sauce", variable=pizza_sauce,onvalue=1,
            offvalue=0, bd=0, command=self.pizza_sauce_pizza).place(x=80,y=0)
        tk.Checkbutton(self.piz_frame,bg='blue',text="Alfredo Sauce",variable=alfredo_sauce,
            onvalue=1,offvalue=0, bd=0, command=self.alferdo_sauce_pizza).place(x=80,y=20)
        tk.Checkbutton(self.piz_frame,bg='blue', text="BBQ Sauce", variable=bbq_sauce, onvalue=1,
            offvalue=0, bd=0, command=self.bbq_sauce_pizza).place(x=80,y=40)
        #Size buttons
        tk.Checkbutton(self.piz_frame,bg='blue', text="Small", variable=small, onvalue=1,
            offvalue=0, bd=0, command=self.small_pizza).place(x=0,y=80)
        tk.Checkbutton(self.piz_frame,bg='blue', text="Medium", variable=medium, onvalue=1,
            offvalue=0, bd=0, command=self.medium_pizza).place(x=0,y=100)
        tk.Checkbutton(self.piz_frame,bg='blue', text="Large", variable=large, onvalue=1,
            offvalue=0, bd=0, command=self.large_pizza).place(x=0,y=120)

    #Type functions
    def deep_dish_pizza(self):
        """Function for the deep dish"""
        #start pizza with size then this, can only be selected when small or large
        if round.get() or thin_crust.get():
            round.set(False)
            thin_crust.set(False)
        if medium.get():
            deep_dish.set(False)
            messagebox.showerror("Round", "Mediums only come round")
    def round_pizza(self):
        """Function for the round"""
        #start pizza with size then this, can only be selected when medium
        if deep_dish.get() or thin_crust.get():
            deep_dish.set(False)
            thin_crust.set(False)
    def thin_crust_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if deep_dish.get() or round.get():
            deep_dish.set(False)
            round.set(False)
        if medium.get():
            thin_crust.set(False)
            messagebox.showerror("Round", "Mediums only come round")

    #sauce functions
    def pizza_sauce_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if alfredo_sauce.get() or bbq_sauce.get():
            alfredo_sauce.set(False)
            bbq_sauce.set(False)
    def alferdo_sauce_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if bbq_sauce.get() or pizza_sauce.get():
            bbq_sauce.set(False)
            pizza_sauce.set(False)
    def bbq_sauce_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if alfredo_sauce.get() or pizza_sauce.get():
            alfredo_sauce.set(False)
            pizza_sauce.set(False)
    #Size functions
    def small_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if medium.get() or large.get():
            medium.set(False)
            large.set(False)
            print("Small")
    def medium_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if small.get() or large.get():
            small.set(False)
            large.set(False)
        if deep_dish.get() or thin_crust.get():
            medium.set(False)
            messagebox.showerror("Round", "Mediums only come round")
    def large_pizza(self):
        """Function for the thin crust"""
        #start pizza with size then this, can only be selected when small or large
        if small.get() or medium.get():
            small.set(False)
            medium.set(False)

    #Order Type functions
    def carryout_fn(self):
        """Function to make carryout only option"""
        if delivery.get() or pick_up.get():
            delivery.set(False)
            pick_up.set(False)
    def pickup_fn(self):
        """Function to make carryout only option"""
        if delivery.get() or carryout.get():
            delivery.set(False)
            carryout.set(False)
    def delivery_fn(self):
        """Function to make carryout only option"""
        if carryout.get() or pick_up.get():
            carryout.set(False)
            pick_up.set(False)

    #Add items to order function
    def add_item_fn(self):
        """Add item to order"""
        global order_box
        if PIZZA_FRAME_VAR:
            #error handling so we have a full pizza
            if not (small.get() or medium.get() or large.get()):
                messagebox.showerror("Size", "No Size found\nPlease add a size")
                return
            if not (deep_dish.get() or round.get() or thin_crust.get()):
                messagebox.showerror("Type", "No type found\nPlease add a type")
                return
            if not (pizza_sauce.get() or alfredo_sauce.get() or bbq_sauce.get()):
                messagebox.showerror("Sauce", "No sauce found\nPlease add a sauce")
                return

            #Adding items to list box
            pizza_list = []
            for i in size:
                if i.get():
                    pizza_list.append(i)
                    i.set(False)
            for i in pizza:
                if i.get():
                    pizza_list.append(i)
                    i.set(False)
            if pizza_list:
                order_box.insert(tk.END, pizza_list)
                #self.order_box.itemconfig(0,weight="bold")
            for i in sauce:
                if i.get():
                    order_box.insert(tk.END,(f"    {i}"))
                    i.set(False)
            for i in toppings:
                if i.get():
                    order_box.insert(tk.END,(f"    {i}"))
                    i.set(False)
        if SIDE_FRAME_VAR:
            side_list = []
            for i in size:
                if i.get():
                    side_list.append(i)
                    i.set(False)
            for i in side:
                if i.get():
                    side_list.append(i)
                    i.set(False)
            if side_list:
                order_box.insert(tk.END, side_list)

    def delete_item_fn(self):
        """Function to delete an item"""
        item = order_box.curselection()
        delete_itm = order_box.index(tk.ACTIVE)
        for i in toppings:
            if str(order_box.get(item)) == (f"    {i}"):
                tk.messagebox.showerror("Pizza not found", "Please delete a whole pizza")
                return
        for i in sauce:
            if str(order_box.get(item)) == (f"    {i}"):
                tk.messagebox.showerror("Pizza not found", "Please delete a whole pizza")
                return
        #Deleting items in reverse, and only deleting one pizza at a time.
        for j in order_box.get(item[0], END):
            if isinstance(j, tuple) and delete_itm != item[0]:
                break
            delete_itm +=1
        while delete_itm > item[0]:
            order_box.delete(delete_itm-1)
            delete_itm -=1

    def submit_order_fn(self):
        """For Submitting orders"""
        global ORDER_NUMBER, CUSTOMER, order_box, employee_name
        #Check if box is empty before sumbiting order
        if order_box.size() == 0:
            messagebox.showerror("Empty", "Order is empty")
            return
        #check if order type is selected
        if not (carryout.get() or pick_up.get() or delivery.get()):
            messagebox.showerror("Order Type", "You need to select an order type")
            return
        if customer_name.get() == "":
            messagebox.showerror("Customer Name", "You need a customer's name")
            return
        if self.write_order_file():
            #Adding to a customer file
            try:
                cus_file = open(os.path.join(__location__, "logs/customer_file.txt"),
                "a", encoding="utf-8")
            except FileNotFoundError:
                messagebox.showerror("File not Found", "File not Found")
                return
            cus_file.write(f"Customer: {customer_phone.get()} ")
            cus_file.write(f"{customer_name.get()} ")
            cus_file.write(f"{customer_address.get()}\n")
            cus_file.close()

            for i in CUSTOMER:
                i.set("")
            #Updating inverntory
            self.inv_update()
            #Clearing info
            order_box.delete(0,END)
            with open(os.path.join(__location__,"logs/employeeslog.txt"),
                mode="a+", encoding="utf-8") as emp_file:
                emp_file.write(f"{employee_name} Submitted order number {ORDER_NUMBER}\n")
                emp_file.close()
            self.controller.show_frame("StartPage")
            employee_name = "No one"
            ORDER_NUMBER +=1

    def inv_update(self):
        """Updating inventory"""
        global order_box
        top_list = []
        #Get current inventory
        try:
            with open(os.path.join(__location__,"logs/Inventory.json"),'r',encoding="utf-8")as file:
                data=json.load(file)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "File not found")
        for i in data["Toppings"]:
            top_list.append(i["Quanity"])
        list = order_box.get(0,END)
        for item in list:
            for index, top in enumerate(toppings):
                if str(top) == str(item).strip():
                    top_list[index] -=1

        for index, item in enumerate(data["Toppings"]):
            try:
                item["Quanity"] = top_list[index]
            except ValueError:
                messagebox.showerror("Failure", "Please Enter an interger")
                return
            if top_list[index] < 5:
                messagebox.showwarning("Low Resources", "Getting low on " + item["Item"])
        with open(os.path.join(__location__, "logs/Inventory.json"),'w',encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def write_order_file(self):
        """Writing order to file"""
        global order_box, employee_name
        #open file
        try:
            file = open(os.path.join(__location__, "logs/Order_File.txt"),
            "a", encoding="utf-8")
        except FileNotFoundError:
            messagebox.showerror("File not Found", "File not Found")
            return
        #write order type to file
        for i in order_type:
            if i.get():
                #Checking for Phone number on Delivery order
                if str(i) == 'Pickup':
                    if customer_phone.get() == "":
                        messagebox.showerror("Phone Error",
                            "Please enter a phone number for the order")
                        return
                    if not self.check_phone(customer_phone.get()):
                        return
                #Checking for phone number for Delivery
                if str(i) == 'Delivery':
                    if customer_phone.get() == "":
                        messagebox.showerror("Phone Error",
                            "Please enter a phone number for the order")
                        return
                    if not self.check_phone(customer_phone.get()):
                        return
                    if customer_address.get() == "":
                        messagebox.showerror("Address Error",
                            "Please enter an addess for the delivery")
                        return
                #write order nubmer to file
                file.write(f"Order Number {ORDER_NUMBER} ")
                file.write(f" {i} ")
                #Writing Customer info to order
                file.write(f"Customer: {customer_phone.get()} ")
                file.write(f"{customer_name.get()} ")
                #Only Write the address for a delivery
                if str(i) == 'Delivery':
                    file.write(f"{customer_address.get()} ")
                i.set(False)
        #Write the order box
        for i in order_box.get(0, END):
            i = str(i).replace('"', '').replace("'", "").replace('(', '').replace(')','')
            file.write(f"{i} ")
        file.write(f"Taken by: {employee_name} ")
        #Add the time of order to file
        file.write(" " + str(datetime.now().strftime("%H:%M:%S")) +"\n")
        file.close()
        #Print Successful
        messagebox.showinfo("Order Submit", "Successful")
        return True

    def check_phone(self, phone):
        """Check if phone is correct format"""
        if re.match(r"\(\d{3}\)\d{3}-\d{4}",phone):
            return True
        messagebox.showerror("Phone Error","The phone number was not the correct format\n\
                Try in the format of (888)555-4545")
        return False

    def exit_fn(self):
        """Function to exit an order"""
        global employee_name
        #Add logging
        with open(os.path.join(__location__,"logs/employeeslog.txt"),
            mode="a+", encoding="utf-8") as emp_file:
            emp_file.write(f"{employee_name} has canceled the order\n")
            emp_file.close()

        #Set frame variable back to false
        global PIZZA_FRAME_VAR, SIDE_FRAME_VAR, order_box
        PIZZA_FRAME_VAR=False
        SIDE_FRAME_VAR=False
        #Set evertyhing back to nothing
        for i in sauce:
            i.set(False)
        for i in pizza:
            i.set(False)
        for i in toppings:
            i.set(False)
        for i in size:
            i.set(False)
        for i in CUSTOMER:
            i.set("")
        order_box.delete(0,END)
        employee_name = "No one"
        self.controller.show_frame("StartPage")

    #Sides Frame
    def side_frame(self):
        """Side Frame for the menu"""
        self.destroy_children(self.piz_frame)
        self.sid_frame.configure(bg='blue',width=640,height=780)
        self.sid_frame.place(x=360,y=30)
        global PIZZA_FRAME_VAR
        global SIDE_FRAME_VAR
        PIZZA_FRAME_VAR=False
        SIDE_FRAME_VAR=True

        #Open Image
        self.breadstick =(os.path.abspath
            (os.path.join(__location__, "assests/breadstick.png")))
        self.breadstick = Image.open(self.breadstick)
        self.breadstick = self.breadstick.resize((50,50))
        self.breadstick = ImageTk.PhotoImage(self.breadstick)

        #Buttons for sides
        #Size buttons
        tk.Checkbutton(self.sid_frame,bg='blue',text="Small", variable=small, onvalue=1,
            offvalue=0, bd=0, command=self.small_pizza).place(x=0,y=00)
        tk.Checkbutton(self.sid_frame,bg='blue',text="Large", variable=large, onvalue=1,
            offvalue=0, bd=0, command=self.large_pizza).place(x=0,y=20)

        pep_btn=tk.Checkbutton(self.sid_frame,bg='blue',text="Breadsticks",variable=breadstick,
            onvalue=1,offvalue=0,compound="top",bd=0,image=self.breadstick)
        pep_btn.place(x=75,y=0)

    def destroy_children(self, frame):
        """Destroy children of a frame"""
        for widget in reversed(frame.winfo_children()):
            widget.destroy()
        frame.place_forget()

class CustomerPage(MenuPage):
    """Class for the customer"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #MenuPage.__init__(self,parent,controller)
        self.controller = controller
        self.configure(background="blue")

        #variables
        global customer_name, customer_phone,customer_address,customer_note
        customer_name =tk.StringVar()
        customer_phone =tk.StringVar()
        customer_address =tk.StringVar()
        customer_note =tk.StringVar()
        global CUSTOMER
        CUSTOMER=[customer_phone,customer_name,customer_address,customer_note]

        #get image link
        self.menu =(os.path.abspath
            (os.path.join(__location__, "assests/menu.png")))
        self.exit =(os.path.abspath(os.path.join(__location__, "assests/exit.png")))
        self.submit_order =(os.path.abspath(os.path.join(__location__, "assests/submit_order.png")))

        # Open image using PIL
        self.menu = Image.open(self.menu)
        self.menu = self.menu.resize((200,200))
        self.exit = Image.open(self.exit)
        self.exit = self.exit.resize((200,200))
        self.submit_order = Image.open(self.submit_order)
        self.submit_order = self.submit_order.resize((200,200))

        # Convert the PIL image object to a Tkinter PhotoImage object
        self.menu = ImageTk.PhotoImage(self.menu)
        self.exit = ImageTk.PhotoImage(self.exit)
        self.submit_order = ImageTk.PhotoImage(self.submit_order)

        #Lables and Entry for getting customer info
        tk.Label(self, bg="blue",text="Customer Phone Number").pack()
        tk.Entry(self, width=20, textvariable=customer_phone).pack()
        tk.Label(self, bg="blue",text="Customer Name").pack()
        tk.Entry(self, width=50, textvariable=customer_name).pack()
        tk.Label(self, bg="blue",text="Customer Address").pack()
        tk.Entry(self, width=50, textvariable=customer_address).pack()
        tk.Label(self, bg="blue",text="Customer Notes").pack()
        tk.Text(self, width=50, height=20).pack()

        tk.Button(self,image=self.menu, text="Menu",compound="top",bg="blue",borderwidth=0,
            command=lambda:controller.show_frame("MenuPage")).place(x=0,y=775)
        tk.Button(self,image=self.submit_order,text="Submit Order",compound="top",bg='blue',
            borderwidth=0,command=self.submit_order_fn).place(x=400,y=775)
        tk.Button(self, image=self.exit,compound="top",bg="blue",borderwidth=0,
            text="Exit", command=lambda: controller.show_frame("StartPage")).place(x=800,y=775)

class ClockPage(CustomerPage):
    """Class for Time Clock page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='blue')

        self.exit =(os.path.abspath(os.path.join(__location__, "assests/exit.png")))
        self.exit = Image.open(self.exit)
        self.exit = self.exit.resize((200,200))
        self.exit = ImageTk.PhotoImage(self.exit)

        tk.Button(self, image=self.exit,compound="top",
            text="Exit", command=lambda: controller.show_frame("StartPage")).place(x=800,y=775)

        #label
        label = Label(self,bg="blue",font=("Arial", 30), text="Enter your 4 digit employee pin")
        label.place(x = 225, y = 375)

        #enter employee number to log in
        global employee_pin
        employee_pin = Entry(self, width=10)
        employee_pin.focus_set()
        employee_pin.place(x = 450, y = 425)

        #start shift button
        start_shift = Button(self, text = "Start shift", command = self.start_shift)
        start_shift.place(x = 400, y = 450)

        #start break button
        start_break = Button(self, text = "Start break", command = self.start_break)
        start_break.place(x = 480, y = 450)

        #end break button
        end_break = Button(self, text = "End break  ", command = self.end_break)
        end_break.place(x = 480, y = 480)

        #end shift button
        end_shift = Button(self, text = "End shift  ", command = self.end_shift)
        end_shift.place(x = 400, y = 480)

    def validate_pin(self):
        """Validating the Pin"""
        n = 0
        global employee_name
        if employee_pin.get() == "":
            messagebox.showerror("Error", "Invalid pin. Please try again.")
            return
        #make sure pin is valid by searching for employee number in employee file
        with open(os.path.join(__location__,"logs/employees.txt"), 'r', encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if employee_pin.get() in line:
                    employee_name = re.split(r'\s+(?=\d)|(?<=\d)\s+', line)[0]
                    n = 1
        employee_pin.delete(0,END)
        #invalid pin error message
        if n != 1:
            messagebox.showerror("Error", "Invalid pin. Please try again.")
            return n
        return n

    # def logged_in(self):
    #     """Function to show you are logged in"""
    #     if self.validate_pin() == 1:
    #         messagebox.showinfo("Login", f"{employee_name} has successfully logged in.")
    #         self.controller.show_frame("StartPage")
    def start_shift(self):
        """Function to start shift"""
        current_time = time.strftime("%H:%M:%S")
        if self.validate_pin() == 1:
            #open and write to file
            file = open(os.path.join(__location__,"logs/employeeslog.txt"), "a+", encoding="utf-8")
            file.write(f"Clocking in: {str(date.today())} ")
            file.write(f"{employee_name} ")
            file.write(f"{str(current_time)}\n")
            file.close()
            messagebox.showinfo("Login", f"{employee_name} has successfully clocked in in.")
            self.controller.show_frame("StartPage")

    def start_break(self):
        """Function to start break"""
        current_time = time.strftime("%H:%M:%S")
        if self.validate_pin() == 1:
            #open and write to file
            file = open(os.path.join(__location__,"logs/employeeslog.txt"), "a", encoding="utf-8")
            file.write("Start break ")
            file.write(f"{employee_name} ")
            file.write(f"{str(current_time)}\n")
            file.close()
            self.controller.show_frame("StartPage")

    def end_break(self):
        """Function to end break"""
        current_time = time.strftime("%H:%M:%S")
        if self.validate_pin() == 1:
            #open and write to file
            file = open(os.path.join(__location__,"logs/employeeslog.txt"), "a", encoding="utf-8")
            file.write("End break ")
            file.write(f"{employee_name} ")
            file.write(f"{str(current_time)}\n")
            file.close()
            self.controller.show_frame("StartPage")

    def end_shift(self):
        """Function to end shift"""
        current_time = time.strftime("%H:%M:%S")
        if self.validate_pin() == 1:
            #open and write to file
            file = open(os.path.join(__location__,"logs/employeeslog.txt"), "a", encoding="utf-8")
            file.write("End shift ")
            file.write(f"{employee_name} ")
            file.write(f"{str(current_time)}\n")
            file.close()
            self.controller.show_frame("StartPage")

class ManagerPage(ClockPage):
    """Class for Time Clock page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="blue")

        self.exit =(os.path.abspath(os.path.join(__location__, "assests/exit.png")))
        self.note =(os.path.abspath(os.path.join(__location__, "assests/note.png")))
        self.update_inv =(os.path.abspath(os.path.join(__location__, "assests/update_inv.png")))
        self.emp_img =(os.path.abspath(os.path.join(__location__, "assests/employee.png")))

        self.exit = Image.open(self.exit)
        self.exit = self.exit.resize((200,200))
        self.note = Image.open(self.note)
        self.note = self.note.resize((200,200))
        self.update_inv = Image.open(self.update_inv)
        self.update_inv = self.update_inv.resize((200,200))
        self.emp_img = Image.open(self.emp_img)
        self.emp_img = self.emp_img.resize((200,200))

        self.exit = ImageTk.PhotoImage(self.exit)
        self.note = ImageTk.PhotoImage(self.note)
        self.update_inv = ImageTk.PhotoImage(self.update_inv)
        self.emp_img = ImageTk.PhotoImage(self.emp_img)

        tk.Button(self,text="Show Inventory",image=self.note,compound='top',bg='blue',borderwidth=0,
            command=self.show_inventory).place(x=150,y=400)
        tk.Button(self, text="Update Inventory",image=self.update_inv,compound='top',bg='blue',
            borderwidth=0,command=self.update_inv_fn).place(x=400,y=400)
        tk.Button(self, text="Show Orders",image=self.note,compound='top',bg='blue',
            borderwidth=0,command=self.show_order_fn).place(x=250,y=100)
        tk.Button(self, text="Show Customer",image=self.emp_img,compound='top',bg='blue',
            borderwidth=0,command=self.show_customer_fn).place(x=550,y=100)
        tk.Button(self, text="Employee Logs",image=self.emp_img,compound='top',bg='blue',
            borderwidth=0,command=self.employee_log_fn).place(x=650,y=400)
        tk.Button(self, text="Exit",image=self.exit,compound='top',bg='blue',borderwidth=0,
            command=lambda:controller.show_frame("StartPage")).place(x=800,y=775)
    def employee_log_fn(self):
        """Showing Employee logs"""
        try:
            with open(os.path.join(__location__,"logs/employeeslog.txt"),
                'r',encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "File not found")
         #Create new window to show order
        emp_win = tk.Toplevel()
        emp_win.title("Show Order")
        emp_win.geometry("1000x1000")
        emp_win.configure(background = "blue")

        #Creating scrollbar and listbox to add order to
        scrollbar=tk.Scrollbar(emp_win,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y,pady=25)
        list_box=tk.Listbox(emp_win,background="blue",yscrollcommand=scrollbar.set,
            borderwidth=0,highlightthickness=0)
        for line in lines:
            list_box.insert(END,line)
        file.close()
        list_box.pack(side=LEFT,fill=BOTH,expand=TRUE)
        scrollbar.config(command=list_box.yview)

        #Quit button
        tk.Button(emp_win,bg="red",text="Quit",command=emp_win.destroy).place(x=967,y=975)

    def show_customer_fn(self):
        """Showing customer info"""
        try:
            with open(os.path.join(__location__,"logs/customer_file.txt"),
            'r',encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "File not found")
            return
        #Create new window to show order
        inv_win = tk.Toplevel()
        inv_win.title("Show Order")
        inv_win.geometry("1000x1000")
        inv_win.configure(background = "blue")

        #Creating scrollbar and listbox to add order to
        scrollbar=tk.Scrollbar(inv_win,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y,pady=25)
        list_box=tk.Listbox(inv_win,background="blue",yscrollcommand=scrollbar.set,
            borderwidth=0,highlightthickness=0)
        for line in lines:
            list_box.insert(END,line)
        file.close()
        list_box.pack(side=LEFT,fill=BOTH,expand=TRUE)
        scrollbar.config(command=list_box.yview)

        #Quit button
        tk.Button(inv_win,bg="red",text="Quit",command=inv_win.destroy).place(x=967,y=975)

    def show_order_fn(self):
        """Show Orders to the managers"""
        try:
            with open(os.path.join(__location__,"logs/Order_File.txt"),'r',encoding="utf-8")as file:
                lines = file.readlines()
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "File not found")
        #Create new window to show order
        inv_win = tk.Toplevel()
        inv_win.title("Show Order")
        inv_win.geometry("1000x1000")
        inv_win.configure(background = "blue")

        #Creating scrollbar and listbox to add order to
        scrollbar=tk.Scrollbar(inv_win,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y,pady=25)
        list_box=tk.Listbox(inv_win,background="blue",yscrollcommand=scrollbar.set,
            borderwidth=0,highlightthickness=0)
        for line in lines:
            list_box.insert(END,line)
        file.close()
        list_box.pack(side=LEFT,fill=BOTH,expand=TRUE)
        scrollbar.config(command=list_box.yview)

        #Quit button
        tk.Button(inv_win,bg="red",text="Quit",command=inv_win.destroy).place(x=967,y=975)

    def show_inventory(self):
        """Show Inventory"""
        try:
            with open(os.path.join(__location__,"logs/Inventory.json"),'r',encoding="utf-8")as file:
                data=json.load(file)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "File not found")
        inv_win = tk.Toplevel()
        inv_win.title("Show Inventory")
        inv_win.geometry("400x400")
        inv_win.configure(background = "blue")
        for i in data["Toppings"]:
            tk.Label(inv_win, text=(i["Item"] + f"\t\tQuanity: "+ str(i["Quanity"])),
                background="blue").pack()
        file.close()
        inv_win.update()
        tk.Button(inv_win,bg="red",text="Quit",
            command=inv_win.destroy).place(x=inv_win.winfo_width()-35,y=inv_win.winfo_height()-25)

    def update_inv_fn(self):
        """Function to update inventory"""
        upt_inv_win = tk.Toplevel()
        upt_inv_win.title("Update Inventory")
        upt_inv_win.geometry("400x400")
        upt_inv_win.configure(background = "blue")

        #Variables for updating inventory
        global pep_inv,ham_inv,bacon_inv,sausage_inv,mush_inv,gp_inv,onion_inv,bp_inv
        pep_inv = tk.StringVar()
        ham_inv = tk.StringVar()
        bacon_inv =tk.StringVar()
        sausage_inv = tk.StringVar()
        mush_inv = tk.StringVar()
        bacon_inv =tk.StringVar()
        gp_inv = tk.StringVar()
        onion_inv = tk.StringVar()
        bp_inv = tk.StringVar()
        self.inv_list =[pep_inv,ham_inv,bacon_inv,sausage_inv,mush_inv,gp_inv,onion_inv,bp_inv]

        tk.Label(upt_inv_win, text="Pepporini Quanity",bg='blue').grid(column=0,row=0)
        tk.Entry(upt_inv_win, textvariable=pep_inv).grid(column=1, row=0)
        tk.Label(upt_inv_win, text="Ham Quanity",bg='blue').grid(column=0, row=1)
        tk.Entry(upt_inv_win, textvariable=ham_inv).grid(column=1, row=1)
        tk.Label(upt_inv_win, text="Bacon Quanity",bg='blue').grid(column=0, row=2)
        tk.Entry(upt_inv_win, textvariable=bacon_inv).grid(column=1, row=2)
        tk.Label(upt_inv_win, text="Sausage Quanity",bg='blue').grid(column=0, row=3)
        tk.Entry(upt_inv_win, textvariable=sausage_inv).grid(column=1, row=3)
        tk.Label(upt_inv_win, text="Mushroom Quanity",bg='blue').grid(column=0, row=4)
        tk.Entry(upt_inv_win, textvariable=mush_inv).grid(column=1, row=4)
        tk.Label(upt_inv_win, text="Green Pepper Quanity",bg='blue').grid(column=0, row=5)
        tk.Entry(upt_inv_win, textvariable=gp_inv).grid(column=1, row=5)
        tk.Label(upt_inv_win, text="Onion Quanity",bg='blue').grid(column=0, row=6)
        tk.Entry(upt_inv_win, textvariable=onion_inv).grid(column=1, row=6)
        tk.Label(upt_inv_win, text="Banana Pepper Quanity",bg='blue').grid(column=0, row=7)
        tk.Entry(upt_inv_win, textvariable=bp_inv).grid(column=1, row=7)


        tk.Button(upt_inv_win, text="Submit",font=24,width=10,
            command=lambda: self.destory_window(upt_inv_win)).grid(column=1,row=10)
        tk.Button(upt_inv_win,text="Quit",bg='red',
            command=upt_inv_win.destroy).place(x=366,y=400,anchor=SW)

    def update_json(self):
        """Updating json"""
        with open(os.path.join(__location__,"logs/Inventory.json"),'r',encoding='utf-8') as file:
            data=json.load(file)
        i = 0
        for item in data["Toppings"]:
            if self.inv_list[i].get() != "":
                try:
                    item["Quanity"] = int(self.inv_list[i].get())
                except ValueError:
                    messagebox.showerror("Failure", "Please Enter an interger")
                    return
            self.inv_list[i].set("")
            i +=1
        with open(os.path.join(__location__, "logs/Inventory.json"),'w',encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Successful", "You have successful update the invetory")

    def destory_window(self,window):
        """Function to destroy window"""
        self.update_json()
        window.destroy()

def main():
    """Main function for the program"""
    app = PizzaApp()
    app.mainloop()

if __name__ == "__main__":
    main()

#Group Project 2
#Matthew Krol END version 5, END 4/2/23
