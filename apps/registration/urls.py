from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^login$', views.login),
	url(r'^success/(?P<id>\d+)$', views.success)
]