FROM nginx:1.23.3

RUN apt-get update && \
    apt-get install -y && \
    rm /etc/nginx/conf.d/default.conf

COPY bagles_app.conf /etc/nginx/conf.d/

