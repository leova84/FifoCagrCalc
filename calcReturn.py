from Transaction import Transaction
from datetime import datetime
from decimal import *
getcontext().prec = 6


tlist = {}

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")
    return abs((d2 - d1).days)


def testTransaction():
	t = Transaction(6.50, 7, '12/13/2017')
	print t.price
	print t.quantity
	print t.date

def processTransaction(itype, iname, iprice, iquantity, idate):

	if itype == 'buy':

		if iname in tlist:
			tlist[iname].add(iprice, iquantity, idate)
	    
		else:

			tlist[iname]= Transaction(iprice, iquantity, idate)


	if itype == 'sell':
		
		if iname not in tlist: 
			print "There is inadequate " + iname +" item to sell."
			raise ValueError('There is inadequate " + iname +" item to sell.')

		basis = 0;
		count = 0;
		length_held = 0;

		while iquantity > count and iname in tlist:

			top = tlist[iname].quantity[0]
			count = count + top;

			# trying to satisfiy the sell
			if iquantity - count >= 0:

				# print Decimal(tlist[iname].quantity[0]) / Decimal(iquantity)
				# print days_between(tlist[iname].date[0], idate)

				# praportion of the length held to the proporation of the overall quantity
				length_held += Decimal(tlist[iname].quantity[0]) / Decimal(iquantity) *  days_between(tlist[iname].date.popleft(), idate)


				basis += tlist[iname].price.popleft() * tlist[iname].quantity.popleft()


			else:
				length_held += Decimal(tlist[iname].quantity[0]) / Decimal(iquantity) *  days_between(tlist[iname].date.popleft(), idate)

				basis = (top-(count - iquantity)) * tlist[iname].price[0]
				tlist[iname].quantity[0] = count - iquantity

		if count < iquantity:
			print "There is inadequate " + iname +" item to sell."
			raise ValueError('There is inadequate " + iname +" item to sell.')

		gain = iquantity * iprice - basis;

		cagr = Decimal((iquantity * iprice) / basis) **  Decimal(Decimal(1) / (Decimal(length_held)/Decimal(365.25))) - 1

		print iname, iquantity, basis, gain, length_held, cagr



testbuys = [['adm', 10.00, 1, '1/1/2015'], ['ttwo', 10.00, 10, '1/1/2015'], ['adm', 20.00, 100, '1/1/2016']]
testsells = [['ttwo', 20.00, 10, '1/1/2016'], ['adm', 30.00, 101, '1/1/2017']]


for buy in testbuys:
	processTransaction('buy', buy[0], buy[1], buy[2], buy[3])

print len(tlist)

for k, v in tlist.iteritems():
	print k , v.price , v.quantity, v.date

for sell in testsells:
	processTransaction('sell', sell[0], sell[1], sell[2], sell[3])


