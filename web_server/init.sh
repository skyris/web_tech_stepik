#!/bin/bash
sudo apt-get install nginx
cd ~
mkdir web
cd web
mkdir public uploads etc
cd public
mkdir img css js

cp ~/web_server/nginx.conf /home/box/web/etc/nginx.conf

sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx start﻿