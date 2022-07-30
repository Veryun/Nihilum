import marshmallow as ma
from marshmallow import validate


class ErrorSchema(ma.Schema):
    error = ma.fields.String()
