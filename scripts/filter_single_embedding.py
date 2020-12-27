"""
For all articles count the word 'кита' in it,
if count < 2, move the article to ./single_embed/
"""
import shutil
from pathlib import Path

ARTICLES = Path(r'D:\01code\01piton\rg_china\rg_until_2019-02')
PROJECT_DIR = Path(r'D:\01code\01piton\rg_china')


def count_kita(a: Path):
    with open(a, 'r', encoding='utf-8') as f:
        t = f.read()

    text = t.lower()
    return text.count('кита')


for article in ARTICLES.iterdir():
    print('-', end='')
    if count_kita(article) < 2:
        shutil.move(article, Path(PROJECT_DIR / 'single_embed' / article.name))
        print('.', end='')
