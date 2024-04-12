import unittest
from manage import app

class TestApp(unittest.TestCase):
    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.get_json(), {'message': 'Hello, World!'})

