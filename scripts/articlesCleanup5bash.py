import scrapy

filesList = open('filesList5.txt', 'r')
firstWord = 'firefox '
bashScript = open('articlesCleanup5.sh', 'a')

for fileName in filesList:
	fileName ='https://rg.ru/' + fileName.strip('\n')
	bashScript.write(firstWord + fileName + '\n')
filesList.close()		
bashScript.close()