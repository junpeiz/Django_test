import json

class LoadJsonNews():

    def getnews(self):
        news = []
        ch = ["头条","财经","体育","教育","科技"]
        for channel in ch:
            filename = "D:/Desktop/BSproject/blog/static/json/" + channel + ".json"
            json_data = open(filename)   
            temp_news = json.load(json_data)
            news = news + temp_news
            json_data.close()
        return news