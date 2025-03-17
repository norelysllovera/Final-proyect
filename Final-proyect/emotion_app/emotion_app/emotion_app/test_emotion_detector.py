import unittest
from emotion_detector import emotion_predictor

class TestEmotionDetector(unittest.TestCase):

    def test_happy_emotion(self):
        text = "I'm so happy and excited today!"
        result = emotion_predictor(text)
        self.assertIn('joy', result)

    def test_sad_emotion(self):
        text = "I feel sad and down."
        result = emotion_predictor(text)
        self.assertIn('sadness', result)

if __name__ == '__main__':
    unittest.main()
