from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from  pepito import views
from .views import about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns  += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
