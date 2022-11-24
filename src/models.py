from flask_sqlalchemy import SQLAlchemy
# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy2 import render_er

db = SQLAlchemy()
# Base = declarative_base()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    user_name = Column(String(250),primary_key=True)
    name = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites = relationship(User)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    population = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250))
    people = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))
    planets = relationship(Favorites)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
   
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
