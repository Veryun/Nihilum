from flask.views import MethodView
from flask_smorest import Blueprint
from Nihilum.models.user import User
from Nihilum.schema.user import UserSchema, UserPostSchema
import json

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("")
class UsersEndpoint(MethodView):

    @user_blueprint.arguments(schema=UserPostSchema)
    @user_blueprint.response(200, schema=UserSchema)
    def post(self, user):
        user = User(name=user["name"])
        user.save()
        return user


@user_blueprint.route("/<user_id>")
class UserEndpoint(MethodView):

    @user_blueprint.response(200, schema=UserSchema)
    def get(self, user_id) -> User:
        return User.query.get(user_id)
