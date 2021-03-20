from pathlib import Path

TARGET_DIR = Path('./html/empties')
MESSAGE_404 = 'Страница, которую Вы запросили, не найдена на сайте Российской Газеты'
MESSAGE_301 = '301 Moved Permanently'
oops = 'Oops.'


def move_emptie(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read()
    article_parts = text.split('***')
    if '###' in article_parts[1]:
        # print(txt_file.name)
        html_file = Path('./html') / txt_file.name.replace('txt', 'html')
        # print(html_file)
        html_file.rename(TARGET_DIR / html_file.name)


def del_404(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        text = f.read()
    if MESSAGE_404 in text or MESSAGE_301 in text or oops in text:
        html_file.unlink()


def main():
    # for txt_file in Path('./txt').glob('*.txt'):
    #     move_emptie(txt_file)
    for html_file in Path(TARGET_DIR).glob('*.html'):
        del_404(html_file)


if __name__ == '__main__':
    main()
