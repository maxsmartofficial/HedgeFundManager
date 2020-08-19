from numpy import random


class Stock:
    def __init__(self):

        self.price = 10000  # This is how prices work trust me

        # Risk and 'profit' are percentage increase per day
        self.profit = random.random() - 0.5 # Mean increase
        self.risk = random.random() # Standard deviation

    def nextDay(self):
        
        # Update price
        increasePercentage = random.normal(self.profit, self.risk)
        increaseProportion = 1 + (increasePercentage / 100)
        self.price = int(self.price * increaseProportion)
        
