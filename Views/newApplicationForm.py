from tkinter import *
from tkinter import ttk
from BusinessLogic.CRUD import CRUD

# Main window
class NewApplicationGui:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Job Tracker")

        self.create_widgets()


    def create_widgets(self):

        container = LabelFrame(self.master, text="Job Tracker")
        container.pack(side="top", fill="both", expand=True)

        #company name and label creation
        company_label = Label(container, text="Company Name", font=("Arial", 8))
        company_label.grid(row=0, column=0, padx=10, pady=3, sticky=W)

        self.company_name = StringVar()
        self.company_entry = Entry(container, textvariable=self.company_name)
        self.company_entry.grid(row=1, column=0, ipady=5,  padx=10, sticky='we')

        #Role and role entry creation
        role_label = Label(container, text="Role", font=("Arial", 8))
        role_label.grid(row=0, column=1, sticky=W, pady=3, padx=10)

        self.role = StringVar()
        self.role_entry = Entry(container, textvariable=self.role)
        self.role_entry.grid(row=1, column=1, ipady = 5, sticky='we', padx=10)

        #Date applied label and entry creation
        date_label = Label(container, text="Date", font=("Arial", 8))
        date_label.grid(row=2, column=0, sticky=W, padx=10)

        self.date = StringVar()
        self.date_entry = Entry(container, textvariable=self.date)
        self.date_entry.grid(row = 3,column=0, ipady= 5, padx=10, sticky='we')

        # Status label and dropdown menue creation

        status_label = Label(container, text="Status", font=("Arial", 8))
        status_label.grid(row=2, column=1, sticky=W, pady=3, padx=10)

        self.status = StringVar()
        options = ['Applied', 'Interview', 'Rejected', 'Offer']
        status_dropdown = ttk.Combobox(container, values=options, textvariable=self.status)
        status_dropdown.current(0)
        status_dropdown.grid(row=3, column=1, ipady=5, padx=10, sticky='we')

        #notes label and entry creation
        notes_label = Label(container, text="Notes", font=("Arial", 8))
        notes_label.grid(row=4, column=0, sticky=W, padx=10)
        self.notes = StringVar()
        self.notes_entry = Entry(container, textvariable=self.notes)
        self.notes_entry.grid(row=5, column=0, columnspan=2, sticky='we', ipady=30, padx=10)

        #Save and cancel button creation
        buttons_frame = Frame(container)
        buttons_frame.grid(column=1, row = 6, pady=10)

        #cancel button
        self.cancel_button = Button(buttons_frame, text='Cancel', width=7, bg='red', fg='white', command=self.master.destroy)
        self.cancel_button.grid(row = 0, column=0, padx = 10)

        #Save button
        self.save_button = Button(buttons_frame, text='Save', width=7, bg='blue', fg='white', command=self.add_application)
        self.save_button.grid(row = 0, column=1)

    def add_application(self):
        CRUD().add_application(self)