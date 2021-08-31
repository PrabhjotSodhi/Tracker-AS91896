import tkinter as tk

class Root(object):
    """
    A single instance of this class is responsible for 
    managing which individual window state is active
    and keeping it updated.
    """
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x300')
        self.master.title("Julie's Party Tracker - AS91896")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
    def change_state(self, states, state_to):
        self.frame.destroy()
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        states[state_to](self.frame)
