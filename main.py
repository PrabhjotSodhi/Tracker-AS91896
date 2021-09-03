"""
Application Program for AS91896 Internal
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from window import Root
import csv

def validate_input(tree, data, error_labels):
    """
    Handles all input from user into treeview,
    also saves treeview into data.csv file.
    """
    validation = {'fail_0': False, 'fail_1': False, 'fail_2': False, 'fail_3': False}
    # Customer Name Validation
    try:
        if data[0].get().isalpha() and len(data[0].get()) > 2:
            error_labels[0].config(text="")
        else:
            raise TypeError
    except TypeError:
        error_labels[0].config(text="Please Enter Valid Name")
        validation['fail_0'] = True
    # Receipt Number Validation
    try:
        int(data[1].get())
        error_labels[1].config(text="")
    except ValueError:
        error_labels[1].config(text="Please Enter Valid Number")
        validation['fail_1'] = True
    # Item Name Validation
    try:
        if data[2].get().isalpha() and len(data[2].get()) > 2:
            error_labels[2].config(text="")
        else:
            raise TypeError
    except TypeError:
        error_labels[2].config(text="Please Enter Valid Item Name")
        validation['fail_2'] = True
    # Quantity Item Validation
    try:
        int(data[3].get())
        if 1 <= int(data[3].get()) <= 500:
            error_labels[3].config(text="")
        else:
            raise ValueError
    except ValueError:
        error_labels[3].config(text="Please Enter Valid Quantity")
        validation['fail_3'] = True
    # Conditions met then save to file and import into tree
    if all(value == False for value in validation.values()):
        tree.insert(parent='', index='end', text='', values=(data[0].get(),data[1].get(),data[2].get(),data[3].get()))
        add_to_file(tree)

def create_file():
    """
    Creates file if it already exists
    then override it and changes state.
    """
    open("data.csv", "w").close()
    window.change_state(states, 'APP')

def add_to_file(tree):
    """
    Gets items in tree and appends to csv file
    """
    with open("data.csv", "w", newline='') as data_file:
        write_file = csv.writer(data_file, delimiter=",")
        for row_id in tree.get_children():
            row = tree.item(row_id)['values']
            print('save row:',row)
            write_file.writerow(row)

def load_file():
    """
    Handles loading data.csv file and
    inputing into tree
    """
    window.change_state(states, 'APP')
    with open("data.csv") as data_file:
        read_file = csv.reader(data_file, delimiter=",")
        for row in read_file:
            print('Load row:', row)
            tree.insert("", 'end', values=row)

def menu(frame):
    """
    State Menu, menu screen for user
    to either create new or load data
    """
    root.geometry('300x400')
    root.title("Julie's Party Tracker - AS91896")
    tk.Label(frame, text="Julie's Party Tracker").pack()
    tk.Button(frame, text='Create New Party Tracker', command=lambda: create_file()).pack()
    tk.Button(frame, text='Load Party Tracker from file', command=lambda: load_file()).pack()

def app(frame):
    """
    State app, actual application and most
    used state from the user
    """
    global tree
    root.geometry('800x600')
    root.title("Julie's Party Tracker - Application")
	# Customer Input Box
    tk.Label(frame, text='Customer Name').grid(row=0, column=0, pady=2, sticky='w')
    customer_name = tk.Entry(frame)
    customer_name.grid(row=1, column=0, padx=(0,10))
    error_customer_name = tk.Label(frame, text='')
    error_customer_name.grid(row=2, column=0, pady=2, sticky='w')

	# Receipt Input Box
    tk.Label(frame, text='Receipt #').grid(row=0, column=1, pady=2, sticky='w')
    receipt_number = tk.Entry(frame, width=10)
    receipt_number.grid(row=1, column=1, padx=(0,5))
    error_receipt_number = tk.Label(frame, text='')
    error_receipt_number.grid(row=2, column=1, pady=2, sticky='w')

	# Item Name Input Box
    tk.Label(frame, text='Item Name').grid(row=0, column=2, pady=2, sticky='w')
    item_name = tk.Entry(frame)
    item_name.grid(row=1, column=2, padx=(0,5))
    error_item_name = tk.Label(frame, text='')
    error_item_name.grid(row=2, column=2, pady=2, sticky='w')

	# Item Qty Input Box
    tk.Label(frame, text='Item Qty').grid(row=0, column=3, pady=2, sticky='w')
    quantity_item = tk.Entry(frame, width=10)
    quantity_item.grid(row=1, column=3, padx=(0,5))
    error_quanity_item = tk.Label(frame, text='')
    error_quanity_item.grid(row=2, column=3, pady=2, sticky='w')

    data = [customer_name, receipt_number, item_name, quantity_item]
    error_labels = [error_customer_name, error_receipt_number, error_item_name, error_quanity_item]
	# Submit Data
    tk.Button(frame, width=20, text='Submit Data', command=lambda: validate_input(tree, data, error_labels)).grid(column=4, row=1)

	# Create the Treview
    tree_frame = Frame(frame)
    tree_scroll = Scrollbar(tree_frame)
    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
	# Handle all columns
    tree['columns'] = ('Name','Receipt','Item Name','Item Qty')
    tree.column("#0", width=0, minwidth=0)
    tree.column("Name", anchor=W, width=220)
    tree.column("Receipt", anchor=W, width=160)
    tree.column("Item Name", anchor=W, width=220)
    tree.column("Item Qty", anchor=W, width=160)
	# Create headings corresponding to colums
    tree.heading("#0", text='', anchor=W)
    tree.heading("Name", text="Name", anchor=W)
    tree.heading("Receipt", text="ID", anchor=W)
    tree.heading("Item Name", text="Item Name", anchor=W)
    tree.heading("Item Qty", text="Item Qty", anchor=W)
	# Show Treview
    tree_scroll.configure(command=tree.yview)
    tree_frame.grid(pady=10, padx=10, columnspan=6, column=0, row=3)
    tree_scroll.grid(row=0, column=1, sticky="nesw")
    tree.grid(row=0, sticky="ew")

    # Screen min width size of tree
    frame.update()
    root.minsize(frame.winfo_width(), frame.winfo_height())

    # Buttons for modifying tree and returning to menu
    modify_tree_frame = Frame(frame)
    modify_tree_frame.grid()
    tk.Button(modify_tree_frame, width=20, text='Return Item', command=lambda: tree.delete(tree.selection()[0])).pack()
    tk.Button(modify_tree_frame, width=20, text='Return to Menu', command=lambda: window.change_state(states, 'MENU', tree_frame)).pack()

if __name__ == '__main__':
    """
    Checks to make sure user is running program
    from this file
    """
    root = Tk()
    states = {"MENU": menu, "APP": app} # State Dictionary
    window = Root(root)
    window.change_state(states, 'MENU')
    root.mainloop()