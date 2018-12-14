# This Flask App serves up images based on IIIF parameters

Given a path such as /some_identifier/full/200,/0/default.jpg, you should receive an image 200 pixels wide assuming you've successfully mounted an image in your images directory and a line in a .db file in a mounted /data directory of format ('some_identifier', 'somedir/some_identifier.jpg').
