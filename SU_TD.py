#---setUp and tearDown---#
#overview example
import unittest

class SomeTests(unittest.TestCase):
    def setUp(self):
        #set up whatever you want and it re-runs for every test
        pass

    def some_test1(self):
        pass

    def some_dtest2(self):
        pass

    def tearDown(self):
        #take down everything here
        #you dont always have to do this in all situations
        pass