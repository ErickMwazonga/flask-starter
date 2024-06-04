#!/bin/bash

# Prompt for the app name
read -p "Enter the name of your application: " APP_NAME

# Rename the directory
mv flask-starter "$APP_NAME"
cd "$APP_NAME"

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
flask db init
flask db migrate -m 'Initial migration'
flask db upgrade

# Run the app
flask run

# Open the app in the default web browser
open http://127.0.0.1:5001
echo "Please open a browser and navigate to http://127.0.0.1:5001"