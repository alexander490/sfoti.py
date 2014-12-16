from django.contrib import admin

from albums.models import Album

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_cover', 'slug', 'artist', )
	readonly_fields = ('slug', )

admin.site.register(Album, AlbumAdmin)