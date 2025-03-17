from server import app
import unittest

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_no_text_error(self):
        response = self.app.post('/detect_emotion', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('No text provided', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
