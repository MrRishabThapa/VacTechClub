from flask import Flask
from firebase_admin import firestore, credentials, initialize_app
import cloudinary

db = None

def create_app():
    app = Flask(__name__)

    '''Initializing Cloudinary App'''
    cloudinary.config(
        cloud_name="do9ertejv",
        api_key="959525144626746",
        api_secret="q8tDQ2d7hzfI6A05QLlwP8m-rKQ",
        secure=True
    )

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

    from app.routes.manage_gallery import gallery_bp
    app.register_blueprint(gallery_bp, url_prefix='/api/gallery')
    
    return app