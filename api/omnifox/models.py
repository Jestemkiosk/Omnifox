from flask_restful import Resource, abort
from flask import request
import omnifox.database as database
import json

database.db.create_all()

class HomePage(Resource):

  def get(self):
    return {
      "Endpoints": {
        "GET /cities" : "Returns all of the cities",
        "GET /cities/<id:int>" : "Returns a city with a given ID.",
        "GET /foxes": "Returns all of the foxes",
        "GET /foxes/<id:int>": "Returns a fox with a given ID."
      }
    }

class Foxes(Resource):

  def get(self):
    foxes = database.Fox.query.all()
    return [fox.as_dict_full() for fox in foxes]

  def post(self):
    data = json.loads(request.data)

    fox = database.Fox(
      name=data['name'],
      gender=data['gender'],
      age=data['age'],
      city_name=data['city_name'],
      image_url=data['image_url']
    )

    database.db.session.add(fox)
    database.db.session.commit()
    return fox.as_dict_full()

class Fox(Resource):

  def get(self, id):
    fox = database.Fox.query.filter_by(id=id).first()
    if fox:
        return fox.as_dict_full()

    abort(404, message=f"No fox of id {id} found")

  def delete(self, id):
    abort(401, message="Unauthorized access")  # Due to no API Authorization, this is disabled in production;

    fox = database.Fox.query.filter_by(id=id).first()
    if fox:
      database.db.session.delete(fox)
      database.db.session.commit()
      return '', 204

    abort(404, message=f"No fox of id {id} found")

class Cities(Resource):

  def get(self):
    cities = database.City.query.all()
    return [city.as_dict_full() for city in cities]

  def post(self):
    data = json.loads(request.data)

    city = database.City(
      name=data['name'],
      users=data['users'],
      image_url=data['image_url']
    )

    database.db.session.add(city)
    database.db.session.commit()
    return city.as_dict_full()

class City(Resource):

  def get(self, id):
    city = database.City.query.filter_by(id=id).first()
    if city:
        return city.as_dict_full()

    abort(404, message=f"No city of id {id} found")

  def delete(self, id):
    abort(401, message="Unauthorized access")  # Due to no API Authorization, this is disabled in production;

    city = database.City.query.filter_by(id=id).first()
    if city:
      database.db.session.delete(city)
      database.db.session.commit()
      return '', 204

    abort(404, message=f"No city of id {id} found")