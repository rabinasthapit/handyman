from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<blogid>[0-9]+)/$',views.blog_details, name='blog_details'),
]
