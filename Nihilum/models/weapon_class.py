from Nihilum.models.base import BaseMixin
from Nihilum.models import db
from Nihilum.models.ammo import AmmoType
import enum


class WeaponSize(enum.Enum):
    small = 1
    medium = 2
    large = 3


class WeaponClass(db.Model, BaseMixin):
    __tablename__ = "weapon_class"
    size = db.Column(db.Enum(WeaponSize), nullable=False)
    power_consumption = db.Column(db.Integer, nullable=False)
    max_ammo_capacity = db.Column(db.Integer, nullable=False)
    ammo_type = db.Column(db.Enum(AmmoType), nullable=False)
    fire_rate = db.Column(db.Integer, nullable=False)
    range = db.Column(db.Integer, nullable=False)
    weapons = db.relationship("Weapons", back_populates="ship")

    def __repr__(self):
        return f"User({self.id}, {self.name})"
