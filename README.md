# Flask Starter
Flask starter template

## What is included
- [x] `Flask-Bootstrap` -> UI
- [x] `Flask-Migrate` -> DB Migrations
- [x] `Flask-Moment` -> Date & Time
- [x] `Flask-SQLAlchemy` -> SQL ORM
- [x] `Flask-WTF` -> Forms
- [x] `python-dotenv` -> Environement Variables


## Steps to Configure your application

###  1.  Clone flask boilerplate

###  2.  Change app to your desired name e.g. `APP_NAME`
```bash
mv flask-boilerplate APP_NAME && cd APP_NAME
```

### 3. Add your environment variables folowing `.env.sample`

### 4.  Configure Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Edit App configurations
To change your app configuration, update `.flaskenv` file. It will automatically resync

### 6. Run Migrations
```bash
touch db.sqlite
flask db init
flask db migrate -m 'Initial migration'
flask db upgrade
```

### 7. Run the app
```bash
flask run
```

## Setup Git
```bash
git remote add origin https://github.com/ErickMwazonga/flask-starter.git
git branch -M main
git push -u origin main
```

## Other Configurations
### VSCODE Setup
1. **Exclude Files**

    Text Editor -> Files -> Exclude -> Add Pattern -> add  `**/__pycache__`

2. **Extenstions**
   - `ms-python.python`
   - `wholroyd.jinja`
   - `strap.flask-snippets`

3. **Other Extenstions**
   - `qwtel.sqlite-viewer`
   - `esbenp.prettier-vscode`
   - `formulahendry.auto-close-tag`
   - `formulahendry.auto-rename-tag`
