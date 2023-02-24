FROM nginx:1.23.3

RUN apt-get update && \
    rm /etc/nginx/conf.d/default.conf && \
    addgroup --system bagles_app && \
    adduser --system --group bagles_app

COPY bagles_app.conf /etc/nginx/conf.d/
