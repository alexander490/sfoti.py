from django.contrib import admin

from albums.models import Album

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_cover', 'artist', )

admin.site.register(Album, AlbumAdmin)