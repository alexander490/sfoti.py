import json
import time
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from tracks.models import Track
from tracks.serializers import TrackSerializer
from sfotipy.tasks import demorada


@cache_page(60)
@login_required
def track_view(req, id):
    # track = get_object_or_404(Track, pk=id)

    # data = {
    #     'title': track.name,
    #     'order': track.order,
    #     'album': track.album.name,
    #     'artist': {
    #         'name': track.artist.first_name,
    #         'biography': track.artist.biography
    #     }
    # }

    # json_data = json.dumps(data)
    # json.loads(string_json)

    track = cache.get('data_track_{id}'.format(id=id))
    if track is None:
        try:
            track = Track.objects.get(pk=id)
            cache.set('data_track_{id}'.format(id=id), track)
        except Track.DoesNotExist:
            track = None
        time.sleep(5)

    # json_data = serializers.serialize('json', [track, ],
    #                              indent=4,
    #                              use_natural_foreign_keys=True,
    #                              use_natural_primary_keys=True)

    # return HttpResponse(json_data, content_type='application/json')

    demorada.apply_async(countdown=10, expires=20)
    return render(req, 'track.html', {'track': track})


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
