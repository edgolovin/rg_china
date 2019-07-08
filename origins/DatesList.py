months = []
for i in range(2000, 2019):
	months += [str(i) + m for m in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']]

BashFile = open('BashCmd.sh', 'w')

for i in range(len(months)-1):
	a = 'curl \'https://rg.ru/api/search/\' -H \'content-type: application/json\' --data \'{\"keywords\":\"китай\",\"limit\":999,\"offset\":0,\"filters\":[[\"range_yyyymmdd\",[\"%s01\",\"%s01\"]]],\"view\":\"json\",\"highlight\":0,\"sort_mode\":\"timestamp\"}\' > %s.txt' % (months[i], months[i+1], months[i])
	BashFile.write(a + '\n')
