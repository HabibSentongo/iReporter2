from flask import Flask, jsonify, request
from database.db import DBmigrate
from ..controllers.controller import Endpoints_functions

app = Flask(__name__)
endpoint_function = Endpoints_functions()

@app.route('/')
def home():
    return endpoint_function.home()

                            #  RED FLAGS


@app.route('/api/v2/red-flags', methods=['GET'])
def all_red_flags():
    return endpoint_function.all_records('red_flags')


@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['GET'])
def select_red_flag(red_flag_id):
    return endpoint_function.select_specific('red_flags', red_flag_id)


@app.route('/api/v2/red-flags', methods=['POST'])
def create_red_flag():
    return endpoint_function.create_record('red_flags')


@app.route('/api/v2/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_location(red_flag_id):
    return endpoint_function.edit_column('red_flags', 'location', red_flag_id)


@app.route('/api/v2/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_comment(red_flag_id):
    return endpoint_function.edit_column('red_flags', 'comment', red_flag_id)


@app.route('/api/v2/red-flags/<int:red_flag_id>/status', methods=['PATCH'])
def edit_status(red_flag_id):
    return endpoint_function.edit_column('red_flags', 'status', red_flag_id)


@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_record(red_flag_id):
    return endpoint_function.delete_record('red_flags', red_flag_id)


                            #   INTERVENTIONS


@app.route('/api/v2/interventions', methods=['GET'])
def all_interventions():
    return endpoint_function.all_records('interventions')


@app.route('/api/v2/interventions/<int:intervention_id>', methods=['GET'])
def select_intervention(intervention_id):
    return endpoint_function.select_specific('interventions', intervention_id)


@app.route('/api/v2/interventions', methods=['POST'])
def create_intervention():
    return endpoint_function.create_record('interventions')


@app.route('/api/v2/interventions/<int:intervention_id>/location', methods=['PATCH'])
def edit_inter_location(intervention_id):
    return endpoint_function.edit_column('interventions', 'location', intervention_id)


@app.route('/api/v2/interventions/<int:intervention_id>/comment', methods=['PATCH'])
def edit_inter_comment(intervention_id):
    return endpoint_function.edit_column('interventions', 'comment', intervention_id)


@app.route('/api/v2/interventions/<int:intervention_id>/status', methods=['PATCH'])
def edit_inter_status(intervention_id):
    return endpoint_function.edit_column('interventions', 'status', intervention_id)


@app.route('/api/v2/interventions/<int:intervention_id>', methods=['DELETE'])
def delete_inter_record(intervention_id):
    return endpoint_function.delete_record('interventions', intervention_id)