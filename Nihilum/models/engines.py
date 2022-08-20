from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class Engines(db.Model, BaseMixin):
    __tablename__ = "engines"
    engine_class_id = db.Column(db.Integer, db.ForeignKey("engine_class.id"))
    ship = db.relationship("Ship", back_populates="engine")
    current_fuel = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User({self.id}, {self.name})"
