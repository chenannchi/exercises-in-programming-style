import unittest
from io import StringIO
from unittest.mock import patch

# Assuming the functions are in a module named 'hw1_1'
from hw1_1 import remove_stop_words, scan, filter_chars_and_normalize

class TestRemoveStopWords(unittest.TestCase):
    
    
    def test_remove_stop_words(self):
        expected = ["acquaintance","suppose","sure","know"]
        word_list = ["some","acquaintance","or","other","my","dear","i","suppose","i","am","sure","i","do","not","know"]

        result = remove_stop_words("./stop_words.txt")(word_list)
        self.assertEqual(result, expected)
    
if __name__ == "__main__":
    unittest.main()