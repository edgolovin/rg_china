"""
Load page of rg.ru with query='китай' month by month.
Click 'more' while all articles loaded.
Grab urls of articles.
"""
import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
LOAD_MORE_BTN: WebElement
articles_num: int


def load_more_articles():
    driver.execute_script("arguments[0].click();", LOAD_MORE_BTN)
    time.sleep(2)


def all_articles_loaded() -> bool:
    global articles_num
    found_articles_element = driver.find_element_by_class_name("b-search-info__meta")
    articles_num = int(found_articles_element.text.split()[0])
    articles_elements = driver.find_elements_by_class_name("b-news-inner__list-item")
    return len(articles_elements) == articles_num


def query_month(year, month):
    global LOAD_MORE_BTN
    if month == 12:
        link = f"https://rg.ru/search/?keywords=китай&from=01.12.{year}&to=01.01.{year + 1}"
    else:
        link = "https://rg.ru/search/?keywords=китай&from=01.{:02d}.{:d}&to=01.{:02d}.{:d}".format(month, year,
                                                                                                   month + 1, year)
    driver.get(link)
    time.sleep(5)
    LOAD_MORE_BTN = driver.find_element_by_class_name("b-news-inner__action_btn")
    time.sleep(5)


def main():
    year = 2021
    months = range(1, 2)
    for month in months:
        query_month(year, month)
        while not all_articles_loaded():
            load_more_articles()
        articles_list: WebElement = driver.find_element_by_class_name("b-news-inner__list")
        hrefs = [elem.get_attribute('href') for elem in articles_list.find_elements_by_class_name("b-link_title")]
        pprint(hrefs)
        with open('{:d}-{:02d}.txt'.format(year, month), 'w', encoding='utf-8') as f:
            f.writelines('\n'.join(hrefs + [str(articles_num)]))
    driver.quit()


if __name__ == '__main__':
    main()
