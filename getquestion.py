import requests
from sys import argv
'''
give a search query or keyword and title or body
'''
def getQuestions(query, *args):
	response = requests.get("https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=votes&accepted=true&tagged=api&filter=withbody&site=stackoverflow"+"&q="+query)
	jsonobj = response.json()
	i = 0
	for item in jsonobj["items"]: 
		i = i + 1
		print item[argv[2]]
	print "number of return items are : " + str(i)
	return;
getQuestions(*argv[1:]) 
