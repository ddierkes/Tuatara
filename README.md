# Tuatara, a IIIF Image Server

Named for a three eyed lizard that sees perhaps in color and bitonal, Tuatara is a simple [IIIF Image Server](https://iiif.io/).  Put docker on your machine, clone it and build it.

```
git clone https://github.com/ddierkes/tuatara.git
cd tuatara
docker build -t tuatara .
```

Then run the container at a port of your choosing (in this case 8888) to serve a directory of images of your choosing (in this case /var/www/tuatara/app/images) and an identifier to image path table from a directory mounted at /data.

```docker run -v /var/www/tuatara/app/images:/app/images -v /var/www/tuatara/app/data:/app/data -p 8888:80 tuatara:latest```
