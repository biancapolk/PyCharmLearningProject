from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secretkey'
api = Api(app)

# JWT object uses app, authenticate, identity functions TOGETHER to authenticate users
# JWT creates a new endpoint:  /auth
# when /auth called we send JWT the username and pw
# JWT(username, pw) -> authenticate(username, pw)
# Find correct user object, using that username
# compare its pw to the one that we received to do the /auth endpoint
# if the match , we return the user and that becomes the identity
jwt = JWT(app, authenticate, identity)

# creating a list called items
items = []


# Defining our resource
class Item(Resource):
    # passing in name of the student and returning the name of the student or what we give it
    @jwt_required
    def get(self, name):
        # this is what the method is doing to do when endpoints called
        item = next(filter(lambda x: x['name'] == name, items), None)
        # retrieve the next item that matches the name of the item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:  # Ensures.....
            return {'message': f"An item with this name {name} already exists."}, 400
        data = request.get_json(force=True)  # if the request does not attach a JSON payload or have the proper content-type or header this will give an error
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        # a dictionary with a list of items called items that returns items
        return {'items': items}


# adding the resource student, ad determine how it is going to be accessed
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
# api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf

# runs the app
app.run(port=5000, debug=True)
