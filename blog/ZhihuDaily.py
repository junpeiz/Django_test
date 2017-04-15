# -*- coding: utf-8 -*-

import datetime
import math
import requests

from requests.exceptions import HTTPError

from bs4 import BeautifulSoup


class FetchError(Exception):

    def __init__(self, errtype=''):
        self.errtype = errtype

    def __str__(self, *args, **kwargs):
        return self.__class__.__name__ + ':' + self.errtype


class PageNotFoundError(FetchError):
    pass


class NewsFetcher():
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
               "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Referer": "http://www.example.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
               }

    def fetch_json(self, url, method='get'):
        r = requests.request(
            method=method,
            url=url,
            headers=self.headers
        )
        try:
            r.raise_for_status()
            if r.encoding.lower() == 'iso-8859-1':
                r.encoding = 'utf-8'
            json = r.json()
        except HTTPError as e:
            raise FetchError('invalid_url')
        return json

    def fetch_html(self, url, method='get'):
        r = requests.request(
            method=method,
            url=url,
            headers=self.headers
        )
        try:
            r.raise_for_status()
            if r.encoding.lower() == 'iso-8859-1':
                r.encoding = 'utf-8'
            html = r.text
        except HTTPError as e:
            raise FetchError('invalid_url')
        return html


class ZhihuDailyFetcher(NewsFetcher):
    # ZhihuDaily has official API

    def get_latest_news(self):
        response_json = self.fetch_json(
            'http://news-at.zhihu.com/api/4/news/latest')
        return response_json

    def get_before_news(self, date_str):
        response_json = self.fetch_json(
            'http://news.at.zhihu.com/api/4/news/before/' + date_str)
        return response_json

    def get_story_detail(self, story_id):
        response_json = self.fetch_json(
            'http://news-at.zhihu.com/api/4/news/' + str(story_id))
        return response_json
