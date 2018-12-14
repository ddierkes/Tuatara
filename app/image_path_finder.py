"""
    This script should take an identifier and return a file path.  It is implemented
    simply with sqllite assuming a shared volume but any number of alternative methods could be used here.
    For instance, if your /images directory is just a bunch of flat jpgs, main could
    return f'./images/{identifier}.jpg' and that would be good enough.
"""

import sqlite3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
db = f'{dir_path}/data/imagepaths.db'

def get_path(identifier):
    """
       Given an identifier, a query is made to data/imagepaths.db for all the paths associated.
       These are returned as a list like so [(identifer, path1), (identifier, path2)]
       This function will return the value of path1.
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM imagepaths WHERE identifier=?", (identifier,))
    x = c.fetchall()
    conn.commit()
    conn.close()
    return x[0][1]

def main(identifier):
    """
        In order for any given identifier to be passed into the Tuatara system, there must be
        knowledge of where to find the corresponding image.  image_path_finder.main looks up
        an identifier and returns the path.  If it doesn't find what it is looking for, it returns
        a nonsense path that will 404.
    """
    try:
        filepath = './images/' + get_path(identifier)
    except:
        filepath = "./images/thisfilesimplydoesnotexistandshallfourofour"
    return filepath
