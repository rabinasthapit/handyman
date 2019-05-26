from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.company),
    url(r'^iitnepal/$',views.iitnepal),
]
