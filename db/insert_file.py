import sqlite3
import os

def run_insert_func(input_list):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLPATH = os.path.join(BASE_DIR,"upload.db")

    conn = sqlite3.connect(SQLPATH)

    conn.execute("insert into upload_info(name,file_name) values(?,?);",(input_list[0],input_list[1]))

    conn.commit()
    conn.close()


