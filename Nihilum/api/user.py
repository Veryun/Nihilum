from flask.views import MethodView
from flask_smorest import Blueprint


user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("")
class UserEndpoint(MethodView):

    @user_blueprint.response(200)
    def get(self) -> str:
        return "Hello, world!"
