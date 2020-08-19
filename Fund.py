from numpy import random
import math

class Fund:
    def __init__(self):

        self.money = 1000000000 # Like £10,000,000 or something

        # How skilled the fund manager is
        self.profitSkill = random.randint(1,10)
        self.riskSkill = random.randint(1,10)

        # Preference for 'profit'/risk
        self.profitWeight = random.random()
        self.riskWeight = 1 - self.profitWeight

        self.stocks = {}

        self.cache_stockEstimates = {}
        
    def estimateStock(self, stock):

        # Assumes estimates are Gaussian distributed from true value
        if stock in self.cache_stockEstimates:
            return(self.cache_stockEstimates[stock])
        else:
            estimatedProfit = random.normal(stock.profit, (10 - self.profitSkill) / 10)
            estimatedRisk = random.normal(stock.risk, (10 - self.riskSkill) / 10)

            result = (estimatedProfit, estimatedRisk)
            
            # Cache result
            self.cache_stockEstimates[stock] = result

            return(result)

    def estimate(self, stocks):

        for s in stocks:
            self.estimateStock(s)

    def trade(self):
        # Find best stocks
        # If there's any money left, buy
        bestStock = None
        bestValue = -math.inf
        for s in self.cache_stockEstimates:
            stockEstimate = self.cache_stockEstimates[s]
            profit = stockEstimate[0]
            risk = stockEstimate[1]

            # Calculate value based on risk profile
            value = profit * self.profitWeight - risk * self.riskWeight
            
            if value > bestValue:

                bestValue = value
                bestStock = s

        if bestStock == None:
            return()
        if self.money < 10000:#Basically day > 1
            return()

        amountToBuy = int(self.money / bestStock.price)

        # Purchase
        self.money -= amountToBuy * bestStock.price
        self.stocks[bestStock] = amountToBuy

    def totalValue(self):

        total = 0
        for s in self.stocks:
            amount = self.stocks[s]
            price = s.price
            total += amount * price

        total += self.money
        
        return(total)
