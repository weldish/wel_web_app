from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='signin'
login_manager.login_message = u"Please sign in to access this page"
login_manager.login_message_category = "secondary"
migrate = Migrate(app, db)


from app import views, models

admin=Admin(app)
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Post, db.session))

