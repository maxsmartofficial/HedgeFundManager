import unittest
from Fund import Fund
from Stock import Stock

class TestFund(unittest.TestCase):

    def test_init(self):
        f = Fund()
        self.assertEqual(f.profitWeight + f.riskWeight, 1)

    def test_estimateStock(self):
        f = Fund()
        s = Stock()

        result = f.estimateStock(s)
        self.assertIs(type(result), tuple)

    def test_estimate(self):
        f = Fund()
        s1 = Stock()
        s2 = Stock()
        s3 = Stock()
        stocks = [s1, s2, s3]

        f.estimate(stocks)

    def test_trade(self):
        f = Fund()
        s1 = Stock()
        s2 = Stock()
        s3 = Stock()
        stocks = [s1, s2, s3]

        f.estimate(stocks)
        f.trade()

    def test_totalValue(self):
        f = Fund()

        value = f.totalValue()
        self.assertEqual(value, f.money)
        


if __name__ == '__main__':
    unittest.main()
