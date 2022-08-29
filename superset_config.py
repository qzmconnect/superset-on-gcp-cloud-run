import os

from flask_appbuilder.security.manager import AUTH_OAUTH, AUTH_DB, AUTH_OID
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SUPERSET_CONNECTION_STRING")