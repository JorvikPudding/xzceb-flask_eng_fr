import unittest

from translator import french_to_english, english_to_french

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test Hello to Bonjour
        self.assertIsNone(english_to_french(None))  # test Null
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test Bonjour to Hello
        self.assertIsNone(french_to_english(None))  # test Null
        
unittest.main()