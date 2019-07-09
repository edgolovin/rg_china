# https://github.com/edgolovin/rg_china

## All information was gathered from the site of "Rossiyskaya Gazeta" https:\\rg.ru\

This repo was created for scientific reasons, namely to investigate China's image in Runet media.

### Tools used
* curl
* bash
* python

### Operations sequence
1. rg.ru search form analysis. 'China' keyword is present in more than 30k articles starting from 1990s.
2. To scrape all needed articles urls, we use curl-style request code including search form parameters.
3. Search form output is limited by dynamic page loading. Much worse, dynamic loading doesn't return ALL 30k of needed articles. It returns under several thousands. We must use partial loading of search form results not exceeding 1000 of search results in order to be able to scrape it. Partial loading can be limited by month.
4. Creating Python script _name_ which writes bash script _name_ containing repeatable commands for curl in order to keep search from results under 999 for every month starting from 1990 until nowadays.
5. Executing bash script _name_. Downloading all search form results into separate files for every month.
6. Creating Python script _name_ for extracting all urls into single file _name_.
7. Writing Python script _name_ which produces bash script _name_ taking urls one-by-one and downloading using curl each article into separate html file. Each file has a name referencing to its url on rg.ru.