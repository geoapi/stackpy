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
codeList = [];
def detectCode(code, *args):
	soup = BeautifulSoup(code, "lxml")
	result = soup.find_all(lambda tag: tag.name == 'code')
	if not result:
		print "none"		
	else:
		print result
	return result
print argv[1]

detectCode(argv[1])
