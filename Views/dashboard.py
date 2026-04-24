from tkinter import *
from tkinter import ttk
from Views.Applications import ApplicationGui, Applications


class Dashboard:
    def __init__(self, master, applications, interviews, offers, rejected, interview_rate):
        self.master = master
        self.master.title('Dashboard')
        self.master.geometry('600x300')

        self.applications = applications
        self.interviews = interviews
        self.offers = offers
        self.rejected = rejected
        self.interview_rate = interview_rate

        self.create_dashboard()


    def create_dashboard(self):

        self.master.columnconfigure(0, weight=1)
        # dashboard and applications button frame
        buttons_frame = Frame(self.master)
        buttons_frame.grid(row=0, column=0, pady=20, columnspan=4)

        # dashboard button
        self.dashboard_button = ttk.Button(buttons_frame, text='Dashboard', width=20, state='disabled')
        self.dashboard_button.grid(row=0, column=0, ipady=5, padx=10)

        # Application button
        self.applications_button = ttk.Button(buttons_frame, text='Applications', width=20, command=self.import_applications)
        self.applications_button.grid(row=0, column=1, ipady=5)

        #dashboard ratios for each status category
        ratios_frame = Frame(self.master)
        ratios_frame.grid(row=1, column=0, sticky='we', padx=10, pady=10)
        #configure columns to fill form
        ratios_frame.columnconfigure(0, weight=1)
        ratios_frame.columnconfigure(1, weight=1)
        ratios_frame.columnconfigure(2, weight=1)
        ratios_frame.columnconfigure(3, weight=1)

        #number of applications section
        applied_frame = LabelFrame(ratios_frame, bg='white')
        applied_frame.grid(row=0, column=0, ipady=10, ipadx=20, sticky='we', padx=10)
        applied_frame.columnconfigure(0, weight=1)

        #self.number_of_applications = StringVar() will use later
        applied_number = Label(applied_frame, text=self.applications,bg='white', anchor='center', font=('Arial', 15))
        applied_number.grid(row=0, column=0, sticky='ew')

        applied_label = Label(applied_frame, text='applied', bg='white', anchor='center')
        applied_label.grid(row=1, column=0, sticky='ew')

        #number of interviews section
        interview_frame = LabelFrame(ratios_frame, bg='white')
        interview_frame.grid(row=0, column=1, ipady=10, ipadx=20,sticky='we', padx=10)
        interview_frame.columnconfigure(0, weight=1)

        # self.number_of_interviews = StringVar() will use later
        applied_number = Label(interview_frame, text=self.interviews, bg='white', anchor='center', font=('Arial', 15))
        applied_number.grid(row=0, column=0, sticky='ew')
        applied_label = Label(interview_frame, text='Interviews', bg='white', anchor='center')
        applied_label.grid(row=1, column=0, sticky='ew')

        #Offers section
        offers_frame = LabelFrame(ratios_frame, bg='white')
        offers_frame.grid(row=0, column=2, ipady=10, ipadx=20, sticky='we', padx=10)
        offers_frame.columnconfigure(0, weight=1)

        # self.number_of_interviews = StringVar() will use later
        offers_number = Label(offers_frame, text=self.offers, bg='white', anchor='center', font=('Arial', 15))
        offers_number.grid(row=0, column=0, sticky='ew')
        offers_label = Label(offers_frame, text='Offers', bg='white', anchor='center')
        offers_label.grid(row=1, column=0, sticky='ew')

        #Rejected applications
        rejected_frame = LabelFrame(ratios_frame, bg='white')
        rejected_frame.grid(row=0, column=3, ipady=10, ipadx=20, sticky='we', padx=10)
        rejected_frame.columnconfigure(0, weight=1)

        rejected_number = Label(rejected_frame, text=self.rejected, bg='white', anchor='center', font=('Arial', 15))
        rejected_number.grid(row=0, column=0, sticky='ew')
        rejected_label = Label(rejected_frame, text='Rejections', bg='white', anchor='center')
        rejected_label.grid(row=1, column=0, sticky='ew')

        #dashboard interview rate section
        rates_frame = LabelFrame(ratios_frame, bg='white')
        rates_frame.grid(row=2, column = 0, columnspan=4, sticky='ew', pady=15)
        rates_frame.columnconfigure(0, weight=1)

        rates_label = Label(rates_frame, text=f'Interview rate {self.interview_rate}%: You have {self.interviews} interviews out of {self.applications} applications', bg='white', anchor='center')
        rates_label.grid(row=0, column=0, sticky='ew')

        #view all applications section
        all_applications_frame = Frame(self.master)
        all_applications_frame.grid(row=3, column=0, columnspan=4, sticky='ew')
        all_applications_frame.columnconfigure(0, weight=1)

        all_applications_button = ttk.Button(all_applications_frame, text='View all applications', width=20, command=self.import_applications)
        all_applications_button.grid(row=0, column=0, ipady=5)

    def import_applications(self):
        root = Toplevel(self.master)
        app = Applications(root)
        app.populate_treeview()

