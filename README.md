# Mining web for texts about China

## `rg.ru` workflow
1. *rg.ru* search form analysis. 'китай' keyword is present in more than 30k articles starting from 1990s.
1. To scrape all needed articles urls, we use curl-style request code including search form parameters.
1. Search form output is limited by dynamic page loading. Much worse, dynamic loading doesn't return ALL 30k of needed articles. It returns under several thousands. We use partial loading of search form results not exceeding 1000 of search results in order to be able to scrape it. Partial loading was limited by month.
1. Creating Python script `urlsByMonth/origins/DatesList.py` which writes bash script `urlsByMonth/origins/BashCmd.sh` containing repeatable commands for curl in order to keep search from results under 999 for every month starting from 1990 until nowadays.
1. Executing bash script `BashCmd.sh`. Downloading all search form results into separate files for every month.
1. Creating Python script `urlsByMonth/01uri.py` for extracting all urls into single file `urls_till2019-02.txt` which can be found in repo root.
1. Writing Python script `articlesRaw/articlesDownload.py` which produces bash script `articlesRaw/articlesDownload.sh` taking urls one-by-one and downloading using curl each article into separate html file: folder `articlesRaw`. Each file has a name referencing to its uri on *rg.ru*.
1. Writing some Python and bash scripts for cleaning articles files off useless html [folder articlesRaw/]:`articlesCleanup.py, articlesCleanup2.py, articlesCleanup3.py, articlesCleanup4.py, articlesCleanup5bash.py, articlesCleanup5.sh`.
1. After cleaning the folder `articlesRaw/` contains lite versions of articles.html. Several iterations were conducted to clean files because several article types use different XPath on *rg.ru*. On this stage full list is in `filesList6.txt`. Some files.html were deleted manually due to non-relevance (for example 'кит' instead of 'китай') or because of being empty (not present on rg.ru) (`filesList5.txt`).
1. Using `grep` in order to separate even more non-relevant articles. All used `grep` commands are listed in `grepSeparation.txt`. All deleted non-relevant articles listed in `articlesRaw/deletedNotKitai.txt`. After all we have `articlesRaw/cleanList.txt` of 32_816 relevant articles.
1. `articlesRaw/artTimeStats.py` generates `articlesRaw/timeStats.txt` and draws on its base a plot "number of articles per month".
1. ~~Long pause~~
1. `articlesRaw` cleanup: take out textual data, replacing non-readable `\xa0` and `\n` symbols: `bs.py`