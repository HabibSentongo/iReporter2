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

#create a red-flag
@app.route('/api/v1/red-flags', methods=['POST'])
def create_red_flag():
    if not request.json:
        return jsonify({
            'status': 417,
            'error': 'No request data, Provide incident details'
        }), 417
    incident_details = request.get_json()
    if 'created_by' not in incident_details:
        return jsonify({
            'status': 403,
            'error': 'We can\'t identify you, Provide your ID'
        }), 403
    
    incident_title = incident_details.get("incident_title")
    created_by = incident_details.get("created_by")
    location = incident_details.get("location")
    images = incident_details.get("images")
    videos = incident_details.get("videos")
    comment = incident_details.get("comment")

    new_red_flag = Incident(
        incident_details=incident_title,
        created_by= created_by,
        location= location,
        images= images,
        videos= videos,
        comment= comment
    )

    red_flags_list.append(
        new_red_flag.incident_struct('red-flag')
    )
    return jsonify({
        'status': 201,
        'data': [{
            'message': 'Incident {} has been recorded'.format(new_red_flag.incident_id)
        }]
    }), 201