import unittest
import sys

from app import create_app, db
from app.models import Student


test_app = create_app('test')


def fake_records(n):
    for i in range(n):
        e = Student(name=f'name{i}', age=i, address=f'address{i}')
        db.session.add(e)
    db.session.commit()


class TestHello(unittest.TestCase):
    url = '/'

    def test_default(self):
        with test_app.test_client() as client:
            resp = client.get(self.url)
            self.assertEqual(resp.get_data(as_text=True), 'Hello, World!')


class TestShowStudents(unittest.TestCase):
    url = '/student/'

    def setUp(self):
        with test_app.app_context():
            db.create_all()

    def tearDown(self):
        with test_app.app_context():
            db.drop_all()

    def test_default(self):
        with test_app.test_client() as client:
            resp = client.get(self.url)
            json_data = resp.get_json()
            self.assertTrue(json_data['success'])


class TestAddStudent(unittest.TestCase):
    url = '/student/add'

    def setUp(self):
        with test_app.app_context():
            db.create_all()

    def tearDown(self):
        with test_app.app_context():
            db.drop_all()

    def test_default(self):
        with test_app.test_client() as client:
            resp = client.get(self.url, query_string={
                'name': 'foo',
                'age': 18,
                'address': 'Beijing',
            })
            json_data = resp.get_json()
            self.assertTrue(json_data['success'])


if __name__ == '__main__':
    if sys.argv[1] == 'fake_records':
        fake_records(20)
