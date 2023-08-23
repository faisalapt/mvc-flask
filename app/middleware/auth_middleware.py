from ..middleware import *
import datetime
import time

def auth_middleware(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication invalid token",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_time = time.mktime(datetime.datetime.now().timetuple())
            if current_time > data['exp']:
                return {
                    "message" : "Invalid Authentication token",
                    "data" : None,
                    "error" : "Unauthorized"
                }, 401
            current_user=oauth_clients.OauthClient.query.filter_by(client_id=data["client_id"]).first()
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401

        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated