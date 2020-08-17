from Fund import Fund
from Stock import Stock

class World:
    def __init__(self, num_stocks, num_funds):
        self.stocks = []
        self.funds = []

        # Initialise stocks and funds
        for i in range(num_stocks):
            r = Stock()
            self.stocks.append(r)

        for i in range(num_funds):
            f = Fund()
            self.funds.append(f)

    def run(self, days):
        """Run simulation for a given number of days"""
        for i in range(days):
            self.nextDay()

    def nextDay(self):
        for s in self.stocks:
            s.nextDay()

        for f in self.funds:
            # Reevaluate stocks if necessary
            f.estimate(self.stocks)
            # Make trades
            f.trade()
