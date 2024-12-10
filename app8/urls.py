from django.urls import path
from app8.views import LatestStudyTableFeed
from django.views.generic import DetailView
from .models import studytable1
from .views import rss_reader

from . import views
app_name="app8"
urlpatterns = [path("", views.homepage, name="homepage"),
               path("path1", views.fun1, name="fun1"),
               path("path2", views.homepage, name="homepage"),
               path("path3", views.send_emails, name="send_emails"),
               path("path4", views.select_data, name="select_data"),
               path("path5", views.comment_list,name="comment_list"),
               path('latest/feed/', LatestStudyTableFeed(), name='latest-studytable-feed'),
               path('studytable/<int:pk>/', DetailView.as_view(model=studytable1, template_name='studytable_detail.html'), name='studytable-detail'),
               path('rss-reader/', rss_reader, name='rss-reader')
               ]