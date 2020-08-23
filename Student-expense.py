from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox


class Application(tk.Frame):
   
   
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()


app = Application(tk.Tk())
app.root.mainloop()