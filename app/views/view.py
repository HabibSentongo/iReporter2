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

