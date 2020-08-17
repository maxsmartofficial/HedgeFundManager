import unittest
from World import World

class TestWorld(unittest.TestCase):

    def test_init(self):
        w = World(100, 100)
        
        self.assertEqual(len(w.stocks), 100)
        self.assertEqual(len(w.stocks), 100)

    def test_nextDay(self):
        w = World(100, 100)

        w.nextDay()

    def test_nextDay_noStocks(self):
        w = World(0, 100)

        w.nextDay()

    def test_nextDay_noFunds(self):
        w = World(100, 0)
        
        w.nextDay()

    def test_run(self):
        w = World(100, 100)

        w.run(10)

if __name__ == '__main__':
    unittest.main()
