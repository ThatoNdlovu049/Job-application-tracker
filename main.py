from tkinter import Tk
from Database.Database import Database
from Views.dashboard import Dashboard

db = Database('applications.db')

applications = 0
interviews = 0
offers = 0
rejections = 0
interview_rate = 0

rows = db.read_all_applications()
for row in rows:
    applications += 1
    if row[4] == 'interview':
        interviews += 1
    elif row[4] == 'offer':
        offers += 1
    elif row[4] == 'rejected':
        rejections += 1

if applications > 0:
    interview_rate = int((interviews / applications) * 100)

root = Tk()
app = Dashboard(root,applications,interviews,offers,rejections,interview_rate)
root.mainloop()