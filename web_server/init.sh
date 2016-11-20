#!/bin/bash
# install nginx
sudo apt-get update
sudo apt-get install nginx
# creating folders
cd ~
mkdir web etc
cd web
mkdir public uploads etc
cd public
mkdir img css js
cd ~
# Add config for nginx
sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
cp ~/web_server/nginx.conf /home/box/web/etc/nginx.conf
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default

# sudo nginx
# sudo /etc/init.d/nginx restart
# Add WSGI application
cp ~/web_server/hello.py ~/web/hello.py
# Add gunicorn config
cp ~/web_server/hello_config.py ~/etc/hello.py
sudo ln -sf ~/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/gunicorn restart