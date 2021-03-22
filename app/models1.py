from datetime import datetime
from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20), index=True, unique=True)
   surname = db.Column(db.String(20), index=True, unique=True)
   d_b = db.Column(db.String(12))
   books = db.relationship("Book", backref="author", lazy="dynamic")

   def __str__(self):
       return f"<User {self.username}>"

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(50), index=Troue, unique=True)
   genre = db.Column(db.String(20), index=True, unique=True)
   pages = db.Column(db.Integer)
   stock = db.Column(db.Boolean, default=False, nullable=False)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

   def __str__(self):
       return f"<Post {self.id} {self.body[:50]} ...>