from tkinter import *
import tkinter as tk
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

# Variables
customer_name = ''
receipt_number = 0
item_name = ''
quantity_item = 0

def menu(frame):
        tk.Label(frame, text="Julie's Party Tracker").pack()
        tk.Button(frame, text='Create New Party Tracker', command=lambda: window.change_state(states, 'APP')).pack()
        tk.Button(frame, text='Load Party Tracker from file', command=lambda: window.change_state(states, 'APP')).pack()
def app(frame):
        tk.Label(frame, text='App').pack()
        tk.Button(frame, text='Goto A', command=lambda: window.change_state(states, 'MENU')).pack()

if __name__ == '__main__':
    root = Tk()
    states = {"MENU": menu, "APP": app}
    window = Root(root)
    window.change_state(states, 'MENU')
    root.mainloop()