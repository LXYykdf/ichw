'''
currency.py:
			Module for currency exchange

			This module provides several string parsing functions to implement a 
			simple currency exchange routine using an online currency service. 
			The primary function in this module is exchange.
			Returns: amount of currency received in the given exchange.
__author__='Liuxinyi'
__pkuid__ ='1800011815'
__email__ ='1800011815@pku.edu.cn'
'''





from urllib.request import urlopen

def currency_response(currency_from,currency_to,amount_from):
	
	'''
	Returns: a JSON string that is a response to a currency query.
	
	A currency query converts amount_from money in currency currency_from 
	to the currency currency_to. The response should be a string of the form
	
		'{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
	
	where the values old-amount and new-amount contain the value and name 
	for the original and new currencies. If the query is invalid, both 
	old-amount and new-amount will be empty, while "success" will be followed 
	by the value false.
	
	Parameter currency_from: the currency on hand
	Precondition: currency_from is a string
	
	Parameter currency_to: the currency to convert to
	Precondition: currency_to is a string
	
	Parameter amount_from: amount of currency to convert
	Precondition: amount_from is a float
	'''

	st = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+\
		currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
	doc = urlopen(st)
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii')
	return jstr


	
def iscurrency(currency):

	'''
	Returns: True if currency is a valid (3 letter code for a) currency. 
	It returns False otherwise.

	Parameter currency: the currency code to verify
	Precondition: currency is a string.
	'''

	response = currency_response(currency,'USD',5)
	string = response.split('"')

	if string[10] == ' : true, ':
		return True
	else:
		return False


def exchange(currency_from,currency_to,amount_from):
	
	'''
	In this exchange, the user is changing amount_from money in 
	currency currency_from to the currency currency_to. The value 
	returned represents the amount in currency currency_to.

	

	Parameter currency_from: the currency on hand;
	Precondition: currency_from is a string for a valid currency code;
	
	Parameter currency_to: the currency to convert to;
	Precondition: currency_to is a string for a valid currency code;
	
	Parameter amount_from: amount of currency to convert;
	Precondition: amount_from is a float.

	The value returned has type float.
	'''

	if iscurrency(currency_from) and iscurrency(currency_to):
		response = currency_response(currency_from,currency_to,amount_from)
		string = response.split('"')
		amount_out = string[7]
		out = amount_out.split(' ')
		output = out[0]
		return (float(output))
	else:
		response = currency_response(currency_from,currency_to,amount_from)
		string = response.split('"')
		return string[-2]


def test_currency_response():
	'''
	Unit test for module exchange

	When run as a script, this module invokes several procedures that 
	test the  function currency_response.
	'''
	assert(currency_response('USD','EUR',2) == '{ "from" : "2 United States Dollars", "to" : "1.727138 Euros", "success" : true, "error" : "" }')
	assert(currency_response('s','s',8) == '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
	assert(currency_response('USD','CNY',1) == '{ "from" : "1 United States Dollar", "to" : "6.8521 Chinese Yuan", "success" : true, "error" : "" }')

def test_iscurrency():
	'''
	Unit test for module exchange

	When run as a script, this module invokes several procedures that 
	test the  function iscurrency.
	'''
	assert(iscurrency('USD') is True)
	assert(iscurrency('s') is False)
	assert(iscurrency('CNY') is True)

def test_exchange():
	'''
	Unit test for module exchange

	When run as a script, this module invokes several procedures that 
	test the  function exchange.
	'''
	assert(exchange('USD','EUR',2)  ==  1.727138)
	assert(exchange('s','s',8) == 'Source currency code is invalid.')
	assert(exchange('USD','CNY',1)  ==  6.8521)

def testALL():
	'''Test all cases.'''
	test_currency_response()
	test_iscurrency()
	test_exchange()
	print('All tests passed')

def main():
	'''
	main module
	'''
	currency_from = input('请输入起始货币英文简称:')
	currency_to = input('请输入目标货币英文简称:')
	amount_from = float(input('请输入起始货币金额:'))

	print(exchange(currency_from,currency_to,amount_from))
	testALL()

if __name__ == '__main__':
	main()
