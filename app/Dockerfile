FROM nginx:1.23.3

RUN apt-get update && apt-get install -y python3 uwsgi python3-pip systemctl libpq-dev python3-dev python3-psycopg2 uwsgi-plugin-python3

RUN mkdir /bagles_app

WORKDIR /bagles_app

COPY . . 

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y python3 uwsgi python3-pip systemctl libpq-dev python3-dev python3-psycopg2 uwsgi-plugin-python3

RUN pip3 install --no-cache --upgrade pip -r requirements.txt

RUN cp settings/bagles_app.service /etc/systemd/system/

COPY settings/bagles_app /etc/nginx/conf.d/bagles_app.conf

RUN rm /etc/nginx/conf.d/default.conf

RUN systemctl enable bagles_app

RUN systemctl start bagles_app

RUN service nginx stop 

RUN service nginx start

