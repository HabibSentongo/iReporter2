from flask import Flask, jsonify, request
from database.db import DBmigrate

app = Flask(__name__)

db_obj = DBmigrate()

db_obj.create_tables()


@app.route('/')
def home():
    return jsonify({'message': ['Welcome to Sentongo\'s iReporter!',
                                'Endpoints',
                                '01 : GET /api/v2/red-flags',
                                '02 : GET /api/v2/red-flags/<red_flag_id>',
                                '03 : POST /api/v2/red-flags',
                                '04 : PATCH /api/v2/red-flags/<red_flag_id>/location',
                                '05 : PATCH /api/v2/red-flags/<red_flag_id>/comment',
                                '06 : DELETE /api/v2/red-flags/<red_flag_id>'
                                '07 : GET /api/v2/red-flags',
                                '08 : GET /api/v2/red-flags/<red_flag_id>',
                                '09 : POST /api/v2/red-flags',
                                '10 : PATCH /api/v2/red-flags/<red_flag_id>/location',
                                '11 : PATCH /api/v2/red-flags/<red_flag_id>/comment',
                                '12 : DELETE /api/v2/red-flags/<red_flag_id>']
                    })

# fetch all red-flags


@app.route('/api/v2/red-flags', methods=['GET'])
def all_red_flags():

    get_redflags = "SELECT * FROM red_flags;"
    db_obj.my_cursor.execute(get_redflags)
    all_red_flags = db_obj.my_cursor.fetchall()

    if all_red_flags:
        return jsonify({
            'status': 200,
            'data': all_red_flags
        }), 200

    return jsonify({
        'status': 404,
        'error': 'No records yet!'
    }), 404

# fetch specific red-flag


@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['GET'])
def select_red_flag(red_flag_id):
    get_specific = "SELECT * FROM red_flags WHERE incident_id = {};".format(red_flag_id)
    db_obj.my_cursor.execute(get_specific)
    specific_redflag = db_obj.my_cursor.fetchall()
    if specific_redflag:
        return jsonify({
            'status': 302,
            'data': specific_redflag
        }), 302
    return jsonify({
        'status': 404,
        'error': 'No such record'
    }), 404

# create a red-flag


@app.route('/api/v2/red-flags', methods=['POST'])
def create_red_flag():
    if not request.json:
        return jsonify({
            'status': 400,
            'error': 'No request data, Provide incident details'
        }), 400
    incident_details = request.get_json()
    if 'created_by' not in incident_details:
        return jsonify({
            'status': 400,
            'error': 'We can\'t identify you, Provide your ID'
        }), 400

    location = incident_details.get("location")
    images = incident_details.get("images")
    videos = incident_details.get("videos")
    comment = incident_details.get("comment")
    created_by = incident_details.get("created_by")

    new_red_flag = "INSERT INTO red_flags(comment,created_by, location, images, videos)\
    VALUES ('{}',{},'{}','{}','{}') RETURNING incident_id;".format(comment, created_by, location, images, videos)
    db_obj.my_cursor.execute(new_red_flag)
    new_id = db_obj.my_cursor.fetchone()
    return jsonify({
        'status': 201,
        'data': [{
            'ID': new_id['incident_id'],
            'message': 'Created red-flag record'
        }]
    }), 201

#edit record location
@app.route('/api/v2/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_location(red_flag_id):
    if not request.json:
        return jsonify({
            'status': 404,
            'error': 'No request data, Provide new location'
        }), 404
    new_location = request.get_json()
    if 'location' not in new_location:
        return jsonify({
            'status': 404,
            'error': 'New info missing, Provide new location'
        }), 404

    checker = "SELECT incident_id FROM red_flags WHERE incident_id = {};".format(red_flag_id)
    updater = "UPDATE red_flags SET location = '{}' WHERE incident_id = {} RETURNING incident_id;".format(new_location['location'], red_flag_id)

    db_obj.my_cursor.execute(checker)
    hold_checked=db_obj.my_cursor.fetchone

    if hold_checked:
        db_obj.my_cursor.execute(updater)
        its_id = db_obj.my_cursor.fetchone()
        return jsonify({
            'status': 200,
            'data': [{
                'ID': its_id['incident_id'],
                'message': 'Updated red-flag record location'
            }]
        }), 200

    return jsonify({
        'status': 404,
        'error': 'Red-flag record does\'t exist'
    }), 404

#edit record comment
@app.route('/api/v2/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_comment(red_flag_id):
    if not request.json:
        return jsonify({
            'status': 404,
            'error': 'No request data, Provide new comment'
        }), 404
    new_comment = request.get_json()
    if 'comment' not in new_comment:
        return jsonify({
            'status': 404,
            'error': 'New info missing, Provide new comment'
        }), 404

    checker = "SELECT incident_id FROM red_flags WHERE incident_id = {};".format(red_flag_id)
    updater = "UPDATE red_flags SET comment = '{}' WHERE incident_id = {} RETURNING incident_id;".format(new_comment['comment'], red_flag_id)

    db_obj.my_cursor.execute(checker)
    hold_checked=db_obj.my_cursor.fetchone()

    if hold_checked:
        db_obj.my_cursor.execute(updater)
        its_id = db_obj.my_cursor.fetchone()
        return jsonify({
            'status': 200,
            'data': [{
                'ID': its_id['incident_id'],
                'message': 'Updated red-flag record comment'
            }]
        }), 200

    return jsonify({
        'status': 404,
        'error': 'Red-flag record does\'t exist'
    }), 404

#delete a record
@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_record(red_flag_id):
    checker = "SELECT incident_id FROM red_flags WHERE incident_id = {};".format(red_flag_id)
    deleter = "DELETE FROM red_flags WHERE incident_id = {} RETURNING incident_id;".format(red_flag_id)

    db_obj.my_cursor.execute(checker)
    hold_checked=db_obj.my_cursor.fetchone()

    if hold_checked:
        db_obj.my_cursor.execute(deleter)
        its_id = db_obj.my_cursor.fetchone()
        return jsonify({
            'status': 200,
            'data': [{
                'ID': its_id['incident_id'],
                'message': 'intervention record has been deleted'
            }]
        }), 200

    return jsonify({
        'status': 404,
        'error': 'No such record'
    }), 404
