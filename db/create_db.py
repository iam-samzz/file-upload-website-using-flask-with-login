import sqlite3


conn = sqlite3.connect("upload.db")
command = '''create table if not exists upload_info(id integer primary key autoincrement,name varchar(30), file_name varchar(100));'''

conn.execute(command)
conn.close()