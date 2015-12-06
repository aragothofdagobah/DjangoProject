from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'puppys.views.index'),
    url(r'^contact/', 'puppys.views.contact'),
    url(r'^about/', 'puppys.views.about'),
    url(r'^ShihTzu/', 'puppys.views.shihTzu'),
    url(r'^ToyPoodle/', 'puppys.views.toyPoodle'),
    url(r'^admin/', include(admin.site.urls)),
]
