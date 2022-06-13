from app import db
from marshmallow import fields, Schema
from datetime import datetime

class Manufacturer(db.Model):
    """Model for manufacturer."""

    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, data):
        return

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.last_modified = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Manufacturer.query.all()

class ManufacturerSchema(Schema):
    """
    Manufacturer Schema
    """

    id = fields.Int(dump_only=True)
    name = fields.Str()
    url = fields.Url()
    created_at = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime()