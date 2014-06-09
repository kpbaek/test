from django.conf.urls import patterns, include, url

from django.contrib import admin
from sample_board import views 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home),
    url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
	url(r'^searchWithSubject$', views.searchWithSubject),
    url(r'^listSearchedSpecificPageWork/$', views.listSearchedSpecificPageWork),
    url(r'^show_write_form/$', views.show_write_form),
    url(r'^DoWriteBoard$', views.DoWriteBoard),
    url(r'^viewWork/$', views.viewWork),
    url(r'^listSpecificPageWork_to_update/$', views.listSpecificPageWork_to_update),
    url(r'^updateBoard$', views.updateBoard),
	url(r'^DeleteSpecificRow$', views.DeleteSpecificRow),
)
