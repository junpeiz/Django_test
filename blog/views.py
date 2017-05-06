import json
import random
import ast
import operator
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import News, UserProfile
from .forms import SignUpForm
from .LoadJsonNews import LoadJsonNews
from .jisu import jisu

def news_list(request):
    news = list(News.objects.all())
    random.shuffle(news)
    return render(request, 'blog/news_list.html', {'news': news})

def record_history(request):
    # The Maxmimul length of the user's history and the label of user
    max_history = 100
    max_label = 200
    # The type of news_url is string
    news_url = request.GET.get('next')
    news_click = News.objects.get(pk=news_url)
    news_tags = ast.literal_eval(news_click.tags)
    # Judge if the user is logged in
    if request.user.is_authenticated():
        # Do something for authenticated users.
        current_user = request.user
        print("When click the news, the currently logged in user is: ", current_user.username)
        user = User.objects.get(username=current_user.username)
        user_profile = user.userprofile
        # Add the news url to the history
        if(user_profile.click_history == ""):
            temp_list = []
        else:
            temp_list = ast.literal_eval(user_profile.click_history)
        news_attr = {}
        news_attr["title"] = news_click.title
        news_attr["pic"] = news_click.pic
        news_attr["weburl"] = news_click.weburl
        if(news_attr in temp_list):
            temp_list.remove(news_attr)
        temp_list.append(news_attr)
        if(len(temp_list) > max_history):
            temp_list.pop(0)
        user_profile.click_history = str(temp_list)    
        print("Now the user's history is: ", user_profile.click_history)
        # Add the tag to the user's label
        if(user_profile.label == ""):
            temp_dict = {}
        else:
            temp_dict = ast.literal_eval(user_profile.label)
        for tag in news_tags:
            if(tag not in temp_dict):
                temp_dict[tag] = 1
            else:
                temp_dict[tag] += 1
        if(len(temp_dict) > max_label):
            smallest_label = min(temp_dict, key=temp_dict.get)
            temp_dict.pop(smallest_label, None)
        user_profile.label = str(temp_dict)
        print("Now the user's label is: ", user_profile.label)
        # Save the user's profile
        user_profile.save()
    else:
        # Do something for anonymous users.
        print("When click the news, no user currently logged in")
    # Redirect to the target website of news
    return HttpResponseRedirect(news_url)

def news_recommend(request):
    news = []
    if request.user.is_authenticated():
        news_collect = News.objects.all()
        current_user = request.user
        user = User.objects.get(username=current_user.username)
        if(user.userprofile.label == ""):
            user_label = {}
        else:
            user_label = ast.literal_eval(user.userprofile.label)
        if(user.userprofile.click_history == ""):    
            history_list = []
        else:
            history_list = ast.literal_eval(user.userprofile.click_history)
        similarity_dict = {}
        for news_ins in news_collect:
            visited_flag = 0
            for history_record in history_list:
                if(news_ins.weburl == history_record["weburl"]):
                    visited_flag = 1
            if(visited_flag):
                continue
            news_tags = ast.literal_eval(news_ins.tags)
            temp_similarity = 0
            for tag in news_tags:
                if(tag in user_label):
                    temp_similarity += user_label[tag]
            if(temp_similarity > 0):
                similarity_dict[news_ins] = temp_similarity
        sorted_similarity_dict = sorted(similarity_dict.items(), key=operator.itemgetter(1), reverse=True)
        for it in sorted_similarity_dict:
            news.append(it[0])
    else:
        pass
    return render(request, 'blog/news_recommend.html', {'news': news})

def news_history(request):
    user_history = []
    if request.user.is_authenticated():
        current_user = request.user
        user = User.objects.get(username=current_user.username)
        if(user.userprofile.click_history == ""):
            user_history = []
        else:
            user_history = ast.literal_eval(user.userprofile.click_history)
    else:
        pass
    user_history = reversed(user_history)
    return render(request, 'blog/history.html', {'news': user_history})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and form.clean_email():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Save the corresponding profile automatically when the User is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("The corresponding user_profile is created!")


def contact(request):
    return render(request, 'blog/contact.html')