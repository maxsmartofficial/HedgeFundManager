import unittest
from Stock import Stock

class TestStock(unittest.TestCase):

    def test_init(self):
        s = Stock()
        
        self.assertTrue(0 <= s.profit <= 1 and 0 <= s.risk <= 1)

    def test_nextDay(self):
        s = Stock()

        s.nextDay()

if __name__ == '__main__':
    unittest.main()
