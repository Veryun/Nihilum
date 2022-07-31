from Nihilum.models import db


class BaseMixin:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
