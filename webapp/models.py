from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    # @password.setter
    # def password(self, password):
    #     # self.password = generate_password_hash(password)
    #     self.password=password
    # def verify_password(self, password):
    #     # return check_password_hash(self.password, password)
    #     if self.password==password:
    #         return True
    #     else:
    #         return False