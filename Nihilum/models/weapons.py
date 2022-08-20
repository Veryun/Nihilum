from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class Weapons(db.Model, BaseMixin):
    __tablename__ = "weapons"
    weapon_class_id = db.Column(db.Integer, db.ForeignKey("weapon_class.id"))
    weapon_class = db.relationship("WeaponClass", back_populates="weapons")
    ship = db.relationship("Ship", back_populates="weapons")
    current_ammo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User({self.id}, {self.name})"
