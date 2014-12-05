from rest_framework import serializers
from tracks.models import Track


class TrackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Track
		fields = ('name', 'order', 'track_file', 'artist', 'album', )