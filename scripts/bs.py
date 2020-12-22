"""
Process all articles.html
Grab text, replace non-human-readable symbols
Rewrite as files.txt
"""

from pathlib import Path
from bs4 import BeautifulSoup

ARTICLES = Path(r'D:\01code\01piton\rg_china\articlesRaw')
PROJECT_DIR = Path(r'D:\01code\01piton\rg_china')


def open_and_replace(a: Path):
    with open(a, 'rb') as f:
        soup = BeautifulSoup(f, features='html.parser').get_text()

    c = soup.replace('\\xa0', ' ')
    d = c.replace('\\n', '\n')
    new_name = a.name.strip('html') + 'txt'

    with open(new_name, 'w', encoding='utf-8') as f:
        f.write(d)


for article in ARTICLES.iterdir():
    open_and_replace(article)
