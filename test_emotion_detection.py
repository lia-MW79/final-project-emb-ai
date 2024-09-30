from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):

        joy_detection = emotion_detector("I am glad this happened")
        self.assertEqual(joy_detection['dominant_emotion'], 'joy')

        anger_detection = emotion_detector("I am really mad about this")
        self.assertEqual(anger_detection['dominant_emotion'], 'anger')

        disgust_detection = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_detection['dominant_emotion'], 'disgust')

        sadness_detection = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_detection['dominant_emotion'], 'sadness')

        fear_detection = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_detection['dominant_emotion'], 'fear')

unittest.main()
