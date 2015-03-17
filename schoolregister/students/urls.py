from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.details, name='details'),   
)