"""
The relationship between the volume of mounted files and the ids Tuatara processes need to be mapped.
To limit the complexity of the project, a simple two column table of ids matched to paths should work.
That table will be mounted as a volume when the container launches and should be built outside of this app.
To initialize such a table, just run this script.
"""

import sqlite3

conn = sqlite3.connect('imagepaths.db')

c = conn.cursor()

c.execute("CREATE TABLE imagepaths (identifier text, path text, PRIMARY KEY(path))")

conn.commit()
conn.close()
