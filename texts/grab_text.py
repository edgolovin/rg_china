from bs4 import BeautifulSoup
from pathlib import Path
from bs4 import Tag

header_attrs = ['b-material-head__date-day',
                'b-material-head__title',
                'b-material-head__subtitle']

article_bad_attrs = ['incut',
                     'b-material-img',
                     'b-material-wrapper__rubric',
                     'article-img',
                     'b-read-more',
                     'b-link']


def clear_bad_tags(article):
    bad_tags = article.find_all(class_=article_bad_attrs)
    for tag in bad_tags:
        tag.decompose()
    return article


def make_element(i, soup):
    try:
        if i != 99:
            element = soup.find(class_=header_attrs[i]).text.strip()
        else:
            element = clear_bad_tags(soup.find('article')).text
    except AttributeError:
        element = '###'
    return element


def main():
    for html_file in Path('./html').glob('*.html'):
        print(html_file.name)
        with open(html_file, encoding='utf-8') as hf:
            soup = BeautifulSoup(hf, "html.parser").find('div', class_="l-page__wrapper")

        date_day = make_element(0, soup)
        title = make_element(1, soup)
        subtitle = make_element(2, soup)
        article = make_element(99, soup)

        txt_file = html_file.name.replace('html', 'txt')
        with open(f'./txt/{txt_file}', 'w', encoding='utf-8') as f:
            f.write('\n'.join([date_day, title, subtitle, '***', article]))


if __name__ == '__main__':
    main()
