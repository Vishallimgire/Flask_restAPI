from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
# import pdb;pdb.set_trace()
from security import authenticate, identity
from user import UserRegister
from items import Item, ItemList

app = Flask(__name__)
app.secret_key = 'vishallimgire1995'
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)