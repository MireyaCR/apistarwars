from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


class People(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True, nullable=False)
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
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))
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
            "created":self.created,
            "edited":self.edited,
            "url":self.url, 
        }


# class Favorites(Base):
#     __tablename__ = 'favorites'
#     id = Column(Integer, primary_key=True)
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     people_id = Column(Integer, ForeignKey('people.id'))
#     user_id = Column(Integer, ForeignKey('user.id'))
#     favorites = relationship(User)
# 
