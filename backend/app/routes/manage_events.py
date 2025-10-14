from flask import Blueprint, jsonify, request, current_app

events_bp = Blueprint('events', __name__)

@events_bp.route('/')
def get_all_events():
    try:
        db = current_app.config['db']
        events_ref = db.collection('Events')

        events = [{'id':docs.id, **docs.to_dict()} for docs in events_ref.stream()]
        return jsonify({'msg':'sucessfully fetched all events','events': events}), 200
    
    except Exception as e:
        return jsonify({'msg':'Internal Server error', 'error': str(e)})
    
@events_bp.route('/sample_event', methods=['POST'])
def enter_sample_event():
    try:
        db = current_app.config['db']
       
        sample_events = [
        {
            "title": "Tech Conference",
            "desc": "A conference about emerging tech and AI.",
            "on_date": "2025-12-12",
            "organizers": "TechWorld Inc.",
            "color": "#8D33FF"
        },
        {
            "title": "Art Expo",
            "desc": "Local artists showcase their artwork.",
            "on_date": "2025-11-05",
            "organizers": "City Art Council",
            "color": "#33C1FF"
        }]

        for event in sample_events:
            doc_ref = db.collection('Events').document()
            doc_ref.set({
                "title": event['title'],
                "desc": event['desc'],
                "on_date": event['on_date'],
                "organizers": event['organizers'],
                "color": event['color']
            })
        return jsonify({'msg':'Sucessfully created sample events'}), 201
    except Exception as e:
        return jsonify({'msg':'Internal Server error', 'error': str(e)})
    
@events_bp.route('/get-event/<id>')
def get_event_by_id(id):
    try:
        db = current_app.config['db']
       
        exsisting_document = db.collection('Events').document(id).get()

        if not exsisting_document.exists:
            return jsonify({'msg': 'Missing event, event might have been deleted'}), 404
        event = {'id': exsisting_document.id, **exsisting_document.to_dict()}
    
        return jsonify({'msg':'Sucessfully fetched the event', 'event': event}), 200
    except Exception as e:
        return jsonify({'msg':'Internal Server error', 'error': str(e)})
    

@events_bp.route('/add-event', methods=["POST"])
def add_event():
    try:
        db = current_app.config['db']
        data = request.json

        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ["title", "desc", "on_date", "organizers", "color"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        doc_ref = db.collection('events').document() 
        doc_ref.set({
            "title": data["title"],
            "desc": data["desc"],
            "on_date": data["on_date"],
            "organizers": data["organizers"],
            "color": data["color"]
        })

        return jsonify({'msg':'Sucessfully created the event'}), 201
    
    except Exception as e:
        return jsonify({'msg':'Internal Server error', 'error': str(e)})

