from bs4 import BeautifulSoup
import requests
import re


def max_page(soup):
    while 1:
        maximum = 0
        page = 1

        page_list = soup.find('a', {'class': 'pagination-link'})
        page_list_2 = page_list.find_all('span')
        print(page_list_2)
        if not page_list:
            maximum = page - 1
            break
        page = page + 1

    print(page)
    return page
