from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from tracks.views import TrackViewSet
from artists.views import ArtistDetailView, ArtistViewSet
from albums.views import AlbumViewSet
from userprofiles.urls import urlpatterns as urls_userprofiles

router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<id>[0-9]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^artist/(?P<pk>[\d]+)/', ArtistDetailView.as_view(), name='artist'),
    url(r'^api/', include(router.urls)),
    url(r'', include('albums.urls')),
)

urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
)

urlpatterns += urls_userprofiles