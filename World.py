

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

	def run(days):
		"""Run simulation for a given number of days"""
		for i in range(days):
			self.nextDay()

	def nextDay():

		for f in self.funds:
			# Reevaluate stocks if necessary
			f.evaluate(self.stocks)
			# Make trades
			f.trade()

