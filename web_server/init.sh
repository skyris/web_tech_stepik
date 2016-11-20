#!/bin/bash
sudo apt-get update
sudo apt-get install nginx
cd ~
mkdir web
cd web
mkdir public uploads etc
cd public
mkdir img css js
cd ~
sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
cp ~/web_server/nginx.conf /home/box/web/etc/nginx.conf

sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
# sudo /etc/init.d/nginx start﻿
sudo nginx