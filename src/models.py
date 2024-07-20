import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as sqlalchemy_enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()

class MediaEnum(Enum):
    PHOTO = "PHOTO"
    VIDEO = "VIDEO"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    post = relationship("post", backref="user")
    comment = relationship("comment", backref="user")
    follower = relationship("follower", backref="user")
    follower = relationship("follower", backref="user")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = (Integer, ForeignKey("user.id"))
    user_to_id = (Integer, ForeignKey("user.id"))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    media = relationship("media", backref="post")
    comment = relationship("comment", backref="post") 

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    mediatype = Column(sqlalchemy_enum(MediaEnum))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
