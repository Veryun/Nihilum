import marshmallow as ma
from marshmallow import validate


class UserSchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()


class UserPostSchema(ma.Schema):
    name = ma.fields.String(validate=validate.Length(min=1), required=True)
