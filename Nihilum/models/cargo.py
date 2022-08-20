from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class Cargo(db.Model, BaseMixin):
    __tablename__ = "cargo"

    def __repr__(self):
        return f"User({self.id}, {self.name})"
