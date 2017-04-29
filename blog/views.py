import json
from random import shuffle
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import News
from .forms import PostForm
from .forms import SignUpForm
from .LoadJsonNews import LoadJsonNews
from .ZhihuDaily import ZhihuDailyFetcher
from .jisu import jisu

# The parameter to control the maximum number of news in database
max_news_num = 500
# The parameter to control whether to delete all the news in database
delete_all = 0
# The parameter to control whether to use the local version
from_local = 0

# Create your views here.
def news_update(request):
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
    shuffle(news)

    # Save the news into the database
    for news_instance in news:
        News.get_and_store(news_instance)

    if(delete_all):
        # Delete all the news from database
        news = News.objects.all()
        for temp_news in news:
            temp_news.delete()

    # Control the number of the news in the database
    news_num = News.objects.all().count()
    if(news_num > max_news_num):
        print("The number of news is ", news_num, ", which exceed the maximal length")
        news = News.objects.all().order_by('time')
        for i,temp_news in enumerate(news):
            print("The date of news to be deleted is", temp_news.time)
            temp_news.delete()
            if((i+1) >= (news_num - max_news_num)):
                break
        print("Now after deleting, the number of news is ", News.objects.all().count())

    return render(request, 'blog/news_update.html', {'news_num': news_num})

def news_list(request):
    news = News.objects.all()
    return render(request, 'blog/news_list.html', {'news': news})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def contact(request):
    return render(request, 'blog/contact.html')