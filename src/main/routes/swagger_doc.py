from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from src.settings import API_URL, SWAGGER_URL


swagger_bp = Blueprint("swagger_doc", __name__)


SWAGGER_BP = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "documentation to Account Service"}
)
