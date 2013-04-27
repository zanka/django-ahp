from django.conf.urls import patterns, include, url
from django.contrib import admin

from ahp.core.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahp.views.home', name='home'),
    # url(r'^ahp/', include('ahp.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', HomeView.as_view(),name='home')
)
