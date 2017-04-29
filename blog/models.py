from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime

# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
# This Post class is a child class of models.Model
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) # for text with a limited number of characters
    text = models.TextField() # for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # When call str(PostX), just return the post's title
        return self.title

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

    @classmethod
    def get_and_store(cls, news_ins):
        # try:
        o_news = cls(title=news_ins["title"], category=news_ins["category"], src = news_ins["src"], pic = news_ins["pic"], weburl = news_ins["weburl"], time = timezone.now())
        o_news.save()
        return o_news
        # except:
        #    print("classmethod ERROR")
        #    return None

    def __str__(self):
        return self.title