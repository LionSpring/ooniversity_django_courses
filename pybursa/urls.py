from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail, course_detail


urlpatterns = patterns('',
    url(r'^$', index, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^students/$', student_list, name='student_list'),
    url(r'^student_detail/(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    url(r'^courses/(?P<course_id>\d+)/$', course_detail, name='course_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)
