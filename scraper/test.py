from jisu import jisu

news = jisu()
ch = news.get_channel()

for channel in ch:
    head_collect = news.get_news(channel)
    for head in head_collect:
        print(head)