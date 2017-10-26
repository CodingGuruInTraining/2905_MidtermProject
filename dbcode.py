import sqlite3
import time


def create_table():
    conn = sqlite3.connect('midtermapp.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS taskdata(id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "taskname TEXT UNIQUE, descript TEXT, opened INTEGER, seller TEXT, fare TEXT, "
              "duration TEXT, status TEXT)")
    conn.commit()
    c.close()
    conn.close()

def select_all_db():
    conn = sqlite3.connect('midtermapp.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute('SELECT * FROM taskdata')
    data = c.fetchall()
    c.close()
    conn.close()
    return data

def select_taskname_db(task_name):
    conn = sqlite3.connect('midtermapp.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    sqlString = "SELECT * FROM taskdata WHERE taskname = \'" + task_name + "\'"
    c.execute(sqlString)
    data = c.fetchone()
    c.close()
    conn.close()
    return data

def select_id_db(id):
    conn = sqlite3.connect('midtermapp.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM taskdata WHERE id = ?", id)
    data = c.fetchone()
    c.close()
    conn.close()
    return data

def add_task_db(taskname, descript, seller, fare, duration):
    conn = sqlite3.connect('midtermapp.db')
    c = conn.cursor()
    opened = int(time.time())
    c.execute("INSERT INTO taskdata (taskname, descript, opened, seller, fare, "
              "duration, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (taskname, descript, opened, seller, fare, duration, 'Active'))
    conn.commit()
    print("added task to db")
    c.close()
    conn.close()

def close_task_db(id):
    conn = sqlite3.connect('midtermapp.db')
    c = conn.cursor()
    c.execute("UPDATE taskdata SET status = 'Closed' WHERE id = ?", id)
    conn.commit()
    print('update complete')
    c.close()
    conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d