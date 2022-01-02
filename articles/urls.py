from django.urls import path
from django.urls.conf import re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.articles_list, name="list"),
    path('create',views.article_create, name="create"),
    re_path('(?P<slug>[\w-]+)',views.article_details, name="detail")
]