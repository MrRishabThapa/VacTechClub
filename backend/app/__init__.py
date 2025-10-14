from flask import Flask
from firebase_admin import credentials
from .extensions import init_extensions

def create_app():
    app = Flask(__name__)

    '''Initialize all the necessary extensions'''
    cred = credentials.Certificate("firebase-secret-key.json")
    init_extensions(cred)

    '''Register Blueprints'''
# for managing events 
    from app.routes.manage_events import events_bp 
    app.register_blueprint(events_bp, url_prefix='/api/events')


    return app
    
    