#!/usr/bin/env bash
# Setup of the web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create directories for web_static
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/server_name _;/a location /AirBnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0