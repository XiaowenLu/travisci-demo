import unittest,json

from main import app


class FlaskTestCase(unittest.TestCase): #inherit the TestCase from unittest class
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code,401,'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data)
        self.assertEqual(resp['answer'],35,'Multiply endpoint failed known answer 7*5 = 35')


    # TODO DEFINE TWO MORE TESTS ON THE END POINTS
    def test_toppercase(self):
        response = self.app.get('/touppercase?s=test')
        self.assertEqual(response.data, "TEST", "Toppercase failed known answer toppercase(test) = TEST")



if __name__ == '__main__':
    unittest.main()
