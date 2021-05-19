from flask import Flask, jsonify, request, render_template

app = Flask(__name__) # still relative to module?

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'Cookies',
                'price': 2.99
            }
        ]
    },
    {
        'name': 'Another Store',
        'items': [
            {
                'name': 'Water',
                'price': 2.99
            }
        ]
    }
]

@app.route('/')  # root or endpoint 'https//www.google.com/' the forward slash homepage
def home():
    return render_template('index.html')


# POST - used to recieve data
# GET - used to send data back only
# Defining route and the method to which to access it
# POST - /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    # accessing the data that is coming back to us through the API from the FE
    # browser will send us JSON, the get_json() method converts the json string into a python dictonary
    request_data = request.get_json()

    # dictionary with a new_store
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    # Q: jsonify is important because we will return a dictionary and we need to return a string to the FE??
    # deserializes to python objects so when you return it, as a string
    return jsonify(new_store)


# GET - /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])  # 'http://127.0.0.1:5000/store/some_name'
# Iterate over stores, if the store name matches return that one, if there is no match return nothing
# Is this better as a try/catch
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET - /store
# Q: So we dont specify GET here because it is the default but we can if we wanted?
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # Q: not sure I understand whats going on here


# POST - /store/<string:name>/item, {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message': 'sorry no store was found'})


# GET - /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
