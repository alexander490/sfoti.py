from django.contrib import admin
from userprofiles.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'avatar', )

admin.site.register(UserProfile, UserProfileAdmin)