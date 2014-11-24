from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from tracks.models import Track

def track_view(req, name):
	# track = Track.objects.filter(name=name)
	track = get_object_or_404(Track, name=name)

	return render(req, 'track.html', {'track': track})
