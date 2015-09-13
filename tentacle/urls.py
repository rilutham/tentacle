from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<activity_id>[0-9]+)/delete/$', views.delete_activity, name='delete'),
        ]
