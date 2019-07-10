
BashFile = open('articlesDownload.sh', 'w')
urlsFromFile = open('urls_till2019-02.txt', 'r')

for line in urlsFromFile:
	line = line.strip('\n')
	fileName = line.replace('https://rg.ru/', '').replace('/', '_')
	a = 'curl \'%s\' > %s' % (line, fileName)
	BashFile.write(a + '\n')
