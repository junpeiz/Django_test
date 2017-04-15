# -*- coding: utf8 -*-

import urllib
import requests,time
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

url = 'http://money.163.com/'

response = requests.get(url, headers = headers)
html_soup = BeautifulSoup(response.content, "html.parser")
class_collect = ['topnews_nlist', 'topnews_nlist mb20 no_border']
for class_name in class_collect:
    topnews = html_soup.find('ul', class_=class_name)
    news_list = topnews.find_all('a')
    for news in news_list:
        news_link = str(news.get('href'))
        news_head = news.string
        if not news_head:
            continue
        print(news_head)
        print(news_link)

