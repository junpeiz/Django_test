from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
import jieba
import jieba.analyse
from bs4 import BeautifulSoup

# models.Model means that the Post is a Django Model
# So Django knows that it should be saved in the database.
class News(models.Model):
    # Title of news
    title = models.CharField(max_length=80)
    # Category of news, like sports, education, economy and so on
    category = models.CharField(max_length=20)
    # The name of the website the news from
    src = models.CharField(max_length=20)
    # The url of the picture of the news
    pic = models.URLField(max_length=200)
    # The weburl of the news
    weburl = models.URLField(max_length=200, primary_key=True)
    # The date of getting the news
    time = models.DateTimeField(default=timezone.now)
    # The keyword calculated by TF-IDF
    tags = models.CharField(max_length=50, default="")

    @classmethod
    def get_and_store(cls, news_ins):
        # try:
        content = news_ins["content"]
        html_soup = BeautifulSoup(content, "html.parser")
        para_it = html_soup.find_all('p')
        content = ""
        for para in para_it:
            if(para.string is not None):
                content += para.string
        # Use jieba TF-IDF analysis to get a list of string, each is a word
        tags = jieba.analyse.extract_tags(content, topK=10)
        tags = str(tags)
        o_news = cls(title=news_ins["title"], category=news_ins["category"], src = news_ins["src"], pic = news_ins["pic"], weburl = news_ins["weburl"], time = timezone.now(), tags = tags)
        o_news.save()
        return o_news
        # except:
        #    print("classmethod ERROR")
        #    return None

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    #required by the auth model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    click_history = models.TextField(default="")
    label = models.TextField(default="")

    def __str__(self):
        return "%s's user profile" %self.user