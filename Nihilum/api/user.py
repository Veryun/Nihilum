from flask.views import MethodView
from flask_smorest import Blueprint
from Nihilum.models.user import User
from Nihilum.schema.user import UserSchema, UserPostSchema
from Nihilum.errors import ObjectNotFound

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
        user = User.query.get(user_id)
        if not user:
            raise ObjectNotFound
        return user

    @user_blueprint.response(200)
    def delete(self, user_id):
        user_to_delete = User.query.get(user_id)
        if not user_to_delete:
            raise ObjectNotFound
        user_to_delete.delete()
