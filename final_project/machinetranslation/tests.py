import unittest

from translator import french_to_english, english_to_french

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test Hello to Bonjour
    def test2(self):
        self.assertNotEqual(english_to_french(None),'Bonjour')  # test Null
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test Bonjour to Hello
    def test2(self):  
        self.assertNotEqual(french_to_english(None),'Hello')  # test Null
        
unittest.main()