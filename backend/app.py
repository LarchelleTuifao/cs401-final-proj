
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
FILES = {
    'events': os.path.join(BASE_DIR, 'events.json'),
    'businesses': os.path.join(BASE_DIR, 'businesses.json'),
    'opportunities': os.path.join(BASE_DIR, 'funding.json'),
}

# Helper function
def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# Events API
@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(load_data(FILES['events']))

@app.route('/api/events', methods=['POST'])
def add_event():
    event = request.get_json()
    if not event:
        return jsonify({'error': 'Invalid data'}), 400
    events = load_data(FILES['events'])
    events.append(event)
    save_data(FILES['events'], events)
    return jsonify({'message': 'Event added'}), 201

# Businesses API
@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    return jsonify(load_data(FILES['businesses']))

@app.route('/api/businesses', methods=['POST'])
def add_business():
    business = request.get_json()
    if not business:
        return jsonify({'error': 'Invalid data'}), 400
    businesses = load_data(FILES['businesses'])
    businesses.append(business)
    save_data(FILES['businesses'], businesses)
    return jsonify({'message': 'Business added'}), 201

# Funding Opportunities API
@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    return jsonify(load_data(FILES['opportunities']))

@app.route('/api/opportunities', methods=['POST'])
def add_opportunity():
    opportunity = request.get_json()
    if not opportunity:
        return jsonify({'error': 'Invalid data'}), 400
    opportunities = load_data(FILES['opportunities'])
    opportunities.append(opportunity)
    save_data(FILES['opportunities'], opportunities)
    return jsonify({'message': 'Opportunity added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

