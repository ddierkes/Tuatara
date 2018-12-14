# You must build a .db outside of this code base
The data directory is a mounted volume when this runs within a container.
It accesses a table of identifiers mapped to file paths, but that table should be built elsewhere.  You can use tablebuilder.py to initialize that table and dbCalls.py to populate it, but something more sophisticated would be necessary at any kind of scale.
