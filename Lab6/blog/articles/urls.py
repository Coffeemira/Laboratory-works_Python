from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)/$', views.get_article, name='get_article'),
]