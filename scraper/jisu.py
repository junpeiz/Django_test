from urllib.parse import urlencode

import requests
# -*- coding: utf-8 -*-


class jisu:
    AppKey = 'f19ded98c0f37a29'

    @staticmethod
    def get_channel(timeout=1):
        """
        获取新闻频道 https://api.jisuapi.com/news/channel
        :param timeout: request时长限制
        :return: 渠道list
        """
        url = 'https://api.jisuapi.com/news/channel?'
        params = {'appkey': jisu.AppKey}
        params_encoded = urlencode(params)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.get(url, params=params_encoded, headers=headers, timeout=timeout).json()
            if response['status'] == '0':
                return response['result']
        except:
            pass
        return None

    @staticmethod
    def get_news(channel, timeout=1):
        """
        从单一频道获取新闻 https://api.jisuapi.com/news/get
        :param channel: 频道
        :param timeout: request时长限制
        :return: 新闻list
        """
        url = 'http://api.jisuapi.com/news/get?'
        params = {'appkey': jisu.AppKey, 'start': 0, 'num': 40, 'channel': channel}
        params_encoded = urlencode(params)
        headers = {'content-type': 'application/json'}
        # print("get_news")
        try:
            response = requests.get(url, params=params_encoded, headers=headers, timeout=timeout).json()
            # print(response)
            if response['status'] == '0':
                return response['result']['list']
        except:
            pass
        return None

    @staticmethod
    def search_news(keyword, timeout=1):
        """
        搜索新闻 https://api.jisuapi.com/news/search
        :param keyword: 搜索关键词
        :param timeout: request时长限制
        :return: 新闻list
        """
        url = 'https://api.jisuapi.com/news/search'
        params = {'appkey': jisu.AppKey, 'keyword': keyword}
        params_encoded = urlencode(params)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.get(url, params=params_encoded, headers=headers, timeout=timeout).json()
            if response['status'] == '0':
                return response['result']['list']
        except:
            pass
        return None
