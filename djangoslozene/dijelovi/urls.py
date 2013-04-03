from django.conf.urls import patterns, url

from dijelovi import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^supplier/$', views.supplier, name='supplier'),
	url(r'^part/$', views.part, name='part'),
	url(r'^part/(?P<part_id>\d+)/$', views.part_details, name='part_details'),
	url(r'^part/comments/(?P<part_id>\d+)/$', views.part_comments, name='comments'),
)