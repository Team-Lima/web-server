"""
configuration file for setting up the google oauth2 authentication
"""
import os


# TODO: Check client_id and Client_secret details
class Auth:
    CLIENT_ID = ('688061596571-3c13n0uho6qe34hjqj2apincmqk86ddj'
                '.apps.googleusercontent.com')
    CLIENT_SECRET = 'JXf7Ic_jfCam1S7lBJalDyPZ'
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'


# TODO: determine application name from google dev console
class Config:
    APP_NAME = "NeuralGuide"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "something_secret"

