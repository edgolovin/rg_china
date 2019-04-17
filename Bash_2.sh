curl 'https://rg.ru/api/search/' -H 'content-type: application/json' --data '{"keywords":"китай","limit":999,"offset":0,"filters":[["range_yyyymmdd",["19800101","20000101"]]],"view":"json","highlight":0,"sort_mode":"timestamp"}' > 198001.txt
curl 'https://rg.ru/api/search/' -H 'content-type: application/json' --data '{"keywords":"китай","limit":999,"offset":0,"filters":[["range_yyyymmdd",["20181201","20190101"]]],"view":"json","highlight":0,"sort_mode":"timestamp"}' > 201812.txt
curl 'https://rg.ru/api/search/' -H 'content-type: application/json' --data '{"keywords":"китай","limit":999,"offset":0,"filters":[["range_yyyymmdd",["20190101","20190201"]]],"view":"json","highlight":0,"sort_mode":"timestamp"}' > 201901.txt
curl 'https://rg.ru/api/search/' -H 'content-type: application/json' --data '{"keywords":"китай","limit":999,"offset":0,"filters":[["range_yyyymmdd",["20190201","20190301"]]],"view":"json","highlight":0,"sort_mode":"timestamp"}' > 201902.txt



