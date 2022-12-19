from django.urls import path
from .views import *


urlpatterns = [
   path('', NewsList.as_view(), name = 'news_list'),
   path('<str:post_var>/<int:pk>', NewsDetail.as_view(), name = 'news_detail'),
   path('search/', NewsList_Search.as_view()),
   
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]