from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox


class Application(tk.Frame):
   
    #building windows
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.root.title("Student Expense Tracker")   #Title on the windows bar
        self.root.grid_rowconfigure(0, weight=1)     #grid for row
        self.root.grid_columnconfigure(0, weight=1)  #grid for column
        self.root.config(background="yellow")        #windows background
        
        #Define the different GUI widgets
        #TITLE
        self.label = tk.Label(self.root,text = "Student Expense Tracker")
        self.label.grid(row=0, column= 0)

        self.label = tk.Label(self.root,text = "Records of Student Expense ")
        self.label.grid(row=6, column= 0,sticky = tk.W)

        #showing it onto screen
        #label and entry for amount
        self.Amount_label = tk.Label(self.root, text="Amount (RM) :")
        self.Amount_entry = tk.Entry(self.root)
        #label and entry grid for amount
        self.Amount_label.grid(row=1, column= 0, sticky = tk.W) #tk.W=Stick to left, tk.E=Stick to right
        self.Amount_entry.grid(row=1, column=1, sticky = tk.W)
        
        #label and entry for Description
        self.Description_label = tk.Label(self.root, text="Description     :")
        self.Description_entry = tk.Entry(self.root)
        #label and entry grid for Description
        self.Description_label.grid(row=2, column=0 ,sticky = tk.W)
        self.Description_entry.grid(row=2, column=1,sticky = tk.W)
        
        #label and entry for Date
        self.Date_label = tk.Label(self.root, text="Date                 :")
        self.Date_entry = tk.Entry(self.root)
        #label and entry grid for Date
        self.Date_label.grid(row=3, column= 0, sticky = tk.W)
        self.Date_entry.grid(row=3, column=1,sticky = tk.W)
        
        #create widget for buttons
        
        #Exit button and its grid
        self.submit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.submit_button.grid(row=4, column=1, sticky = tk.W)
        
        #Total button and its grid
        self.total_button = tk.Button(self.root, text="Total", command=self.total_data)
        self.total_button.grid(row=4, column=2, sticky = tk.W)
        
        #Delete button and its grid
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=10, column=2, sticky = tk.W)
        
        #Total Expense button and its grid       
        self.label = tk.Label(self.root, text="Total Expense")
        self.label.grid(row=10, column= 1, sticky = tk.E)
        
        #Insert button and its grid
        self.exit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.exit_button.grid(row=4, column=0, sticky = tk.E)    
        
        #building treeview widget
        self.tree = ttk.Treeview(self.root, columns=('Amount(RM)','Description','Date'))
        
        #heading for column
        self.tree.heading('#0', text='No.')
        self.tree.heading('#1', text='Date')
        self.tree.heading('#2', text='Amount (RM)')
        self.tree.heading('#3', text='Description')
        
        #enable function to stretch the table
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        
        #treeview starting row and column span
        self.tree.grid(row=7, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        
        #counter for "No. " column
        self.id = 1
        self.iid = 1
             
    #function for total button (total for all amount)
    def total_data(self):
        sum1 = 0.0
        for x in self.treeview.get_children():
            sum1 += float(self.treeview.item(x, "values")[1])
            self.label.config(text=sum1)
        tkinter.messagebox.showinfo("Success", "Expenses calculated.")
    
    #function for sort    
    def treeview_sort_column(self, col, reverse):
            l = [(treeview.item(k)["text"], k) for k in treeview.get_children()] #Display column #0 cannot be set
            l.sort(key=lambda t: t[0], reverse=reverse)

            for index, (val, k) in enumerate(l):
                move(k, '', index)

            self.heading(col, command=lambda: treeview_sort_column(self, col, not reverse))     
        
            self.tree.heading("#0", command=lambda : treeview_sort_column(tree, "#0", False))

    #function for insert button
    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="" + str(self.id),
                             values=( self.Date_entry.get(),
                                     self.Amount_entry.get(),
                                     self.Description_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1
    
    #function for delete button
    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)    
     
    
        
app = Application(tk.Tk())
#infinite loop for window stays in view
app.root.mainloop()