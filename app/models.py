from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True,index=True, nullable=False)
    email = db.Column(db.String(130), unique=True, index=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    joined=db.Column(db.DateTime)
    status=db.Column(db.String(20), nullable=True)
    profile_img = db.Column(db.String(30), nullable=False, default='avatar.jpg') 
    Usertype =db.Column(db.String(30) , nullable=True)
    last_time_seen=db.Column(db.DateTime)
    posts = db.relationship('Post', backref='author', cascade="all, delete-orphan",
    lazy=True)

    def __repr__(self):
            return '{}{}{}'.format( self.id, self.username, self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(60), index=True, nullable=False)
    posted_content = db.Column(db.Text, index=True, nullable=False)
    date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
            return '{}{}{}'.format( self.id, self.post_title, self.date)
   

