from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class Ship(db.Model, BaseMixin):
    __tablename__ = "ship"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("ship", uselist=False))
    ship_class_id = db.Column(db.Integer, db.ForeignKey('ship_class.id'))
    ship_class = db.relationship("ShipClass", back_populates="ships")
    weapons = db.relationship("Weapons", back_populates="ship")
    engine = db.relationship("Engines", back_populates="ship")

    def __repr__(self):
        return f"User({self.id}, {self.name})"
