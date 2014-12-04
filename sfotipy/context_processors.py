from tracks.models import Track


def menu_tracks(req):
    tracks = Track.objects.all()
    selected_track = None

    for track in tracks:
        if track.get_absolute_url() == req.path:
            selected_track = track

    return {'tracks': tracks, 'selected_track': selected_track, }
