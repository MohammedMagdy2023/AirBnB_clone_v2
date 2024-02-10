#!/usr/bin/env bash
# Install nginx if not already installed and create directories and files
# for the web static content

if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
echo "Hello World" > /data/web_static/releases/test/index.html

if [ -f "/data/web_static/current" ]; then
    sudo rm /data/web_static/current
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
else
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
fi

sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i "38i \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

sudo service nginx restart