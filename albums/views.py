from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from albums.models import Album
from albums.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class JsonResponseMixin(object):

    def response_handler(self, request, *args, **kwargs):
        f = self.request.GET.get('format', None)

        if f == 'json':
            return self.render_json_to_response()

        context = self.get_context_data()
        return self.render_to_response(context)

    def render_json_to_response(self):
        return JsonResponse(self.json_to_response(), safe=False)


class AlbumListView(JsonResponseMixin, ListView):
    model = Album
    paginate_by = None
    template_name = 'album_list.html'

    def json_to_response(self):
        data = [{
            'name': album.name,
            'cover': album.cover.url,
            'slug': album.slug,
            'artist': {
                'first_name': album.artist.first_name,
                'last_name': album.artist.last_name,
                'biography': album.artist.biography,
                'slug': album.artist.slug,
            },
        } for album in self.object_list]

        return data

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        return self.response_handler(request, *args, ** kwargs)

    def get_queryset(self):
        if self.kwargs.get('artist'):
            queryset = self.model.objects.filter(
                artist__slug__contains=self.kwargs['artist'])
        else:
            queryset = super(AlbumListView, self).get_queryset()

        return queryset


class AlbumDetailView(JsonResponseMixin, DetailView):
    model = Album
    template_name = 'album_detail.html'

    def json_to_response(self):
        data = {
            'name': self.object.name,
            'cover': self.object.cover.url,
            'slug': self.object.slug,
            'artist': {
                'first_name': self.object.artist.first_name,
                'last_name': self.object.artist.last_name,
                'biography': self.object.artist.biography,
                'slug': self.object.artist.slug,
            },
            'tracks': [t.name for t in self.object.track_set.all()],
        }

        return data

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        return self.response_handler(request, *args, **kwargs)
