from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import logging
from flask.logging import default_handler





app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='signin'
login_manager.login_message = u"Please sign in to access this page"
login_manager.login_message_category = "secondary"
migrate = Migrate(app, db)

app.logger.removeHandler(default_handler)


formated = '[%(asctime)s] p %(levelname)s - %(message)s'
logging.basicConfig(format = formated, filename = "Warning.log", level=logging.WARNING)
fileHandler = logging.FileHandler("Warning.log")
fileHandler.setLevel(logging.WARNING)
app.logger.addHandler(fileHandler)


from app import views, models


