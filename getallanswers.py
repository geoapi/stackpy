import requests
from sys import argv
from detectcode import detectCode
s= '''Usage : getallAnswers takes querstion id and returns all answers with body
example 
python getallAnswers.py 16358366 param
where param can be:
owner
score
score
last_activity_date
creation_date
answer_id 
question_id 
body


print s'''

def getallAnswers(*args):
	url = "https://api.stackexchange.com/2.2/questions/"+"".join([str(i) for i in argv[1]])+"/answers?order=desc&sort=votes&filter=withbody&site=stackoverflow"
	'''	print "The URL is: " + url'''
	response = requests.get(url)
	jsonobj = response.json()
	for item in jsonobj["items"]: 
	        '''	print item[argv[2]]'''
		code = item[argv[2]]
		detectCode(code)
	return;

getallAnswers(argv[1:])


