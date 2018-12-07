FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.8

COPY ./app /app

COPY ./requirements.txt /app/requirements.txt
RUN apk add --no-cache jpeg zlib && \
    apk add --no-cache -t .dev gcc musl-dev jpeg-dev zlib-dev && \
    pip install -r requirements.txt && \
    apk rm .dev

VOLUME /app/images
