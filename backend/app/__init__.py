from flask import Flask
from firebase_admin import firestore, credentials, initialize_app

db = None

def create_app():
    app = Flask(__name__)

    '''Initialzing Firebase app'''
    cred = credentials.Certificate('supersecret.json')
    initialize_app(cred)
    db = firestore.client()

    '''Attaching DB Config'''
    app.config['db'] = db


    '''Registering Blueprints'''
    from app.routes.manage_events import events_bp
    app.register_blueprint(events_bp)

    from app.routes.leaderboard import leaderboard_bp
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    
    return app