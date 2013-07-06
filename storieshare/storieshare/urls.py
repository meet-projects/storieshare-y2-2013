from django.conf.urls import patterns, include, url

from stories import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('', url (r'^storieshare/' , views.homepage), 
						url (r'^addstory$' , views.addstory), 
						url (r'^newstory$' , views.newstory),
						url (r'^writtenstory$' , views.writtenstory),
						#url (r'^login$', views.login),
						#url (r'^submitlogin$', views.submitlogin),
						#url (r'^profile$', views.profile),
						url (r'^readstory$' , views.readstory),
						url (r'^readstory/(?P<story_id>\d+)$',views.showstory),
						url (r'^readstory/(?P<story_id>\d+)/newcomment$',views.newcomment),
						url (r'^readstory/(?P<story_id>\d+)/newpara$' , views.newpara),
						url (r'^readstory/(?P<story_id>\d+)/newpara/add$' , views.addpara),
						url (r'^readstory/search$',views.search),
						url (r'^readstory/genre$',views.read_genre),
						url (r'^play$',views.play),
						url (r'^play/add$',views.add_play),
    # Examples:

    # url(r'^$', 'storieshare.views.home', name='home'),
    # url(r'^storieshare/', include('storieshare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
