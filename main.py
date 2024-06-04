import os

from flask_migrate import Migrate
from dotenv import load_dotenv

from app import create_app, db 

app = create_app(os.getenv('FLASK_CONFIG', 'default')) 

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Configure db migrations
migrate = Migrate(app, db)
