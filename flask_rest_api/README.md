# Your first flask application
    See flask_rest_api.py
# HTTP VERBS

    # What is a web server?
        Designed to recieve incomming web requests.
    # When we send something to a web server we expect something in return.
        GET / HTTP/1.1
        Host: http://wwww.google.com 
    # The server sees: 
        Verb = Get - Path = / Protocol = HTTP/1.1
        GET / HTTP/1.1
    
        Examples:
    
        GET /login HTTP/1.1
        Host: http://wwww.twitter.com 
    
        GET /download/mac HTTP/1.1
        Host: http://wwww.git-scm.com 
    
        GET / HTTP/1.1
        Host: http://wwww.google.co.uk 
    
    # Verb Meanings: 
        GET -   Retrieve something -  GET /item/1
        POST - Recieve data, and use it -  POST /item
        PUT -  Make sure that something is there -  PUT /item
        DELETE -    Remove something-  DELETE /item/1

# What is a REST API
    REST is a way of thinking about how a web server responds to your requests
    Think of it as having resources 
    REST is STATELESS - meaning one request cannot depend on another request.
        --The server does not kow the item now exists--

# Creating our application endpoints 


# Calling the API from JavaScript 
    Flask automaticlaly looks for template folder
    ** see render_template here: flask_rest_api/template/index.html

# Errors I ran into
    
    404 Error - 
        1. **Solved by** ensure that the function for the specified route returning the render_template
            @app.route('/')  # root or endpoint 'https//www.google.com/' the forward slash homepage
            def home():
                return render_template('index.html')
    500 Internal Server Error - 
        1. check app.py and index.html
        2. reload web page 
        3. clear history
        4. clear cache
        5. **Solved by** ensuring that 
             Becuase I named my templates folder something other than templates and don't want to rename it to the default, I told Flask to use that other directory by doing:
                app = Flask(__name__, template_folder='template')  # still relative to module

# Flask RESTful and Authentication 

    Check(s):
        endpoint
        url
    Status codes:
        404, 201,202

    ------------------------------------------------------------------------------------------------------------------------
    Q's: 

        data = request.get_json(force=True) # if the request does not attach a JSON payload or have the proper content-type or header this will give an error
        debug = True # creates a nice html page with the errorkd

    ------------------------------------------------------------------------------------------------------------------------
    debug = True # creates a nice html page with the errorkd

    Steps in creating a app.py
    1. imports (flask, slask restfull: Resource, Api)
    2. Initialize app & api 
    3. Global variables
    4. Classes and functions
    5. Call api.add_resource(Class, '/route')
    6. app.run(port, debug=True)

# Payload?

# The ItemsList and creating items

#
------------------------------------------------------------------------------------------------------------------------
    Q's: 

        item = filter(lambda x: x['name'] == name, items)  #Dpes this call occur in place?
        
        *Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.
        item 

        *item = next(filter(lambda x: x['name'] == name, items), None) # retrieve the next item that matches the name of the item

        def identity(payload):
            user_id = payload['identity']
            return userid_table.get(user_id, None)

        # Allows us to map a user by its username
        username_mapping = {u.username: u for u in users}
        # Allows us to map a user by its user_id
        userid_mapping = {u.id: u for u in users}

    ------------------------------------------------------------------------------------------------------------------------

# Authentication
    

# DELETE

    Q: 
        # Is there a better way to do this
        global items
        item = list(filter(lambda x: x['name'] != name, items))
# PUT to create or update items

        Section 75
        Section 76
# Optimizing our final code and request parsing