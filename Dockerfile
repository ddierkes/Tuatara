ARG BASE_IMAGE=tiangolo/uwsgi-nginx-flask:python3.7-alpine3.8


FROM ${BASE_IMAGE} as builder
WORKDIR /repo
COPY . .
RUN apk add git && \
    rm -rf dist && \
    python setup.py bdist_wheel


FROM ${BASE_IMAGE}
COPY --from=builder /repo/dist/ /tmp/dist
RUN apk add --no-cache jpeg zlib && \
    apk add --no-cache -t .dev gcc musl-dev jpeg-dev zlib-dev && \
    pip install --no-cache-dir /tmp/dist/*whl && \
    apk del .dev && \
    rm -rf /tmp/dist
VOLUME /app/images
