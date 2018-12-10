# Tuatara, a IIIF Image Server

Tuatara, named for a three eyed lizard that sees perhaps in color and bitonal, is a simple IIIF image server.  Put docker on your machine, clone it and build it.

```
git clone thisrepo
cd tuatara
docker build -t tuatara .
```

Then run the container at a port of your choosing (in this case 8888) to serve a directory of images of your choosing (in this case /var/www/tuatara/app/images)

```docker run -v /var/www/tuatara/app/images:/app/images -p 8888:80 tuatara:latest```
