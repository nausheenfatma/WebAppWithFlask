# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:14:36 2016

@author: nausheenfatma
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date,Boolean,TIMESTAMP,Text
from sqlalchemy.orm import sessionmaker

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://localhost/FlaskTest'
app.secret_key = 'some_secret'
db = SQLAlchemy(app)


 
#Create the Post Class
class Post(db.Model):
    __tablename__ = "Post"
    id = Column(db.Integer, primary_key=True)
    author = Column(db.String(255))
    title = Column(db.String(255),nullable=False)
    #created_on=Column(TIMESTAMP,server_default=db.func.current_timestamp())
    content = Column(db.Text)
    published = Column(db.Boolean, server_default='True', nullable=False)    
 
    def __init__(self, author,title, content,published):
        self.author = author
        self.title = title
        self.content=content
        self.published=published
         
    def add(self,post):
        db.session.add(post)
        return session_commit()
 
    def update(self):
        return session_commit()
 
    def delete(self,post):
        db.session.delete(post)
        return session_commit()
 
def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        reason=str(e)
 
if __name__ == '__main__':
    db.create_all()
    first_entry=Post("Paulo Coulo","Alchemist","",False)
    second_entry=Post("Mitch Albom","Tuesdays with Morrie","",False)
    
    db.session.add_all([first_entry, second_entry])
    db.session.commit()    

