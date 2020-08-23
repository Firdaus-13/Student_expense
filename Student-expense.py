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
        
         # Define the different GUI widgets
        self.Amount_label = tk.Label(self.root, text="Amount (RM) :")
        self.Amount_entry = tk.Entry(self.root)
        self.Amount_label.grid(row=0, column= 0 ,sticky = tk.W)
        self.Amount_entry.grid(row=0, column=1,sticky = tk.W)
 
        self.Description_label = tk.Label(self.root, text="Description     :")
        self.Description_entry = tk.Entry(self.root)
        self.Description_label.grid(row=1, column=0 ,sticky = tk.W)
        self.Description_entry.grid(row=1, column=1,sticky = tk.W)
        
        self.Date_label = tk.Label(self.root, text="Date                 :")
        self.Date_entry = tk.Entry(self.root)
        self.Date_label.grid(row=2, column= 0, sticky = tk.W)
        self.Date_entry.grid(row=2, column=1,sticky = tk.W)
        
        

app = Application(tk.Tk())
app.root.mainloop()