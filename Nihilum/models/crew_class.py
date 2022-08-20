from Nihilum.models.base import BaseMixin
from Nihilum.models import db


class CrewClass(db.Model, BaseMixin):
    __tablename__ = "crew_class"

    def __repr__(self):
        return f"User({self.id}, {self.name})"
