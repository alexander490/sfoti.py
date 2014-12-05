from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('first_name', 'last_name', 'biography', 'favorite_songs', )