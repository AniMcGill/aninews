from django.conf.urls import patterns, url
from aninews.views import NewsList, NewsDetail
from aninews.feeds import NewsFeed

urlpatterns = patterns('',
    url(r'^$', NewsList.as_view(), name='updates'),
    url(r'^rss/$', NewsFeed(), name='update-rss-feed'),
    url(r'^(?P<pk>\d+)/', NewsDetail.as_view(), name='newsitem-detailed'),
)
