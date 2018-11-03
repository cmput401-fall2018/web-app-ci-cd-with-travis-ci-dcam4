import unittest
from service import Service
from mock import patch

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()
        
    @patch('service.Service.bad_random')
    def test_bad_random(self, mock_bad_random):
        mock_bad_random.return_value = 20
        
        #check to see if mock method works
        self.assertEqual(self.service.bad_random(), 20)
    
    @patch('service.Service.bad_random')
    def test_divide(self, mock_bad_random):
        mock_bad_random.return_value = 20
        
        #positive
        self.assertEqual(self.service.divide(5), 4)
        
        #zero
        with self.assertRaises(ZeroDivisionError):
            self.service.divide(0)
        
        #negative
        self.assertEqual(self.service.divide(-2), -10)
    
    
    def test_abs_plus(self):
    
        #negative
        self.assertEqual(self.service.abs_plus(-5), 6)
        
        #zero
        self.assertEqual(self.service.abs_plus(0), 1)
        
        #positive
        self.assertEqual(self.service.abs_plus(5), 6)
        
        
    @patch('service.Service.bad_random')
    def test_complicated_function(self, mock_bad_random):
        mock_bad_random.return_value = 20
        
        #test mod with a 0 result
        self.assertEqual(self.service.complicated_function(5), (4,0))
        
        mock_bad_random.return_value = 9
        #test mod with a non zero result
        self.assertEqual(self.service.complicated_function(3), (3,1))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()