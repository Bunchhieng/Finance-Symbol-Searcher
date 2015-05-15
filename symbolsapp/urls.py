from django.conf.urls import patterns, url
from symbolsapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^yahoo$', views.yahoo, name='yahoo'),
            )