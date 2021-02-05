# standard
import os
import sys
from datetime import datetime
# internal
from utils import get_engine
# external
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey


# Base Model
Base = declarative_base()


# author model:
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    profile = relationship('Profile', backref='author', uselist=False)
    posts = relationship('Post', backref='author')


# author's profile model:
class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    tell = Column(String(20), nullable= True)
    email = Column(String(50), nullable=True, unique=True)
    address = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'))


# category model:
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    posts = relationship('Post', backref='category')


# post_tag pivot table:
post_tag = Table('post_tag', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
    )


# tags model:
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)


# post model:
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'))
    author_id = Column(Integer, ForeignKey('authors.id'))
    tags = relationship('Tag', secondary=post_tag, backref='posts')


if __name__ == '__main__':
    # default message
    msg = 'action not found!'
    # get action from command line
    action = sys.argv[1]
    if action == 'create':
        Base.metadata.create_all(get_engine())
        msg = 'models created successfully.'
    elif action == 'drop':
        Base.metadata.drop_all(get_engine())
        msg = 'models destroyed.'
    print(msg)

