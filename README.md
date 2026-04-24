# Job Application Tracker

A desktop application built with Python and Tkinter that helps you manage and track your job applications in one place. Monitor your application statuses, interview rates, and outcomes through a clean dashboard interface backed by a local SQLite database.

---

## Features Overview

- **Dashboard** — View live stats including total applications, interviews, offers, rejections and your interview rate at a glance
- **Application Table** — Browse all your applications in a sortable, searchable table
- **Add Applications** — Log new job applications with company, role, date, status and notes
- **Edit Applications** — Update any existing application record
- **Delete Applications** — Remove applications you no longer need to track
- **Search** — Find applications by company name or ID
- **Filter by Status** — Filter your table by Applied, Interview, Offer or Rejected

---

## Project Structure

```
Job_Tracker/
│
├── main.py                  # Entry point — calculates stats and launches the app
│
├── Views/                   # UI layer (Tkinter windows and forms)
│   ├── dashboard.py         # Dashboard window with stats overview
│   ├── Applications.py      # Main applications table view
│   ├── newApplicationForm.py        # Form for adding a new application
│   └── updateApplicationForm.py     # Form for editing an existing application
│
├── BusinessLogic/           # Logic layer — validation and data operations
│   └── CRUD.py              # Create, Read, Update, Delete operations
│
├── Database/                # Data layer — SQLite connection and raw SQL
│   └── Database.py          # Database class with all SQL methods
│
└── applications.db          # Auto-generated SQLite database file (created on first run)
```

---

## Prerequisites

Before running the app, make sure you have the following installed:

- **Python 3.8 or higher** — [Download here](https://www.python.org/downloads/)
- **Tkinter** — Included with most Python installations by default
- **SQLite3** — Included with Python's standard library, no separate install needed

To verify your Python installation:
```bash
python --version
```

To verify Tkinter is available:
```bash
python -m tkinter
```
A small test window should appear if Tkinter is installed correctly.

---

## Installation

1. **Clone or download the repository**
```bash
git clone https://github.com/yourusername/job-tracker.git
cd job-tracker
```

2. **Verify you have Python 3.8+**
```bash
python --version
```

3. **No additional dependencies required** — the project uses only Python standard library modules (`tkinter`, `sqlite3`, `re`)

4. **Run the application**
```bash
python main.py
```

The `applications.db` SQLite database file will be created automatically in the project root on first run.

---

## Usage

### Launching the App
```bash
python main.py
```

### Adding a New Application
1. From the Dashboard, click **Applications**
2. Click **Add New**
3. Fill in the Company Name, Role, Date (format: `YYYY-MM-DD`), Status and Notes
4. Click **Save**

### Editing an Application
1. Navigate to the Applications table
2. Click on a row to select it
3. Click **Edit Selection**
4. Update the fields and click **Save**

### Deleting an Application
1. Click on a row to select it
2. Click **Delete Selection**
3. The table will automatically refresh

### Searching
- Type a company name or ID into the **Search** field and click **Search**

### Filtering by Status
- Select a status from the **Status** dropdown and click **Filter**

---

## Author: Thato Ndlovu

Built as a portfolio project to demonstrate Python desktop application development with Tkinter, SQLite and a layered MVC-style architecture.

---

*Built with Python | Tkinter | SQLite3*
