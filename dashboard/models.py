
from dashboard import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    def get_user_id(self):
        return self.id

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    site_id= db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    subreddit = db.Column(db.String(200), nullable=False)
    body_text = db.Column(db.String(1000), nullable=False)
    num_comments =db.Column(db.Integer(), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    site_id= db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.Float(), nullable=False)
    parent_post = db.Column(db.String(100), nullable=False)
    parent_sub = db.Column(db.String(100),nullable=False)
    body_text = db.Column(db.String(1000),nullable=False)