from pathlib import Path

urls = list()


def main():
    global urls
    for p in Path('.').glob('*.txt'):
        urls.append('https://rg.ru/' + str(p).replace('_', '/').replace('txt', 'html'))

    with open('all_urls_before_2019.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(urls))


if __name__ == '__main__':
    main()
