from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from ahp.core.views import HomeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahp.views.home', name='home'),
    # url(r'^ahp/', include('ahp.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', HomeView.as_view(), name='home')
    
   
)

 # static
urlpatterns += staticfiles_urlpatterns()