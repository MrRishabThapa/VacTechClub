from flask import Blueprint, request, jsonify
from extensions import db

events_bp = Blueprint('event', __name__)

events_bp.route('/get-all-events', methods=['GET'])
def get_all_events():
    try:
        events_ref = db.collection('Events')
        events = [doc.to_dict() | {"id": doc.id} for doc in events_ref.stream()]
        
        return jsonify({
            'msg': 'Sucessfully fetched all events', 
            'events': events}), 200
    
    except Exception as e:
        return jsonify({
            'msg': 'Internal server error',
            'error': str(e)}), 500