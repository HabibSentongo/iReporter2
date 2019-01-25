import unittest
from app.views.view import app
import json
from app.models.incident_model import Static_strings
from database.db import DBmigrate


test_db = DBmigrate()


class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        test_db.drop_table('red_flags')
        test_db.drop_table('interventions')
        test_db.drop_table('users')

        test_db.create_tables()

    def test_home_status(self):
        response = self.client.get('/', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        returndata = json.loads(response.data.decode())
        expected = ['Welcome to Sentongo\'s iReporter!',
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
        self.assertEqual(returndata['message'], expected)

    def test_create_without_post_data(self):
        response = json.loads(self.client.post('/api/v2/red-flags',data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],400)
        self.assertEqual(response['error'], Static_strings.error_bad_data)

    def test_create_wothout_User_id(self):
        response = json.loads(self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],400)
        self.assertEqual(response['error'], Static_strings.error_no_id)

    def test_create_good_request(self):
        response = json.loads(self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],201)
        self.assertEqual(response['data'][0]["message"], 'Created record')

    def test_fetch_all_not_empty(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": 1,
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = self.client.get('/api/v2/red-flags', content_type = 'application/json')
        return_data = json.loads(response.data.decode())
        self.assertEqual(return_data['status'], 200)
        self.assertEqual(return_data['data'][0]['comment'], 'kill it')
    
    def test_fetch_all_when_empty(self):
        response = json.loads(self.client.get('/api/v2/red-flags', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], Static_strings.error_empty)

    def test_fetch_specific_when_exists(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.get('/api/v2/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],302)
        self.assertEqual(response['data'][0]['incident_id'], 1)

    def test_fetch_specific_when_not_exist(self):
        response = json.loads(self.client.get('/api/v2/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],404)
        self.assertEqual(response['error'], Static_strings.error_missing)

    def test_edit_location_when_no_request_data(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/location', data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], Static_strings.error_bad_data)

    def test_edit_location_when_no_location_in_data(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/location', data = json.dumps({'created_by': '1'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], Static_strings.error_bad_data)

    def test_edit_location_with_good_request_but_missing_record(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/location', data = json.dumps({'location': 'kampala'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], Static_strings.error_missing)

    def test_edit_location_with_good_request(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.patch('/api/v2/red-flags/1/location', data = json.dumps({'location': 'kampala'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data'][0]['message'],  Static_strings.msg_updated)

    def test_edit_comment_when_no_request_data(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/comment', data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], Static_strings.error_bad_data)

    def test_edit_comment_when_no_comment_in_data(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/comment', data = json.dumps({'created_by': '1'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 400)
        self.assertEqual(response['error'], Static_strings.error_bad_data)

    def test_edit_comment_with_good_request_but_missing_record(self):
        response = json.loads(self.client.patch('/api/v2/red-flags/1/comment', data = json.dumps({'comment': 'its terrible'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], Static_strings.error_missing)

    def test_edit_comment_with_good_request(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.patch('/api/v2/red-flags/1/comment', data = json.dumps({'comment': 'its terrible'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data'][0]['message'], Static_strings.msg_updated)

    def test_delete_good_request(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.delete('/api/v2/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data'][0]['message'], Static_strings.msg_deleted)

    def test_delete_with_missing_id(self):
        self.client.post('/api/v2/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": 1,
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.delete('/api/v2/red-flags/2', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], Static_strings.error_missing)