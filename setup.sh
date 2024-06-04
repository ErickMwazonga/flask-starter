#!/bin/bash

# Prompt for the app name
read -p "Enter the name of your application: " APP_NAME

# Rename the directory if it exists
if [ -d "flask-starter" ]; then
    mv flask-starter "$APP_NAME"
    echo "changes directory successfuly."
fi

# Check if the directory was renamed successfully
if [ -d "$APP_NAME" ]; then
    cd "$APP_NAME"
else
    echo "Failed to rename directory. Please make sure you have cloned flask-starter"
    exit 1
fi

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
if command -v pip >/dev/null 2>&1; then
    pip install -r requirements.txt
elif command -v pip3 >/dev/null 2>&1; then
    pip3 install -r requirements.txt
else
    echo "pip or pip3 not found. Please install Python pip."
    exit 1
fi

# Run migrations
flask db init
flask db migrate -m 'Initial migration'
flask db upgrade

# Run the app
flask run &