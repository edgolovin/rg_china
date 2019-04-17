import re

fl = open('FilesList.txt', 'r')
months = fl.read().split('\n')
urlsFile = open('_urls.txt', 'w')
# print(months)

for month in months[:-1]:
	with open(month, 'r') as file:
		for line in file:
			uri = re.search(r'"uri":"/\d+\S+"', line)
			try:
				urlsFile.write('https://rg.ru' + line[uri.start()+7:uri.end()-1] + '\n')
			except AttributeError:
				print('**************************Empty re.search**************************')
	
urlsFile.close()