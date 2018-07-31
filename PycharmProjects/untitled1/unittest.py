#encoding = utf - 8
import unittest
import random

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.sep = range(10)

    def runTest(self):
        element =random.choice(self.sep)

        self.assertTrue(element in self.sep)

class TestDictValueFormatFunction(unittest.TestCase):
    def setUp(self):
        self.sep = range(10)

        def test_shuffle(self):
            random.shuffle(self.sep)
            self.sep.sort()
            self.asserEqual(self.sep,range(10))

            self.asserEqual(TypeError,random.shuffle,(1,2,3))

if __name__=='main':
    unittest.main()
