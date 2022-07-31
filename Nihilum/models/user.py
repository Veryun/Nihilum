from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class User(db.Model, BaseMixin):
    __tablename__ = "user"

    def __repr__(self):
        return f"User({self.id}, {self.name})"
