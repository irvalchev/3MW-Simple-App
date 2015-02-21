from django.conf.urls import patterns, include, url
from django.contrib import admin
from site_summary import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.sites, name='sites'),
    url(r'^sites/$', views.sites, name='sites'),
    url(r'^sites/(?P<site_id>\d+)/$', views.site_details, name='site details'),
    url(r'^summary-sum/$', views.summary_sum, name='sum summary'),
    url(r'^summary-average/$', views.summary_average, name='average summary'),
    )
