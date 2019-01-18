import unittest
from app.views.view import app
from app.models.incident_model import red_flags_list
import json

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        red_flags_list[:] = []

    def test_home_status(self):
        response = self.client.get('/', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        returndata = json.loads(response.data.decode())
        expected = ['Welcome to Sentongo\'s iReporter!',
                    'Endpoints',
                    '01 : GET /api/v1/red-flags',
                    '02 : GET /api/v1/red-flags/<red_flag_id>',
                    '03 : POST /api/v1/red-flags',
                    '04 : PATCH /api/v1/red-flags/<red_flag_id>/location',
                    '05 : PATCH /api/v1/red-flags/<red_flag_id>/comment',
                    '06 : DELETE /api/v1/red-flags/<red_flag_id>']
        self.assertEqual(returndata['message'], expected)

    def test_create_without_post_data(self):
        response = json.loads(self.client.post('/api/v1/red-flags',data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],417)
        self.assertEqual(response['error'], 'No request data, Provide incident details')

    def test_create_wothout_User_id(self):
        response = json.loads(self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],403)
        self.assertEqual(response['error'], 'We can\'t identify you, Provide your ID')

    def test_create_good_request(self):
        response = json.loads(self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],201)
        self.assertEqual(response['data'], [{'message': 'Incident 1 has been recorded'}])

    def test_fetch_all_not_empty(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.get('/api/v1/red-flags', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data'][0]['comment'], 'kill it')
    
    def test_fetch_all_when_empty(self):
        response = json.loads(self.client.get('/api/v1/red-flags', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 204)
        self.assertEqual(response['error'], 'No records yet!')

    def test_fetch_specific_when_exists(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.get('/api/v1/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],302)
        self.assertEqual(response['data'][0]['incident_id'], 1)

    def test_fetch_specific_when_not_exist(self):
        response = json.loads(self.client.get('/api/v1/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'],204)
        self.assertEqual(response['error'], 'No such record')

    def test_edit_location_when_no_request_data(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/location', data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 417)
        self.assertEqual(response['error'], 'No request data, Provide new location')

    def test_edit_location_when_no_location_in_data(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/location', data = json.dumps({'created_by': '1'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 412)
        self.assertEqual(response['error'], 'New info missing, Provide new location')

    def test_edit_location_with_good_request_but_missing_record(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/location', data = json.dumps({'location': 'kampala'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], 'Red-flag record does\'t exist')

    def test_edit_location_with_good_request(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.patch('/api/v1/red-flags/1/location', data = json.dumps({'location': 'kampala'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 202)
        self.assertEqual(response['data'], [{'message': 'Location of record 1 updated to kampala'}] )

    def test_edit_comment_when_no_request_data(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/comment', data = json.dumps({}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 417)
        self.assertEqual(response['error'], 'No request data, Provide new comment')

    def test_edit_comment_when_no_comment_in_data(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/comment', data = json.dumps({'created_by': '1'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 412)
        self.assertEqual(response['error'], 'New info missing, Provide new comment')

    def test_edit_comment_with_good_request_but_missing_record(self):
        response = json.loads(self.client.patch('/api/v1/red-flags/1/comment', data = json.dumps({'comment': 'its terrible'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], 'Red-flag record does\'t exist')

    def test_edit_comment_with_good_request(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.patch('/api/v1/red-flags/1/comment', data = json.dumps({'comment': 'its terrible'}), content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 202)
        self.assertEqual(response['data'], [{'message': 'Comment of record 1 updated to its terrible'}] )

    def test_delete_good_request(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.delete('/api/v1/red-flags/1', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data'], [{'message': 'Record 1 deleted successfully'}])

    def test_delete_with_missing_id(self):
        self.client.post('/api/v1/red-flags', data = json.dumps({
            "incident_title": "omubbi",
            "created_by": "1",
            "location": "gheto",
            "images": "solmon",
            "comment": "kill it"
        }),content_type = 'application/json')
        response = json.loads(self.client.delete('/api/v1/red-flags/2', content_type = 'application/json').data.decode())
        self.assertEqual(response['status'], 404)
        self.assertEqual(response['error'], 'No such record')

    
