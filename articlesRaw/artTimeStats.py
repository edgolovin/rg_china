''' this script counts all articles placing them into dict

'''
import matplotlib.pyplot as plt

artByMonths = {}

with open('cleanList.txt', 'r') as filesNames:
	for file in filesNames:
		file = file.strip('\n')
		monthKey = file[:7] # 0123_56_
		if monthKey in artByMonths:
			artByMonths[monthKey] += 1
		else:
			artByMonths[monthKey] = 1

#print(str(artByMonths.keys()))

with open('timeStats.txt', 'w') as f:
	for i in artByMonths.keys():
		f.write(str(i) + ': ' + str(artByMonths[i]) + '\n')

#plt.plot(artByMonths.keys(), artByMonths.values())
plt.bar(artByMonths.keys(), artByMonths.values())
plt.autoscale()
plt.show()