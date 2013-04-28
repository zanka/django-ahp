from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from ahp.core.views import HomeView, AlgorytmView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^algorytm$', AlgorytmView.as_view(), name='algorithm'),
    
   
)

 # static
urlpatterns += staticfiles_urlpatterns()