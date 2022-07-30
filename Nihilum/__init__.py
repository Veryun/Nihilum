from flask import Flask
from Nihilum.api.user import user_blueprint
from Nihilum.api.errors import error_blueprint
from Nihilum.models import db

app = Flask(__name__)

app.config.from_object('config')
app.register_blueprint(user_blueprint)
app.register_blueprint(error_blueprint)
db.init_app(app)
