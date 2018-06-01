from flask import Blueprint
from flask_restful import Api
from app.resource.user import UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# route
api.add_resource(UserResource, '/user')