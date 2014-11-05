from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from aninews.models import NewsItem, EventItem

class NewsFeed(Feed):
    title = "McGill Students' Anime Club News"
    link = "/updates/"
    description = "Latest News and Events from the McGill Students' Anime Club"
    author_name = "McGill Students' Anime Club"
    item_author_name = author_name
    

    def items(self):
        return NewsItem.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.contents_saved

    def item_pubdate(self, item):
        return item.published
