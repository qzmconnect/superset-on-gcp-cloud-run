import os

from flask_appbuilder.security.manager import AUTH_OAUTH

ENABLE_PROXY_FIX=True
ROW_LIMIT=5000
SECRET_KEY=os.getenv("SUPERSET_SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SUPERSET_CONNECTION_STRING")
WTF_CSRF_ENABLED=True
CSRF_ENABLED=True


FEATURE_FLAGS = {
    "DASHBOARD_NATIVE_FILTERS": True,
}

AUTH_TYPE=AUTH_OAUTH
AUTH_USER_REGISTRATION=True
AUTH_USER_REGISTRATION_ROLE="Admin"


OAUTH_PROVIDERS = [{
    "name": "google",
    "icon": "fa-google",
    "token_key": "access_token",
    "remote_app": {
        "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
        "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
        "api_base_url": "https://www.googleapis.com/oauth2/v2/",
        "client_kwargs": {"scope": "email profile"},
        "request_token_url": None,
        "access_token_url": "https://oauth2.googleapis.com/token",
        "authorize_url": "https://accounts.google.com/o/oauth2/auth",
        "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
        "authorize_params": {"hd": "qzmarketing.com"}
    }
}]

#SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")
#SQLALCHEMY_DATABASE_URI=os.getenv("SUPERSET_CONNECTION_STRING")