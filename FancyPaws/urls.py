from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'puppys.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
