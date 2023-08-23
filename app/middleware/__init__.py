from functools import wraps
import jwt
from flask import request, abort, jsonify
from flask import current_app
from ..models import oauth_clients