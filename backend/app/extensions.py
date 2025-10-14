from firebase_admin import initialize_app, firestore

'''Creating DB Instance'''

'''For Initializing firebase app'''
def init_extensions(app):
    initialize_app(app)
    db = firestore.client()
   

    
