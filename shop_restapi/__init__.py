from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from flask_migrate import Migrate

from .ma import ma
from .db import db
from .blacklist import BLACKLIST
from .resources.user import UserRegister, UserLogin, User, TokenRefresh, UserLogout
from .resources.item import Item, ItemList
from .resources.store import Store, StoreList
from config import Config

migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)
    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return decrypted_token["jti"] in BLACKLIST

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        return jsonify(err.messages), 400

    api.add_resource(Store, "/store/<string:name>")
    api.add_resource(StoreList, "/stores")
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(UserRegister, "/register")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UserLogin, "/login")
    api.add_resource(TokenRefresh, "/refresh")
    api.add_resource(UserLogout, "/logout")

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app
