from django.shortcuts import render
from django.views.generic import ListView, DetailView
from aninews.models import NewsItem, EventItem
# Create your views here.

class NewsList(ListView):
    queryset = NewsItem.objects.order_by('-published')
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = NewsItem
    context_object_name = 'item'
