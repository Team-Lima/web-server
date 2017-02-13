"""
auth.py will provide an abstraction on OAuth2 to be used in server.py for authenticating users to the application server
"""
from flask_oauthlib.provider import OAuth2Provider
oauth = OAuth2Provider()


def create_auth_app(app):
    """
    :param app: A Flask application without OAuth2 authentication enabled
    :return: A Flask application with OAuth2 capabilities
    """
    oauth.init_app(app)
    return app

