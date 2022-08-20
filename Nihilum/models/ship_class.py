from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class ShipClass(db.Model, BaseMixin):
    __tablename__ = "ship_class"
    ship_size = db.Column(db.Integer, nullable=False)
    max_engine_size = db.Column(db.Integer, nullable=False)
    min_engine_size = db.Column(db.Integer, nullable=False)
    small_external_mount_points = db.Column(db.Integer, nullable=False)
    medium_external_mount_points = db.Column(db.Integer, nullable=False)
    large_external_mount_points = db.Column(db.Integer, nullable=False)
    hull_class = db.Column(db.Integer, nullable=False)  # Armor class
    durability = db.Column(db.Integer, nullable=False)  # hit points
    ships = db.relationship("Ship", back_populates="ship_class")

    def __repr__(self):
        return f"User({self.id}, {self.name})"
