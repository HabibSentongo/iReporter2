from flask import Flask, jsonify, request
from database.db import DBmigrate
from ..controllers.controller import All_fns

app = Flask(__name__)
funct = All_fns()

@app.route('/')
def home():
    return funct.home()

                            #  RED FLAGS


@app.route('/api/v2/red-flags', methods=['GET'])
def all_red_flags():
    return funct.all_records('red_flags')


@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['GET'])
def select_red_flag(red_flag_id):
    return funct.select_specific('red_flags', red_flag_id)


@app.route('/api/v2/red-flags', methods=['POST'])
def create_red_flag():
    return funct.create_record('red_flags')


@app.route('/api/v2/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_location(red_flag_id):
    return funct.edit_column('red_flags', 'location', red_flag_id)


@app.route('/api/v2/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_comment(red_flag_id):
    return funct.edit_column('red_flags', 'comment', red_flag_id)


@app.route('/api/v2/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_record(red_flag_id):
    return funct.delete_record('red_flags', red_flag_id)


                            #   INTERVENTIONS


