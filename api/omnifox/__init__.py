from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
db = SQLAlchemy(app)

@app.errorhandler(ValueError)
def handle_value_err(e):
  return (str(e), 422)

@app.errorhandler(TypeError)
def handle_type_err(e):
  return (str(e), 422)

from omnifox import routes