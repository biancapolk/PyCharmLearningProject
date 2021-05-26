from flask_sqlalchemy import SQLAlchemy


# Looks at all of the objects that we tell it to, and maps the objects to the DB
db = SQLAlchemy()

# Added this after I started recieving errors
# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)