from Nihilum.models.base import BaseMixin
from Nihilum.models import db
import enum


class AmmoType(enum.Enum):
    pass


class Ammo(db.Model, BaseMixin):
    __tablename__ = "ammo"
    range_mod = db.Column(db.Integer, nullable=False)
    ammo_type = db.Column(db.Enum(AmmoType), nullable=False)

    def __repr__(self):
        return f"User({self.id}, {self.name})"
