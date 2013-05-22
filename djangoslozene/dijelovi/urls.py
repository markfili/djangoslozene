from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from dijelovi import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^supplier/(?P<supplier_id>\d+)/$', views.supplier, name='supplier'),
	url(r'^part/$', views.part, name='part'),
	url(r'^part/(?P<part_id>\d+)/$', views.part_details, name='part_details'),
	url(r'^part/comments/(?P<part_id>\d+)/$', views.part_comments, name='comments'),
	url(r'^category/(?P<category_id>\d+)/$', views.part_category, name='part_category'),
	url(r'^part/bulk_upload/$', views.bulk_upload, name='bulk_upload'),
	url(r'^search/$', views.search, name='search'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register_view, name='register'),
	url(r'^register_success/$', views.register_success_view, name="register_success"),
)
