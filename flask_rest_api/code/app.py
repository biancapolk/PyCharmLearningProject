from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'json'
# creating a list called items
items = []


# Defining our resource
class Item(Resource):
    # passing in name of the student and returning the name of the student or what we give it
    def get(self, name):
        # this is what the method is doing to do when endpoints called
        item = next(filter(lambda x: x['name'] == name, items),
                    None)  # retrieve the next item that matches the name of the item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:  # Ensures
            return {'message': f"An item with this name '{name}' already exists."}, 400

        data = request.get_json(
            force=True)  # if the request does not attach a JSON payload or have the proper content-type or header this will give an error
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        # a dictionary with a list of items called items that returns items
        return {'items': items}


# adding the resource student, ad determine how it is going to be accessed
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf

# runs the app
app.run(port=5000, debug=True)
