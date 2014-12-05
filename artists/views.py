from django.shortcuts import render
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from artists.models import Artist
from artists.serializers import ArtistSerializer

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'artist'

	def get_template_names(self):
		return 'artist.html'

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer