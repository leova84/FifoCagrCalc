from collections import deque

class Transaction(object):


	def __init__(self, iprice, iquantity, idate):

		self.price = deque([iprice])
		self.quantity = deque([iquantity])
		self.date = deque([idate])

	def add(self, iprice, iquantity, idate):
		self.price.append(iprice)
		self.quantity.append(iquantity)
		self.date.append(idate)