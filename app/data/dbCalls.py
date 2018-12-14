"""
This script is just for diagnostic purposes or building test data.   The values
found in the imagespath.db table should be generated outside of the Tuatara code base.
Being able to generate test data here could serve as an example for how the production
data should work.
"""

import sqlite3
import os
import traceback

dir_path = os.path.dirname(os.path.realpath(__file__))
db = f'{dir_path}/imagepaths.db'


def add_row(data):
    try:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("INSERT INTO imagepaths VALUES (?, ?)", data)
        conn.commit()
        conn.close()
        return f"Image Path {data} added to table"
    except sqlite3.IntegrityError:
        return f"Image Path {data} already in table"
    except:
        x = traceback.format_exc()
        return f"{x}"

def read_all():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM imagepaths")
    x = c.fetchall()
    conn.commit()
    conn.close()
    return x

def read_rows(data):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM imagepaths WHERE identifier=?", (data,))
    x = c.fetchall()
    conn.commit()
    conn.close()
    return x

def remove_row(data):
    try:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("DELETE FROM imagepaths WHERE identifier=? AND path = ?", (data[0], data[1], ))
        conn.commit()
        conn.close()
    except:
        x = traceback.format_exc()
        return f"{x}"
    return "removed"

if __name__ == "__main__":
    print(add_row(("windmill", "somedir/windmill.jpg")))
    print(remove_row(('windmill', 'somedirwindmill.jpg')))
    print(read_all())
    print(read_rows("buggy"))
