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

# {
#     "status": "0",
#     "msg": "ok",
#     "result": {
#         "channel": "头条",
#         "num": "10",
#         "list": [        
#             {
#                 "title": "中国开闸放水27天解救越南旱灾",
#                 "time": "2016-03-16 07:23",
#                 "src": "中国网",
#                 "category": "mil",
#                 "pic": "http://api.jisuapi.com/news/upload/20160316/105123_31442.jpg",
#                 "content": "<p class="\"art_t\"">　　原标题：防总：应越南请求 中方启动澜沧江水电站水量应急调度</p><p class="\"art_t\"">　　记者从国家防总获悉，应越南社会主义共和国请求，我方启动澜沧江梯级水电站水量应急调度，缓解湄公河流域严重旱情。3月15日8时，澜沧江景洪水电站下泄流量已加大至2190立方米每秒，标志着应越方请求，由我方实施的澜沧江梯级水电站水量应急调度正式启动。</p>",
#                 "url": "http://mil.sina.cn/zgjq/2016-03-16/detail-ifxqhmve9235380.d.html?vt=4&pos=108",
#                 "weburl": "http://mil.news.sina.com.cn/china/2016-03-16/doc-ifxqhmve9235380.shtml"
#             }
#         ]
#     }
# }