#README

# INTRODUCTION
    * REST API using GIT

## Code characteristics

* Python 3
    * gitTutorial
        * commands
        * models
        * static
        * templates
        * views
    * tests

# Clone the code repository into ~/dev/my_app
    $ mkdir -p ~/dev
    $ cd ~/dev
    $ git clone <Bia to place url here>


## Setting up a development environment
	$ python3 -m venv env
	$ source env/bin/activate

      # Installing Flask
	 python -m pip install Flask==1.1.1

      # Install required Python packages
    	$ cd chcp-backend-master
    	$ pip install -r requirements.txt

## Initializing the Database

    # Create DB tables and populate the roles and users tables
    $ python manage.py init_db


## Running the app

    # Start the django development web server
        $
	#Start


Point your web browser to http://localhost:5000/

You can make use of the following users:
- email `user@example.com` with password `Password1`.
- email `admin@example.com` with password `Password1`.


## Authors

- BIANCA