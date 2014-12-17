from django.contrib import admin
from tracks.models import Track
from sfotipy.actions import export_as_excel

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'artist', 'name', 'order', 'listen', 'album', 'player', 'is_guetta', )
    list_filter = ('artist', 'album', )
    search_fields = ('name', 'artist__first_name', 'artist__last_name', )
    list_editable = ('name', 'album', )
    # actions
    raw_id_fields = ('artist', )
    actions = (export_as_excel, )

    def is_guetta(self, obj):
        return obj.artist.id == 1

    is_guetta.boolean = True

# admin.site.register(Track, TrackAdmin)
