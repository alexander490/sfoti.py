import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from tracks.models import Track

def track_view(req, name):
	# track = Track.objects.filter(name=name)
	track = get_object_or_404(Track, name=name)

	data = {
		'title': track.name,
		'order': track.order,
		'album': track.album.name,
		'artist': {
			'name': track.artist.first_name,
			'biography': track.artist.biography
		}
	}

	json_data = json.dumps(data)

	# json.loads(string_json)
	return HttpResponse(json_data, content_type='application/json')
	# return render(req, 'track.html', {'track': track})
