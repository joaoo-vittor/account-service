from flask import jsonify, request, Blueprint
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from src.main.adapter import (
    flask_adapter_registry_user,
    flask_adapter_find_user,
    flask_adapter_update_user,
    flask_adapter_deactivate_user,
    flask_adapter_activate_user,
    flask_adapter_login_user,
)
from src.main.composer import (
    registry_user_composite,
    find_user_composite,
    update_user_composite,
    deactivate_user_composite,
    activate_user_composite,
)
from src.settings import HASH

api_route_bp = Blueprint("api_bp", __name__)


@api_route_bp.route("/api/v1/registry", methods=["POST"])
def register_user():
    """register user route"""

    message = {}

    response = flask_adapter_registry_user(
        request=request, api_route=registry_user_composite()
    )

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {
                "name": response.body.user_name,
                "email": response.body.email,
                "active": response.body.active,
            },
        }

        return jsonify({"data": message}), 201

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_route_bp.route("/api/v1/login", methods=["POST"])
def login_user():
    """register user route"""

    response = flask_adapter_login_user(
        request=request, api_route=find_user_composite()
    )

    if response.status_code < 300:
        if request.args.to_dict():
            password = request.args.to_dict()["password"]
        else:
            password = request.get_json()["password"]

        pwhash = f"{HASH}{response.body.password}"
        valid_pw = check_password_hash(pwhash, password)

        if valid_pw and response.body.active:
            token_de_acesso = create_access_token(
                {
                    "user_id": f"{response.body.id}",
                    "user_name": f"{response.body.user_name}",
                }
            )

            message = {
                "access_token": token_de_acesso,
            }

            return jsonify(message), response.status_code

        return jsonify({"error": {"status": 401, "title": "Unauthorized"}}), 401

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_route_bp.route("/api/v1/user_info", methods=["GET"])
@jwt_required()
def user_info():
    """register user route"""

    response = flask_adapter_find_user(request=request, api_route=find_user_composite())

    if response.status_code < 300:

        if response.body.active == 1:
            message = {
                "type": "users",
                "id": response.body.id,
                "attributes": {
                    "name": response.body.user_name,
                    "email": response.body.email,
                    "active": response.body.active,
                    "type": response.body.type,
                },
            }

        else:
            message = {
                "type": "users",
                "message": "deactivated account.",
            }

        return jsonify(message), response.status_code

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_route_bp.route("/api/v1/update", methods=["PUT"])
@jwt_required()
def update_user():
    """update user route"""

    response = flask_adapter_update_user(
        request=request, api_route=update_user_composite()
    )

    if response.status_code < 300:

        message = {
            "type": "users",
            "updated": response.body,
        }

        return jsonify(message), response.status_code

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_route_bp.route("/api/v1/deactive_user", methods=["PUT"])
@jwt_required()
def deactive_user_user():
    """deactive user user route"""

    response = flask_adapter_deactivate_user(
        request=request, api_route=deactivate_user_composite()
    )

    if response.status_code < 300:

        message = {
            "type": "users",
            "deactivated": response.body,
        }

        return jsonify(message), response.status_code

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_route_bp.route("/api/v1/active_user", methods=["PUT"])
def active_user_user():
    """active user user route"""

    response = flask_adapter_activate_user(
        request=request, api_route=activate_user_composite()
    )

    if response.status_code < 300:

        message = {
            "type": "users",
            "activated": response.body,
        }

        return jsonify(message), response.status_code

    # handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
