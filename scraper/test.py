from jisu import jisu
import json

news = jisu()
ch = news.get_channel()

for channel in ch:
    result = news.get_news(channel)
    for i, news_ in enumerate(result):
        if(news_["pic"]==""):
            print("pop",i)
            result.pop(i)
    filename = str(channel)+".json"
    with open(filename, 'w') as outfile:
        json.dump(result, outfile)

# Return parameter:
# channel string  频道(头条,财经,体育,娱乐,军事,教育,科技,NBA,股票)
# num int 数量
# title   string  标题
# time    string  时间
# src string  来源
# category    string  分类
# pic string  图片
# content string  内容
# url string  原文手机网址
# weburl  string  原文PC网址

# 手机号18888888888卖出1.2亿 2017-04-15 08:14 环球网 tech http://api.jisuapi.com/news/upload/20170415/100002_82818.jpg
# 手机靓号18888888888卖1.2亿 2017-04-15 08:13 环球网 finance http://api.jisuapi.com/news/upload/20170415/100002_65966.jpg
# 铁岭2个月内党政一把手均被查 2017-04-15 07:51 综合 news http://api.jisuapi.com/news/upload/20170415/100002_62928.jpg
# 外媒:特朗普正在成为战争总统 2017-04-15 06:25 环球网 news http://api.jisuapi.com/news/upload/20170415/100002_68786.jpg
# 震惊!这些霸占行业龙头的大学 2017-04-15 07:40 新浪教育 edu http://api.jisuapi.com/news/upload/20170415/090004_76462.jpg
# 安卓8.0发布:华为Mate 9适配 2017-04-14 19:37 TechWeb tech http://api.jisuapi.com/news/upload/20170415/090003_33401.png
# 2500元价位高关注手机推荐 2017-04-15 05:43 新浪手机 tech http://api.jisuapi.com/news/upload/20170415/090003_38039.jpg
# 小米6渲染图再次曝光 2017-04-15 06:30 IT168.com tech http://api.jisuapi.com/news/upload/20170415/090002_33507.jpg
# 分析师称iPhone8将拯救苹果 2017-04-15 06:30 综合 tech http://api.jisuapi.com/news/upload/20170415/090002_10087.jpg
# 华为席卷双摄手机销量排行 2017-04-15 06:30 手机中国 tech http://api.jisuapi.com/news/upload/20170415/090002_86668.jpg
# 郑渊洁买十套房存放读者来信 2017-04-15 08:12 综合 finance http://api.jisuapi.com/news/upload/20170415/090002_77958.jpg
# 郑渊洁买十套房:给读者的信住 2017-04-15 06:39 央视新闻 news http://api.jisuapi.com/news/upload/20170415/090001_39979.jpg
# 报告:中国因吸烟年损失3500亿 2017-04-15 01:10 环球网 news http://api.jisuapi.com/news/upload/20170415/080001_87565.jpg
# 证监会剑指次新股恶意炒作 2017-04-15 06:04 21世纪经济报道 finance
# 秦皇岛深夜出台限购政策 2017-04-15 00:36 综合 finance
# 警方通报山水水泥武斗事件 2017-04-15 01:28 上海证券报 finance
# 穆帅透露马塔休战至5月底 2017-04-15 03:39 新浪体育 sports http://api.jisuapi.com/news/upload/20170415/070005_47804.jpg
# 禅师公开宣布今夏兜售甜瓜 2017-04-15 06:16 新浪体育 sports http://api.jisuapi.com/news/upload/20170415/070005_99586.jpg
# 孙杨微博发声:全满贯人生圆满 2017-04-15 03:30 新浪体育 sports http://api.jisuapi.com/news/upload/20170415/070004_31801.jpg
# “撕名牌”主角:爱中国身份 2017-04-15 03:34 中国新闻网 news http://api.jisuapi.com/news/upload/20170415/070004_12252.jpg
# 中国专家批美军“炸弹之母” 2017-04-15 02:13 环球网 news http://api.jisuapi.com/news/upload/20170415/070004_88460.jpg
# 首艘国产航母即将下水 2017-04-15 01:20 综合 finance http://api.jisuapi.com/news/upload/20170415/070004_57671.jpg
# 雄安新区严管严打炒房炒地 2017-04-15 02:24 综合 finance
# 朝鲜或进行第六次核试验 2017-04-14 23:32 环球网 news http://api.jisuapi.com/news/upload/20170415/070003_49099.jpg
# MVP排行榜:威少榜首力压哈登 2017-04-15 05:55 新浪体育 sports http://api.jisuapi.com/news/upload/20170415/070003_60269.jpg