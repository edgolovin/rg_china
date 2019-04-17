import re

fl = open('FilesList.txt', 'r')
months = fl.read().split('\n')


for month in months:
	file = open(month, 'r')
	# print(file.read())
	split_file = re.sub(r'},{','\\n', file.read())
	modFile = open('_'+month, 'w')
	modFile.write(split_file)
	modFile.close()