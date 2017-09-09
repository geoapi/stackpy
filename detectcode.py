import BeautifulSoup
soup = BeautifulSoup(argv[1])
for el in soup.findall('code'):
	print el.code.string


