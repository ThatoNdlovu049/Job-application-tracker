import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Applications(Id INTEGER PRIMARY KEY AUTOINCREMENT, Company TEXT NOT NULL, Role TEXT NOT NULL, Date TEXT NOT NULL, Status TEXT NOT NULL, Notes TEXT NOT NULL)")
        self.conn.commit()

    def read_all_applications(self):
        self.cursor.execute("SELECT * FROM Applications")
        rows = self.cursor.fetchall()
        return rows

    def search(self,search_value):
        self.cursor.execute("SELECT * FROM Applications WHERE Id = ? OR Company = ?", (search_value, search_value))
        rows = self.cursor.fetchall()
        return rows

    def filter_applications(self, filter_by):
        self.cursor.execute("SELECT * FROM Applications WHERE Status = ?", (filter_by,))
        rows = self.cursor.fetchall()
        return rows

    def add_application(self, company, role, date, status, notes):
        self.cursor.execute("INSERT INTO Applications(Company,Role,Date,Status,Notes) VALUES(?,?,?,?,?)", (company, role, date, status, notes))
        self.conn.commit()

    def delete_application(self,company_id):
        self.cursor.execute("DELETE FROM Applications WHERE Id = ?", (company_id,))
        self.conn.commit()

    def edit_application(self,  application_id,company, role, date, status, notes):
        self.cursor.execute("UPDATE Applications SET Company =?, Role =?, Date =?, Status =?, Notes =? WHERE Id = ?", (company, role, date, status, notes, application_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()