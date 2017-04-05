import unittest

class TestGoogleSearchApi(unittest.TestCase):
    def setUp(self):
        self.search_instance=search("Test Driven Development")

    def test_it_does_not_return_None(self):
        self.assertIsNotEqual(search_instance,None,msg="Should not return None")

    def test_search_returns_a_multidimensional_dictionary(self):
        self.assertIsinstance(search_instance,dict,msg="Search request should returns json in dictionary format")






if __name__=='__main__':
    unittest.main()
