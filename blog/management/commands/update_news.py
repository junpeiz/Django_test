from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from blog.models import Post, News, UserProfile
from blog.LoadJsonNews import LoadJsonNews
from blog.jisu import jisu
import json

class Command(BaseCommand):

    help = 'Update the news and store it into the database'

    def handle(self, *args, **options):
        # The parameter to control the maximum number of news in database
        max_news_num = 300
        # The parameter to control whether to delete all the news in database
        delete_all_news = 0
        # The parameter to control whether to delete all the users in database
        delete_all_users = 0
        # The parameter to control whether to use the local version
        from_local = 0

        self.stdout.write("Start fetching the news ......")

        if(not from_local):
            # The online version
            news = []
            jisu_collect = jisu()
            ch = ["头条","财经","体育","教育","科技"]
            for channel in ch:
                result = jisu_collect.get_news(channel)
                news = news + result
        else:
            # The read local file version
            news = []
            news_ = LoadJsonNews()
            news_jisu = news_.getnews()
            news = news + news_jisu

        # Delete the news with blank URL
        for temp_news in news:
            if(temp_news["pic"]=="" or temp_news["weburl"]==""):
                news.remove(temp_news)

        # Save the news into the database
        for news_instance in news:
            News.get_and_store(news_instance)

        if(delete_all_news):
            News.objects.all().delete()
        if(delete_all_users):
            User.objects.all().delete()
            UserProfile.objects.all().delete()

        # Control the number of the news in the database
        news_num = News.objects.all().count()
        if(news_num > max_news_num):
            self.stdout.write("The number of news is %d, which exceed the maximal length" % news_num)
            news = News.objects.all().order_by('time')
            for i,temp_news in enumerate(news):
                # print("The date of news to be deleted is", temp_news.time)
                temp_news.delete()
                if((i+1) >= (news_num - max_news_num)):
                    break
        self.stdout.write("Now after deleting, the number of news is %d" % News.objects.all().count())

            