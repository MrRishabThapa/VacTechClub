from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Firebase
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Helper function to convert Firestore document to dictionary
def event_to_dict(doc):
    data = doc.to_dict()
    data['id'] = doc.id
    return data

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    try:
        # Test Firestore connection
        test_ref = db.collection('health_check').document('test')
        test_ref.set({'timestamp': firestore.SERVER_TIMESTAMP})
        test_ref.delete()
        
        return jsonify({'status': 'healthy', 'message': 'Firebase connection working'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Routes
@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        events_ref = db.collection('events')
        docs = events_ref.stream()
        events = {}
        
        for doc in docs:
            event_data = event_to_dict(doc)
            date = event_data['date']
            if date not in events:
                events[date] = []
            events[date].append(event_data)
        
        return jsonify(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events', methods=['POST'])
def add_event():
    try:
        data = request.json
        required_fields = ['date', 'title', 'description', 'color']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        event_data = {
            'date': data['date'],
            'title': data['title'],
            'description': data.get('description', ''),
            'color': data['color'],
            'created_at': firestore.SERVER_TIMESTAMP
        }
        
        doc_ref = db.collection('events').document()
        doc_ref.set(event_data)
        
        event_data['id'] = doc_ref.id
        return jsonify(event_data), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events/<date>', methods=['GET'])
def get_events_by_date(date):
    try:
        events_ref = db.collection('events')
        query = events_ref.where('date', '==', date)
        docs = query.stream()
        
        events = []
        for doc in docs:
            events.append(event_to_dict(doc))
        
        return jsonify(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        db.collection('events').document(event_id).delete()
        return jsonify({'message': 'Event deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events/batch', methods=['DELETE'])
def delete_events_batch():
    try:
        data = request.json
        event_ids = data.get('event_ids', [])
        
        batch = db.batch()
        for event_id in event_ids:
            doc_ref = db.collection('events').document(event_id)
            batch.delete(doc_ref)
        
        batch.commit()
        return jsonify({'message': f'Deleted {len(event_ids)} events'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add some sample data
@app.route('/api/seed', methods=['POST'])
def seed_data():
    try:
        sample_events = [
            {
                'date': '2024-10-11',
                'title': 'Team Meeting',
                'description': 'Weekly team sync',
                'color': 'blue'
            },
            {
                'date': '2024-10-15',
                'title': 'Project Deadline',
                'description': 'Submit final project',
                'color': 'red'
            },
            {
                'date': '2024-10-20',
                'title': 'Birthday Party',
                'description': 'John\'s birthday celebration',
                'color': 'green'
            }
        ]
        
        for event_data in sample_events:
            doc_ref = db.collection('events').document()
            event_data['created_at'] = firestore.SERVER_TIMESTAMP
            doc_ref.set(event_data)
        
        return jsonify({'message': 'Sample data added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Root route for testing
@app.route('/')
def home():
    return jsonify({
        # 'message': 'Calendar API is running!',
        'endpoints': {
            'health': '/api/health',
            'events': '/api/events',
            'seed_data': '/api/seed (POST)'
        }
    })

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Available endpoints:")
    print("  http://localhost:5000/ - API info")
    print("  http://localhost:5000/api/health - Health check")
    print("  http://localhost:5000/api/events - Get all events")
    print("  http://localhost:5000/api/seed - Add sample data (POST)")
    print("\nFrontend pages:")
    print("  Open admin.html in your browser")
    print("  Open users.html in your browser")
    app.run(debug=True, port=5000, host='0.0.0.0')