from ..models import *
class OauthClient(db.Model):
    id = db.Column(db.String(36), primary_key=True,default=str(uuid.uuid1))
    name = db.Column(db.String(255),nullable=True)
    client_id = db.Column(db.String(48), unique=True, nullable=False)
    client_secret = db.Column(db.String(120), nullable=False)
    client_type = db.Column(db.String(40), default='public')
    grant_types = db.Column(db.String(120))
    redirect_uris = db.Column(db.String(2000))
    default_scope = db.Column(db.String(2000))

    def __init__(self, client_id, client_secret, client_type='public', grant_types=None, redirect_uris=None, default_scope=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_type = client_type
        self.grant_types = grant_types
        self.redirect_uris = redirect_uris
        self.default_scope = default_scope