import unittest
from first import Person, scrape
from Exception import DataException

class TestScrape(unittest.TestCase):
        
        global Ayush
        Bismita = Person('biscuit.2510','Bismita Guha', ['IMG'], 'XYZ' ) 

        def test_username(self):
                self.assertEqual('biscuit.2510', Bismita.username)

        def test_name(self):
                self.assertEqual('Bismita Guha', Bismita.name)

        def test_city(self):
                self.assertEqual('XYZ', Bismita.city)

        def test_work(self):
                self.assertEqual(['IMG'], Bismita.work)
        
        global Error
        Error = Person()
        
        def test_work_null(self):
                with self.assertRaises(Exception):
                Error.work
        
        def test_username_null(self):
                with self.assertRaises(Exception):
                Error.username

        def test_invalid(self):
                scrape('swapnil.negi09')
                self.assertEqual('My name is Swapnil Negi and my current city is Roorkee', scrap('swapnil.negi09'))
            
if __name__ == '__main__':
    unittest.main()
