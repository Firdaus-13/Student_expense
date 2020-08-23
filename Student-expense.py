from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox


class Application(tk.Frame):
   
   
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.root.title("Student Expense Tracker")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="white")
        
        

app = Application(tk.Tk())
app.root.mainloop()