from django.conf.urls import url
from .import  views
from django.contrib.auth import views as auth_view


urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^login/',auth_view.login,{'template_name':'login.html'},name='login'),
    url(r'^dashboard/',views.dashboard,name='dashboard'),
    url(r'^logout/',auth_view.logout,{'next_page':'/account/login'},name='logout'),
    url(r'^whoareyou/',views.whoareyou, name='whoareyou'),
    url(r'^employee/',views.employee, name='employee_create'),
    url(r'^skill/',views.skill, name='skill'),
    url(r'^degree/',views.degree,name='degree'),
    url(r'^experience/',views.experience,name='experience'),
    url(r'^cv/',views.cv,name='cv'),
    url(r'^company/',views.company,name='company_create'),
    url(r'^vacancy/',views.vacancy,name='vacancy'),
    url(r'^application/',views.application,name='application'),
    url(r'^companydashboard/',views.companydashboard,name='companydashboard'),
    url(r'^user_update/',views.user_update,name='user_update'),
    url(r'^user_skill/$',views.user_skill,name='user_skill'),
    url(r'^user_skill/(?P<id>[0-9]+)/delete/$',views.user_skill_delete,name='user_skill_delete'),
    url(r'^user_cv/$',views.user_cv,name='user_cv'),
    url(r'^user_cv/(?P<id>[0-9]+)/cv_update/$',views.user_cv_update,name='user_cv_update'),
    url(r'^user_cv/(?P<id>[0-9]+)/delete/$',views.user_cv_delete,name='user_cv_delete'),
    url(r'^user_degree/$',views.user_degree,name='user_degree'),
    url(r'^user_degree/(?P<id>[0-9]+)/delete/$',views.user_degree_delete,name='user_degree_delete'),
    url(r'^user_experience/$',views.user_experience,name='user_experience'),
    url(r'^user_experience/(?P<id>[0-9]+)/delete/$',views.user_experience_delete,name='user_experience_delete'),
    url(r'^add_vacancy/$',views.add_vacancy,name='add_vacancy'),
    url(r'^list_vacancy/$',views.list_vacancy,name='list_vacancy'),
    url(r'^list_vacancy/(?P<id>[0-9]+)/update/$',views.update_vacancy,name='update_vacancy'),
    url(r'^list_vacancy/(?P<id>[0-9]+)/delete/$',views.delete_vacancy,name='delete_vacancy'),
    url(r'^list_vacancy/(?P<id>[0-9]+)/readmore/$',views.readmore_vacancy,name='readmore_vacancy'),





]
