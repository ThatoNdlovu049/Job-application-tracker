from tkinter import *
from tkinter import ttk, messagebox
from BusinessLogic.CRUD import CRUD
from Views.updateApplicationForm import ApplicationGui
from Views.newApplicationForm import NewApplicationGui

class Applications:
    def __init__(self, master):
        self.master = master
        self.master.geometry('650x450')
        self.master.title('Applications')

        self.create()

    def create(self):

        #dashboard and applications button frame
        buttons_frame = Frame(self.master)
        buttons_frame.grid(row = 0, column=0, pady=20)

        #dashboard button
        self.dashboard_button = ttk.Button(buttons_frame, text='Dashboard', width=20, command=self.redirect_to_dashboard)
        self.dashboard_button.grid(row=0, column=0, ipady=5, padx = 10)

        #Application button
        self.applications_button = ttk.Button(buttons_frame, text='Applications', width=20, state='disabled')
        self.applications_button.grid(row=0, column=1, ipady=5)

        #search, filter and reload button section
        search_frame = Frame(self.master)
        search_frame.grid(row = 1, column=0, columnspan=6, pady=20)

        #search label and button
        search_label = Label(search_frame, text='Search')
        search_label.grid(row=0, column=0, padx=10)

        self.search_value = StringVar()
        search_entry = Entry(search_frame, textvariable=self.search_value)
        search_entry.grid(row=0, column=1, ipady=3, sticky='we')

        #filter applications
        filter_label = Label(search_frame, text='Status')
        filter_label.grid(row=0, column=2, padx=10)

        self.status = StringVar()
        options = ['Applied', 'Interview', 'Rejected', 'Offer']
        filter_dropdown = ttk.Combobox(search_frame, values=options, textvariable=self.status)
        filter_dropdown.grid(row=0, column=3, ipady=3, sticky='we')

        #Search and filter buttons
        self.search_button = ttk.Button(search_frame, text='Search', width=15, command=self.search)
        self.search_button.grid(row=0, column=4, padx=10)

        self.filter_button = ttk.Button(search_frame, text='Filter', width=15, command=self.filter)
        self.filter_button.grid(row=0, column=5)

        #setting up treeview for applications
        self.treeview = ttk.Treeview(self.master, columns=('#', 'Company', 'Role', 'Date applied', 'Status', 'Notes'), show='headings')
        self.treeview.heading('#', text='#')
        self.treeview.heading('Company', text='Company')
        self.treeview.heading('Role', text='Role')
        self.treeview.heading('Date applied', text='Date applied')
        self.treeview.heading('Status', text='Status')
        self.treeview.heading('Notes', text='Notes')

        self.treeview.column('#', width=30)
        self.treeview.column('Company', width=150)
        self.treeview.column('Role', width=150)
        self.treeview.column('Date applied', width=110)
        self.treeview.column('Status', width=90)
        self.treeview.column('Notes', width=90)

        self.treeview.grid(row = 2, column=0, columnspan=6, padx=10)

        #binding treeview with on_select function
        self.treeview.bind('<<TreeviewSelect>>', self.on_select)

        #add,edit, delete, clear buttons

        crud_frame = Frame(self.master)
        crud_frame.grid(row = 3, column=0, pady=10, columnspan=6)

        #add button
        add_button = ttk.Button(crud_frame, text='Add new', width=15, command=self.redirect_to_new_form)
        add_button.grid(row=0, column=0, ipady=5, padx=3)

        #edit button
        edit_button = ttk.Button(crud_frame, text='Edit Selection', width=15, command=self.redirect_to_edit_form)
        edit_button.grid(row=0, column=1, ipady=5, padx=3)

        #delete
        delete_button = ttk.Button(crud_frame, text='Delete Selection', width=15, command=self.delete_application)
        delete_button.grid(row=0, column=2, ipady=5, padx=3)

        #reload button
        reload_button = ttk.Button(crud_frame, text='Reload table', width=15, command=self.populate_treeview)
        reload_button.grid(row=0, column=3, ipady=5, padx=3)

        #instructions label
        instructions_label = Label(crud_frame, text='Select a row first then Edit or Delete')
        instructions_label.grid(row=0, column=4, padx=8)

    #buttons functionality
    def populate_treeview(self):
        CRUD().read_all_applications(self)

    def redirect_to_new_form(self):
        root = Toplevel(self.master)
        app = NewApplicationGui(root)

    def search(self):
        CRUD().search_application(self)

    def filter(self):
        CRUD().filter(self)

    def on_select(self, event):
        selected = self.treeview.focus()
        self.row = self.treeview.item(selected, 'values')

    def open_edit(self):
        top = Toplevel(self.master)
        edit = ApplicationGui(top, self)

    def delete_application(self):
        if not hasattr(self, 'row') or not self.row:
            messagebox.showwarning('Warning', 'Please select a row first')
            return
        CRUD().delete_application(self,self.row[0])

    def redirect_to_edit_form(self):
        if not hasattr(self, 'row') or not self.row:
            messagebox.showwarning('Warning', 'Please select a row first')
            return
        root = Toplevel(self.master)
        app = ApplicationGui(root, self)

    def redirect_to_dashboard(self):
        self.master.destroy()



'''root = Tk()
app = Applications(root)
Applications.populate_treeview(app)
root.mainloop()'''