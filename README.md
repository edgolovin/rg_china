https://github.com/edgolovin/rg_china

## All information was gathered from the site of "Rossiyskaya Gazeta" https:\\rg.ru\

This repo was created for scientific reasons, namely to investigate China's image in Runet media.

### Tools used
* curl
* bash
* grep
* python
	* scrapy

### Operations sequence
1. *rg.ru* search form analysis. 'китай' (China in rus.) keyword is present in more than 30k articles starting from 1990s.
2. To scrape all needed articles urls, we use curl-style request code including search form parameters.
3. Search form output is limited by dynamic page loading. Much worse, dynamic loading doesn't return ALL 30k of needed articles. It returns under several thousands. We use partial loading of search form results not exceeding 1000 of search results in order to be able to scrape it. Partial loading was limited by month.
4. Creating Python script _urlsByMonth/origins/DatesList.py_ which writes bash script _urlsByMonth/origins/BashCmd.sh_ containing repeatable commands for curl in order to keep search from results under 999 for every month starting from 1990 until nowadays.
5. Executing bash script _BashCmd.sh_. Downloading all search form results into separate files for every month.
6. Creating Python script _urlsByMonth/01uri.py_ for extracting all urls into single file _urls_till2019-02.txt_ which can be found in repo root.
7. Writing Python script _articlesRaw/articlesDownload.py_ which produces bash script _articlesRaw/articlesDownload.sh_ taking urls one-by-one and downloading using curl each article into separate html file: folder _articlesRaw_. Each file has a name referencing to its uri on *rg.ru*.
8. Writing some Python and bash scripts for cleaning articles files off useless html [folder articlesRaw/]:_articlesCleanup.py, articlesCleanup2.py, articlesCleanup3.py, articlesCleanup4.py, articlesCleanup5bash.py, articlesCleanup5.sh_.
9. After cleaning the folder _articlesRaw/_ contains lite versions of articles.html. Several iterations were conducted to clean files because several article types use different XPath on *rg.ru*. On this stage full list is in _filesList6.txt_. Some files.html were deleted manually due to non-relevance (for example 'кит' instead of 'китай') or because of being empty (not present on rg.ru) (_filesList5.txt_).
10. Using _grep_ in order to separate even more non-relevant articles. All used _grep_ commands are listed in _grepSeparation.txt_. All deleted non-relevant articles listed in _articlesRaw/deletedNotKitai.txt_. After all we have _articlesRaw/cleanList.txt_ of 32_816 relevant articles.
11. _articlesRaw/artTimeStats.py_ generates _articlesRaw/timeStats.txt_ and draws on its base a plot "number of articles per month".