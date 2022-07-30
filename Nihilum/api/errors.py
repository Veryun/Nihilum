from Nihilum.schema.errors import ErrorSchema
from flask_smorest import Blueprint
from Nihilum.errors import ObjectNotFound

error_blueprint = Blueprint("error", __name__)


@error_blueprint.app_errorhandler(Exception)
@error_blueprint.response(500, schema=ErrorSchema)
def schema_error_handler(e):
    return {"error": "oops!"}


@error_blueprint.app_errorhandler(ObjectNotFound)
@error_blueprint.response(404, schema=ErrorSchema)
def handle_object_not_found(e):
    return {"error": "not found!"}
