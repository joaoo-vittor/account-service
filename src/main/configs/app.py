import uuid
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from src.main.routes import api_route_bp
from src.main.routes import SWAGGER_BP
from src.settings import SWAGGER_URL, PRIVATE_KEY
from .revoked_token import BLOCKLIST

api = Flask(__name__)
api.config["SECRET_KEY"] = uuid.uuid4().hex
api.config["JWT_SECRET_KEY"] = PRIVATE_KEY
api.config["JWT_BLACKLIST_ENABLED"] = True
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=2)

jwt = JWTManager(api)
CORS(api)


@jwt.token_in_blocklist_loader
def verifica_token(self, token):
    return token["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({"msg": "Voce esta deslogado."}), 401


api.register_blueprint(SWAGGER_BP, url_perfix=SWAGGER_URL)
api.register_blueprint(api_route_bp)
