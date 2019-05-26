"""project2 URL Configuration

    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls')),
    url(r'^account/',include('account.url')),
    url(r'^contact/',views.contactus,name='contactus'),
    url(r'^$',views.home, name='home'),
    url(r'^vacancy/(?P<id>[0-9]+)/$',views.vacancy_details, name='vacancy_details'),
    url(r'^apply/$',views.apply,name='apply'),
    url(r'^professional/',views.professional,name='xyz'),
    url(r'^company/',include('companyprofile.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
