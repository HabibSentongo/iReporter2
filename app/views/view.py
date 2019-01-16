from flask import Flask, jsonify, request
from app.models.incident_model import red_flags_list, Incident

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message' : ['Welcome to Sentongo\'s iReporter!',
    'Endpoints',
    '01 : GET /api/v1/red-flags',
    '02 : GET /api/v1/red-flags/<red_flag_id>',
    '03 : POST /api/v1/red-flags',
    '04 : PATCH /api/v1/red-flags/<red_flag_id>/location',
    '05 : PATCH /api/v1/red-flags/<red_flag_id>/comment',
    '06 : DELETE /api/v1/red-flags/<red_flag_id>']
    })

#fetch all red-flags
@app.route('/api/v1/red-flags', methods=['GET'])
def all_red_flags():
    if len(red_flags_list) > 0:
        return jsonify({
            'status': 200,
            'data': red_flags_list
        }), 200

    return jsonify({
        'status': 204,
        'error': 'No records yet!'
    }), 200

#fetch specific red-flag
@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['GET'])
def select_red_flag(red_flag_id):
    for record in red_flags_list:
        if record['incident_id'] == red_flag_id:
            return jsonify({
                'status': 302,
                'data': [record]
            }),302
    return jsonify({
        'status': 204,
        'error': 'No such record'
    }), 200