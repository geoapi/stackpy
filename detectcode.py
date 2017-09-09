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
