import sqlite3
from db import db


# Internal representation that contain the properties of an item
class ItemModel(db.Model):
    # Creating a model for the DB here, tells it how to read it
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Return JSON representation of the model
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first  # This translates to some SQL code: SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

