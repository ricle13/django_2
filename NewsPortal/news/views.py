from django.shortcuts import render
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

