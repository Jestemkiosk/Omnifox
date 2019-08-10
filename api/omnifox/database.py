from omnifox import db

class City(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  users = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.String)
  foxes = db.relationship('Fox', backref="city", lazy=True)

  def as_dict_full(self):
    if not self.foxes:
      return self.as_dict()
    return {
      "id": self.id,
      "name": self.name,
      "users":self.users,
      "image_url": self.image_url,
      "foxes": [fox.as_dict() for fox in self.foxes]
    }

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "users":self.users,
      "image_url":self.image_url
    }

  def __repr__(self):
    return self.name

class Fox(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  gender = db.Column(db.String(6), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.String)
  city_name = db.Column(db.Integer, db.ForeignKey('city.name'))

  def as_dict_full(self):
    if not self.city:
      return self.as_dict()
    return {
      "id": self.id,
      "name": self.name,
      "gender":self.gender,
      "age": self.age,
      "image_url": self.image_url,
      "city": self.city.as_dict()
    }

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "gender":self.gender,
      "age": self.age,
      "image_url": self.image_url,
    }

  def __repr__(self):
    return f"{self.name} ({self.age})"
