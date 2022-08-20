from Nihilum.models import db

engine_fuel_association = db.Table(
    'engine_fuel_association',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('engine_class_id', db.Integer, db.ForeignKey('engine_class.id')),
    db.Column('fuel_id', db.Integer, db.ForeignKey('fuel.id')),

)

engine_failure_association = db.Table(
    'engine_failure_association',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('engine_class_id', db.Integer, db.ForeignKey('engine_class.id')),
    db.Column('engine_failure_id', db.Integer, db.ForeignKey('engine_failure.id')),
    db.Column('effect_chance', db.Integer),
)
