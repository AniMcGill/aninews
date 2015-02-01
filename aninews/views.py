from django.shortcuts import render
from django.views.generic import ListView, DetailView
from aninews.models import NewsItem, EventItem
from django.views.generic.dates import MonthArchiveView
from django.utils import timezone
import calendar

# Create your views here.


class NewsList(ListView):
    queryset = NewsItem.objects.order_by('-published')
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = NewsItem
    context_object_name = 'item'


class CalendarView(MonthArchiveView):
    allow_future = True
    allow_empty = True
    model = EventItem
    date_field = 'when'