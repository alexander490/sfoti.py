from django.conf.urls import url, patterns
from albums.views import AlbumListView, AlbumDetailView

urlpatterns = patterns('',
	url(r'^albums/$', AlbumListView.as_view(), name='album-list'),
	url(r'^albums/(?P<artist>[\w-]+)/$', AlbumListView.as_view(), name='album-list'),
	url(r'^albums/detail/(?P<slug>[\w-]+)/$', AlbumDetailView.as_view(), name='album-detail'),
)