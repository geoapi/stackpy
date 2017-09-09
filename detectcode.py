''' 
Usage
detectCode('<p> somthing <code> some code! </code> </p>')
returns
[<code> some code! </code>]
if more code exists return them all 
if none return none!
'''
from sys import argv
from bs4 import BeautifulSoup
def detectCode(*args):
	soup = BeautifulSoup(argv[1])
	result = soup.find_all(lambda tag: tag.name == 'code')
	if not result:
		print "none"
		return False
	else:
		print result
		return result

detectCode(argv[1])
