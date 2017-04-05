import unittest
from functions import GoogleSearchApi as gsa

class TestGoogleSearchApi(unittest.TestCase):
    def setUp(self):
        self.search_instance=gsa.search("Test Driven Development")

    def test_it_does_not_return_None(self):
        self.assertNotEqual(self.search_instance,None,msg="Should not return None")

    def test_search_returns_a_multidimensional_dictionary(self):
        self.assertTrue(isinstance(self.search_instance,dict),msg="Search request should returns json in dictionary format")






if __name__=='__main__':
    unittest.main()
