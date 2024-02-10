#!/usr/bin/env bash
# Install nginx if not already installed and create directories and files
# for the web static content

if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

touch /data/web_static/releases/test/index.html
echo "Hello World" > /data/web_static/releases/test/index.html

if [ -f "/data/web_static/current" ]; then
    rm /data/web_static/current
    ln -sf /data/web_static/releases/test/ /data/web_static/current
else
    ln -sf /data/web_static/releases/test/ /data/web_static/current
fi

chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu /data/
sed -i "38i \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

service nginx restart
