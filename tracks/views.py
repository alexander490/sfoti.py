import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from tracks.models import Track


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

    try:
        track = Track.objects.get(pk=id)
    except Track.DoesNotExist:
        track = None

    json_data = serializers.serialize('json', [track, ],
                                 indent=4,
                                 use_natural_foreign_keys=True,
                                 use_natural_primary_keys=True)

    return HttpResponse(json_data, content_type='application/json')
    # return render(req, 'track.html', {'track': track})
