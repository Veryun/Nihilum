from Nihilum.models.base import BaseMixin
from Nihilum.models import db
from Nihilum.models.associations import engine_fuel_association, engine_failure_association


class EngineClass(db.Model, BaseMixin):
    __tablename__ = 'engine_class'
    thrust = db.Column(db.Float, nullable=False)
    power_consumption = db.Column(db.Float, nullable=False)
    size = db.Column(db.Integer, nullable=False)  # cubic centimeters
    stability = db.Column(db.Integer, nullable=False)  # d100 chance to fail; on fail blow up
    # How long a ship can travel before another stability check must be made
    burn_length = db.Column(db.Integer, nullable=False)
    # Local or interstellar units
    burn_length_unit = db.Column(db.String, nullable=False)
    # Failure table
    failure_table = db.relationship('engine_failure', secondary=engine_failure_association, backref='engine')
    fuel_sources = db.relationship('fuel', secondary=engine_fuel_association, backref='engine')
