#!/usr/bin/env bash
# Sets the web servers with thefollowing requirements:
#	Install Nginx if it not already installed
#	Create the folder /data/ if it doesn’t already exist
#	Create the folder /data/web_static/ if it doesn’t already exist
#	Create the folder /data/web_static/releases/ if it doesn’t already exist
#	Create the folder /data/web_static/shared/ if it doesn’t already exist
#	Create the folder /data/web_static/releases/test/ if it doesn’t already exist
#	Create a fake HTML file /data/web_static/releases/test/index.html
#	Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
#	Give ownership of the /data/ folder to the ubuntu user AND group
#	Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static


SERVER_CONFIG="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;
	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://sketchfab.com/bluepeno/models permanent;
	}
	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"
HOME_PAGE="<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		Holberton School
	<body>
</html>
"
# shellcheck disable=SC2230
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
    apt-get update
    apt-get -y install nginx
fi
mkdir -p /var/www/html /var/www/error
chmod -R 755 /var/www
echo 'Hello World!' > /var/www/html/index.html
echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html

mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "$HOME_PAGE" > /data/web_static/releases/test/index.html
[ -d /data/web_static/current ] && rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-available/default"
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi
