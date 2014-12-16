from django.contrib import admin

from artists.models import Artist
from albums.models import Album
from tracks.models import Track


class TrackInline(admin.StackedInline):
    model = Track
    extra = 1


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'biography', )
    search_fields = ('first_name', 'last_name', )
    filter_horizontal = ('favorite_songs', )
    # filter_vertical = ('favorite_songs', )
    inlines = [TrackInline, AlbumInline, ]
    readonly_fields = ('slug', )

admin.site.register(Artist, ArtistAdmin)
