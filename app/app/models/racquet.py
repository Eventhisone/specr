from app import db
from marshmallow import fields, Schema
from datetime import datetime
from .manufacturer import ManufacturerSchema
from .pattern_type import PatternTypeSchema

class Racquet(db.Model):
    """Model for tennis racquet."""

    __tablename__ = 'racquets'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    # name varchar
    name = db.Column(db.String)
    # headsize int
    headsize = db.Column(db.Integer)
    # num_crosses int
    num_crosses = db.Column(db.Integer)
    # num_mains int
    num_mains = db.Column(db.Integer)
    # manufacturer_id int [ref: > M.id]
    manufacturer_id = db.Column(db.Integer, db.ForeignKey(
        'manufacturers.id'), nullable=False)
    # len_crosses varchar
    len_crosses = db.Column(db.String)
    # len_mains varchar
    len_mains = db.Column(db.String)
    # start_cross varchar
    start_cross = db.Column(db.String)
    # start_main varchar
    start_main = db.Column(db.String)
    # tie_cross varchar
    tie_cross = db.Column(db.String)
    # tie_main varchar
    tie_main = db.Column(db.String)
    # skip_cross varchar
    skip_cross = db.Column(db.String)
    # skip_main varchar
    skip_main = db.Column(db.String)
    # short_side varchar
    short_side = db.Column(db.String)
    # long_side varchar
    long_side = db.Column(db.String)
    # url string
    url = db.Column(db.String)
    pattern_type_id = db.Column(db.Integer, db.ForeignKey(
        'pattern_types.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, data):
        self.name = data.get('name')
        self.headsize = data.get('headsize')
        self.num_crosses = data.get('num_crosses')
        self.num_mains = data.get('num_mains')
        self.manufacturer_id = data.get('manufacturer_id')
        self.len_crosses = data.get('len_crosses')
        self.len_mains = data.get('len_mains')
        self.start_cross = data.get('start_cross')
        self.start_main = data.get('start_main')
        self.tie_cross = data.get('tie_cross')
        self.tie_main = data.get('tie_main')
        self.skip_cross = data.get('skip_cross')
        self.skip_main = data.get('skip_main')
        self.short_side = data.get('short_side')
        self.long_side = data.get('long_side')
        self.url = data.get('url')
        self.pattern_type = data.get('pattern_type')
        self.created_at = datetime.datetime.utcnow()
        self.last_modified = datetime.datetime.utcnow()

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
        return Racquet.query.all()

class RacquetSchema(Schema):
    """
    Racquet Schema
    """

    id = fields.Int(dump_only=True)
    name = fields.Str()
    # name varchar
    # headsize int
    headsize = fields.Int()
    # num_crosses int
    num_crosses = fields.Int()
    # num_mains int
    num_mains = fields.Int()
    # manufacturer_id int [ref: > M.id]
    manufacturer_full = fields.Nested('ManufacturerSchema', only=("name",))
    # len_crosses varchar
    len_crosses = fields.Str()
    # len_mains varchar
    len_mains = fields.Str()
    # start_cross varchar
    start_cross = fields.Str()
    # start_main varchar
    start_main = fields.Str()
    # tie_cross varchar
    tie_cross = fields.Str()
    # tie_main varchar
    tie_main = fields.Str()
    # skip_cross varchar
    skip_cross = fields.Str()
    # skip_main varchar
    skip_main = fields.Str()
    # short_side varchar
    short_side = fields.Str()
    # long_side varchar
    long_side = fields.Str()
    # url int
    url = fields.Url()
    pattern_type_full = fields.Nested('PatternTypeSchema', only=("pattern_type",))
    created_at = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime()