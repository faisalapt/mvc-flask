from flask import Blueprint, request
from .controller.auth_controller import AuthController
from flask_jwt_extended import jwt_required
from .middleware.auth_middleware import auth_middleware

bp = Blueprint('api', __name__)

@bp.route('/client',methods=['POST'])
def client():
    return AuthController.login(request=request)

@bp.route("/protected",methods=["GET"])
@auth_middleware
def protected():
    return AuthController.testAuth()