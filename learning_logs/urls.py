"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),  # r'^$' means nothing between beginning and end (empty)

    # Show all topics
    url(r'^topics/$', views.topics, name = 'topics'),

    #Details page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')  # matches integer between 2 slashes and stores it in topic_id
]
