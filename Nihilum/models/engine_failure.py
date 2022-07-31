from Nihilum.models.base import BaseMixin
from Nihilum.models import db
from Nihilum.models.associations import engine_failure_association


class EngineFailure(db.Model, BaseMixin):
    effect = db.Column(db.String, nullable=False)
    engines = db.relationship('engine', secondary=engine_failure_association, backref='engine_failure')
