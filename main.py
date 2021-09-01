from tkinter import *
import tkinter as tk
from tkinter import ttk
from window import Root

"""
Assessment Task To-Do List
    v 0.2
    - Create Input Field and button to submit text from the user
    v 0.5
    - On submit data should be formatted and placed into a table
    - Data should be stored in either lists, arrays or dictionaries
    - Create two buttons of return 1 item and return all items.
    v 0.9
    - Upon completion of the program test and create boundary rules for data
    v 1.0
    - BONUS: Save the data in a file and read and write from it
"""

def menu(frame):
        root.geometry('300x400')
        root.title("Julie's Party Tracker - AS91896")

        tk.Label(frame, text="Julie's Party Tracker").pack()
        tk.Button(frame, text='Create New Party Tracker', command=lambda: window.change_state(states, 'APP')).pack()
        tk.Button(frame, text='Load Party Tracker from file', command=lambda: window.change_state(states, 'APP')).pack()
def app(frame):
        root.geometry('800x600')
        root.title("Julie's Party Tracker - Application")

        # Customer Input Box
        tk.Label(frame, text='Customer Name').grid(row=0, column=0, pady=2, sticky='w')
        customer_name = tk.Entry(frame)
        customer_name.grid(row=1, column=0, padx=(0,10))

        # Receipt Input Box
        tk.Label(frame, text='Receipt #').grid(row=0, column=1, pady=2, sticky='w')
        receipt_number = tk.Entry(frame, width=10)
        receipt_number.grid(row=1, column=1, padx=(0,5))

        # Item Name Input Box
        tk.Label(frame, text='Item Name').grid(row=0, column=2, pady=2, sticky='w')
        item_name = tk.Entry(frame)
        item_name.grid(row=1, column=2, padx=(0,5))

        # Item Qty Input Box
        tk.Label(frame, text='Item Qty').grid(row=0, column=3, pady=2, sticky='w')
        quantity_item = tk.Entry(frame, width=10)
        quantity_item.grid(row=1, column=3, padx=(0,5))

        # Submit Data
        tk.Button(frame, width=20, text='Submit Data', command=lambda: tree.insert(parent='', index='end', text='', values=(customer_name.get(), receipt_number.get(), item_name.get(), quantity_item.get()))).grid(column=4, row=1)

        # Create the Treview
        tree_frame = Frame(frame, background='green')
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
        # Insert Data
        tree.insert(parent='', index='end', iid=0, text='', values=("John", 256, "Table", 256))
        # Show Treview
        tree_scroll.configure(command=tree.yview)
        tree_frame.grid(pady=10, padx=10, columnspan=6, column=0, row=3)
        tree_scroll.grid(row=0, column=1, sticky="nesw")
        tree.grid(row=0, sticky="ew")

        frame.update()
        root.minsize(frame.winfo_width(), frame.winfo_height())

        modify_tree_frame = Frame(frame, background='red')
        modify_tree_frame.grid()
        tk.Button(modify_tree_frame, width=20, text='Return to Menu', command=lambda: window.change_state(states, 'MENU', tree_frame)).pack()

if __name__ == '__main__':
    root = Tk()
    states = {"MENU": menu, "APP": app}
    window = Root(root)
    window.change_state(states, 'MENU')
    root.mainloop()