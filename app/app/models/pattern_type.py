from app import db
from marshmallow import fields, Schema
from datetime import datetime

class PatternType(db.Model):
    """Model for patterntype."""

    __tablename__ = 'pattern_types'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    pattern_type = db.Column(db.String)
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
        return PatternType.query.all()

    @staticmethod
    def get_one_by_name(pattern_type):
        return PatternType.query.filter_by(pattern_type=pattern_type).first()


class PatternTypeSchema(Schema):
    """
    PatternType Schema
    """

    id = fields.Int(dump_only=True)
    pattern_type = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime()