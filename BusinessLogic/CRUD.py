from tkinter import messagebox
import re
from Database.Database import Database

db = Database('applications.db')

class CRUD:

    def read_all_applications(self, gui):
        rows = db.read_all_applications()

        #clear treeview's previous results
        for row in gui.treeview.get_children():
            gui.treeview.delete(row)

        if rows:
            for row in rows:
                gui.treeview.insert('', 'end', values=row)
        else:
            messagebox.showerror('Error', 'Could not read applications in the database')

    def add_application(self, gui):

        company = gui.company_name.get().strip().lower()
        role = gui.role.get().strip().lower()
        date = gui.date.get().strip().lower()
        status = gui.status.get().strip().lower()
        notes = gui.notes.get().strip().lower()

        if company and role and date and status and notes:
            match = re.match(r"^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", date)
            if match:
                try:
                    db.add_application(company.lower(), role.lower(), date.lower(), status.lower(), notes.lower())
                    messagebox.showinfo('Success', 'Application added successfully')
                except Exception as e:
                    messagebox.showerror('Error', str(e))
            else:
                messagebox.showerror('Error', 'Date is entered in an incorrect format. Please enter YYYY-MM-DD')
        else:
            messagebox.showerror('Error', 'Please fill all fields')

    def search_application(self, gui):
        search_value = gui.search_value.get().strip().lower()
        rows = db.search(search_value)

        #clearing treeview past results
        for row in gui.treeview.get_children():
            gui.treeview.delete(row)

        if rows:
            for row in rows:
                gui.treeview.insert('', 'end', values=row)
        else:
            messagebox.showerror('Error', 'Could not find application in the database')

    def filter(self, gui):
        status = gui.status.get().strip().lower()
        rows = db.filter_applications(status)

        for row in gui.treeview.get_children():
            gui.treeview.delete(row)

        if rows:
            for row in rows:
                gui.treeview.insert('', 'end', values=row)
        else:
            messagebox.showinfo('No results', f'No applications with status: {status}')

    def delete_application(self,gui, company):
        company_name = company.lower()

        try:
            db.delete_application(company_name)
            messagebox.showinfo('Success', 'Application deleted successfully')
            #clear treeview's previous
            for row in gui.treeview.get_children():
                gui.treeview.delete(row)
            #repopulating treeview
            rows = db.read_all_applications()
            if rows:
                for row in rows:
                    gui.treeview.insert('', 'end', values=row)
            else:
                messagebox.showerror('Error', 'Could not read database')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def edit_application(self,gui):
        company_id = int(gui.company_id)
        company_name = gui.company_name.get().strip().lower()
        role = gui.role.get().strip().lower()
        date = gui.date.get().strip().lower()
        status = gui.status.get().strip().lower()
        notes = gui.notes.get().strip().lower()

        if company_id and company_name and role and date and status and notes:
            match = re.match(r"^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", date)
            if not match:
                messagebox.showerror('Error', 'Date must be in YYYY-MM-DD format')
                return
            db.edit_application(company_id, company_name,role,date,status,notes)
            messagebox.showinfo('Success', 'Application edited successfully')
        else:
            messagebox.showerror('Error', 'Please fill all fields')
