import unittest
import reversesSentence

class test_reversesSentence(unittest.TestCase):
    def test_words(self):
        self.assertEqual(reversesSentence.reverseSentence("My name is Yuna"), "Yuna is name My")

if __name__ == '__main__':
    unittest.main()