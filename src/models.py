from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.user_name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height":self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color":self.skin_color,
            "birth_year": self.birth_year,
            "homeworld":self.homeworld,
            "url":self.url,
         }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_planet = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return{
            "id":self.id,
            "name_planet":self.name_planet,
            "diameter":self.diameter,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "gravity":self.gravity,
            "population":self.population,
            "climate":self.climate,
            "terrain":self.terrain,
            "surface_water":self.surface_water,
            "url":self.url, 
        }


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table = db.Column(db.String)
    table_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
   
    def __repr__(self):
       return '<Favorites %r>' % self.id

    def serialize(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "table":self.table,
            "table_id":self.table_id,
        }