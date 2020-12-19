import scrapy

filesList = open('filesList2.txt', 'r')
htmlHead = '<!DOCTYPE html><html lang="ru"><meta charset="utf-8"><meta property="og:site_name" content="Российская газета">'

for fileName in filesList:
	fileName = fileName.strip('\n')
	with open(fileName) as f:
		sel = scrapy.Selector(text = f.read())
		articleHead = sel.xpath('//*[@id="rgb_material-head_doc"]').extract()
		articleBody = sel.xpath('//*[@class="b-content b-content_document"]').extract()
	if len(articleHead)>0 and len(articleBody)>0:
		newF = open(fileName, 'w')
		newF.write(htmlHead + str(articleHead).strip('[]\'') + str(articleBody).strip('[]\''))
		newF.close()
	else:
		print(fileName)