from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class CargoHold(db.Model, BaseMixin):
    __tablename__ = "cargo_hold"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ship = db.relationship("ship", backref=db.backref("ship", uselist=False))  # relationship to ship (many to many)
    cargo = db.relationship("ship", backref=db.backref("ship", uselist=False))  # relationship to item (many to many)
    ship_class_id = db.Column(db.Integer, db.ForeignKey('ship_class.id'))
    ship_class = db.relationship("ShipClass", back_populates="ships")

    def __repr__(self):
        return f"User({self.id}, {self.name})"
