"""
check kitano, delete if not kitai
"""
import os
import shutil
from pathlib import Path

ARTICLES = Path(r'D:\01code\01piton\rg_china\rg_until_2019-02')
PROJECT_DIR = Path(r'D:\01code\01piton\rg_china')


def check_kitano(a: Path):
    """
    check 'kitano' embeddings against 'kita'
    if equal return true else false
    :param a: Path
    :return: bool
    """
    with open(a, 'r', encoding='utf-8') as f:
        t = f.read()

    text = t.lower()
    return text.count('китано') == text.count('кита')


for article in ARTICLES.iterdir():
    print('-', end='')
    if check_kitano(article):
        os.remove(article)
        print('.', end='')
