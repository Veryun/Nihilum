from Nihilum.models.base import BaseMixin
from Nihilum.models import db
from Nihilum.models.associations import engine_fuel_association


class Fuel(db.Model, BaseMixin):
    __tablename__ = "fuel"
    energy_value = db.Column(db.Integer, nullable=False)
    consumption_rate = db.Column(db.Integer, nullable=False)
    engines = db.relationship('engine', secondary=engine_fuel_association, backref='fuel')
