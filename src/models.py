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
    user_name = db.Column(db.String(250),primary_key=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
#    

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     id = Column(Integer, primary_key=True)
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     people_id = Column(Integer, ForeignKey('people.id'))
#     user_id = Column(Integer, ForeignKey('user.id'))
#     favorites = relationship(User)

class People(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    population = db.Column(db.Integer)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))
    name = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    url = db.Column(db.String(250))
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height":self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color":self.skin_color,
            "population" :self.population,
            "birth_year": self.birth_year,
            "gender":self.gender,
            "created":self.created,
            "edited" : self.edited,
            "homeworld":self.homeworld,
            "url":self.url,
         }


# class Planets(Base):
#     __tablename__ = 'planets'
#     id = Column(Integer, primary_key=True)
#     name_planet = Column(String(250))
#     diameter = Column(String(250))
#     rotation_period = Column(String(250))
#     orbital_period = Column(String(250))
#     gravity = Column(String(250))
#     population = Column(String(250))
#     climate = Column(String(250))
#     terrain = Column(String(250))
#     surface_water = Column(String(250))
#     created = Column(String(250))
#     edited = Column(String(250))
#     url = Column(String(250))
#     planets = relationship(Favorites)

   

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')
