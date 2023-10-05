#!/usr/bin/env bash
<<<<<<< HEAD
# Sets up a web server for deployment of web_static.

apt-get update

if ! command -v nginx &> /dev/null; then
    apt-get install -y nginx
fi

ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
=======
# Script that sets up your web servers for the deployment of web_static.

SITE_FILE=/etc/nginx/sites-available/default
END_POINT='\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n'
HTML_CONTENT=\
"<html>
>>>>>>> 1a1e941993bac195515a6eb20020724a6656fd93
  <head>
  </head>
  <body>
    Holberton School
  </body>
<<<<<<< HEAD
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sed -i '/^server {/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"

service nginx restart
=======
</html>"

CHECK_HBNB=$(grep 'location /hbnb_static' < "$SITE_FILE")

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p '/data/web_static/releases/test/'
sudo mkdir -p '/data/web_static/shared/'
sudo touch '/data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "$HTML_CONTENT" > '/data/web_static/releases/test/index.html'

if [ -z "$CHECK_HBNB" ]; then
	sudo sed -i "s@^\tserver_name _;@&$END_POINT@" $SITE_FILE
fi

sudo service nginx restart
>>>>>>> 1a1e941993bac195515a6eb20020724a6656fd93
