from django.contrib import admin
from aninews.models import NewsItem, EventItem
# Register your models here.

admin.site.register(NewsItem)
admin.site.register(EventItem)