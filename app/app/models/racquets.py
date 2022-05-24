from app import db
from datetime import datetime

class Racquet(db.model):
    """Model for tennis racquet."""

    __tablename__ = 'racquets'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    # name varchar
    # headsize int
    # num_crosses int
    # num_mains int
    # manufacturer_id int [ref: > M.id]
    # len_crosses varchar
    # len_mains varchar
    # start_cross varchar
    # start_main varchar
    # tie_cross varchar
    # tie_main varchar
    # skip_cross varchar
    # skip_main varchar
    # short_side varchar
    # long_side varchar
    # url int
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

class RacquetSchema(Schema):
    """
    Racquet Schema
    """

    id = fields.int(dump_only=True)
    name = fields.Str()
    # name varchar
    # headsize int
    # num_crosses int
    # num_mains int
    # manufacturer_id int [ref: > M.id]
    # len_crosses varchar
    # len_mains varchar
    # start_cross varchar
    # start_main varchar
    # tie_cross varchar
    # tie_main varchar
    # skip_cross varchar
    # skip_main varchar
    # short_side varchar
    # long_side varchar
    # url int
    created_at = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime()