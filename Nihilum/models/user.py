from Nihilum.models import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User({self.id}, {self.name})"

    def save(self):
        db.session.add(self)
        db.session.commit()
