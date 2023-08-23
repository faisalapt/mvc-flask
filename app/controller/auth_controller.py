from ..controller import *
from ..models.oauth_clients import OauthClient
from app import app


class AuthController(BaseController):
    def login(request: Request):
        client_id = request.form.get('client_id')
        client_secret = request.form.get('client_secret')

        oauth_client = OauthClient.query.filter_by(client_id=client_id).first()

        if oauth_client is None:
            return BaseController.error(error_status="ERROR.RESOURCE_NOT_FOUND",message="User Not Found",code=404)

        # Validate client credentials
        if client_secret != oauth_client.client_secret:
            return BaseController.error(error_status="ERROR.INVALID_CREDENTIAL",message="Invalid credential",code=401)

        # Create a JWT token
        custom_claim = {"client_id" : oauth_client.client_id}
        access_token = create_access_token(identity=client_id,expires_delta=app.config['JWT_EXPIRATION_DELTA'],additional_claims=custom_claim)

        return jsonify({'access_token': access_token,"expires_in": int(app.config['JWT_EXPIRATION_DELTA'].total_seconds())}), 200
    
    def testAuth():
        return BaseController.success(message="success",data=None)