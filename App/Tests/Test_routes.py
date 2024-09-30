import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_signup(self):
        response = self.app.post('/signup', json={'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.app.post('/login', json={'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
  
