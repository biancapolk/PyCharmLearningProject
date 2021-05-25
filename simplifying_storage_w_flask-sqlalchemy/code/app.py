from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user_resource import UserRegister
from resources.item_resource import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register') # WHEN we exceute a post request to /register it will call the UserRegister class

if __name__ == '__main__': # Q: This allows us to import app without running app.run()
    from db import db # Q: Circular imports
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True