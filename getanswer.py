import requests
from sys import argv
'''Usage : getAnswers querstion id, tags
getAnswers(16358366,"tags")
return the answer's tags
'''
def getAnswers(*args):
	url = "https://api.stackexchange.com/2.2/questions/"+"".join([str(i) for i in argv[1]])+"/?filter=withbody&site=stackoverflow"
	print "The URL is: " + url
	response = requests.get(url)
	jsonobj = response.json()
	print jsonobj
	return;

getAnswers(argv[1:])

