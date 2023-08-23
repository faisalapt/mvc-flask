from .base_controller import BaseController
from flask import request as Request, jsonify
from flask_jwt_extended import create_access_token
from .auth_controller import AuthController