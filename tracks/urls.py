from django.conf.urls import patterns, url
from tracks.views import TrackListView

urlpatterns = patterns('',
	url(r'^tracks/top/', TrackListView.as_view(), name='track-top'),
)