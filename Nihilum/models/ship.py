from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class Ship(db.Model, BaseMixin):
    __tablename__ = "ship"

    def __repr__(self):
        return f"User({self.id}, {self.name})"
