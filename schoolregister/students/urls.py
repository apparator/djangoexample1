from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.student_listing, name='student_listing'),
    url(r'^(\d+)/$', views.student_details, name='student_details'),
    url(r'^(\d+)/increase_exams$', views.student_increase_exams, name='student_increase_exams'),
)