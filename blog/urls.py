from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #only an empty string will match
    url(r'^$', views.news_list, name='news_list'), 
    # URL for recording the history
    url(r'^record/', views.record_history, name='record_history'), 
    # URL for recommending the news
    url(r'^news_recommend/', views.news_recommend, name='news_recommend'),
    # URL for recording the history
    url(r'^history/', views.news_history, name='history'), 
    # URL for updating the news
    # url(r'^news_update/$', views.news_update, name='news_update'),
    # URL for post in blog
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # URL for sign up
    url(r'^signup/$', views.signup, name='signup'),
    # URL for log in and log out
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # URL for reset the password
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # URL for contact information
    url(r'^contact/$', views.contact, name='contact'),
]