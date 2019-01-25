from flask import Flask, jsonify, request
from database.db import DBmigrate
from ..models.incident_model import Static_strings

db_obj = DBmigrate()
db_obj.create_tables()
class Endpoints_functions:
    def home(self):
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

    def all_records(self, table_name):
        db_obj.my_cursor.execute(Static_strings.all_records.format(table_name))
        all_records = db_obj.my_cursor.fetchall()

        if all_records:
            return jsonify({
                'status': 200,
                'data': all_records
            }), 200

        return jsonify({
            'status': 404,
            'error': Static_strings.error_empty
        }), 404


    def select_specific(self, table_name, record_id):
        db_obj.my_cursor.execute(Static_strings.selector.format('*',table_name, record_id))
        specific_record = db_obj.my_cursor.fetchall()
        if specific_record:
            return jsonify({
                'status': 302,
                'data': specific_record
            }), 302
        return jsonify({
            'status': 404,
            'error': Static_strings.error_missing
        }), 404


    def create_record(self, table_name):
        if not request.json:
            return jsonify({
                'status': 400,
                'error': Static_strings.error_bad_data
            }), 400
        incident_details = request.get_json()
        if 'created_by' not in incident_details:
            return jsonify({
                'status': 400,
                'error': Static_strings.error_no_id
            }), 400

        location = incident_details.get("location")
        images = incident_details.get("images")
        videos = incident_details.get("videos")
        comment = incident_details.get("comment")
        created_by = incident_details.get("created_by")

        db_obj.my_cursor.execute(Static_strings.creator.format(table_name, comment, created_by, location, images, videos))
        new_id = db_obj.my_cursor.fetchone()
        return jsonify({
            'status': 201,
            'data': [{
                'ID': new_id['incident_id'],
                'message': 'Created record'
            }]
        }), 201


    def edit_column(self, table_name, edit_column, record_id):
        if not request.json:
            return jsonify({
                'status': 400,
                'error': Static_strings.error_bad_data
            }), 400
        new_column_data = request.get_json()
        if edit_column not in new_column_data:
            return jsonify({
                'status': 400,
                'error': Static_strings.error_bad_data
            }), 400

        db_obj.my_cursor.execute(Static_strings.selector.format(record_id, table_name, record_id))
        hold_checked = db_obj.my_cursor.fetchone()


        if hold_checked:
            db_obj.my_cursor.execute(Static_strings.updater.format(table_name, edit_column, new_column_data[edit_column], record_id))
            its_id = db_obj.my_cursor.fetchone()
            return jsonify({
                'status': 200,
                'data': [{
                    'ID': its_id['incident_id'],
                    'message': Static_strings.msg_updated
                }]
            }), 200

        return jsonify({
            'status': 404,
            'error': Static_strings.error_missing
        }), 404


    def delete_record(self, table_name, record_id):
        db_obj.my_cursor.execute(Static_strings.selector.format(record_id, table_name, record_id))
        hold_checked = db_obj.my_cursor.fetchone()

        if hold_checked:
            db_obj.my_cursor.execute(Static_strings.deleter.format(table_name, record_id))
            its_id = db_obj.my_cursor.fetchone()
            return jsonify({
                'status': 200,
                'data': [{
                    'ID': its_id['incident_id'],
                    'message': Static_strings.msg_deleted
                }]
            }), 200

        return jsonify({
            'status': 404,
            'error': Static_strings.error_missing
        }), 404