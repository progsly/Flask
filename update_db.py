from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    data = db.Column(db.String(20), unique=True)
    template = db.Column(db.String(20), unique=True)
    zip = db.Column(db.String(30))


db.drop_all()
db.create_all()
