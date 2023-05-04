#!/usr/bin/env bash
# Script will set up web servers

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "
<!DOCTYPE html>
<html>
  <head>
    <title>Testing Ngnix Configuration</title>
  </head>
  <body>
     School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
