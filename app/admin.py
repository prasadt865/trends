from django.contrib import admin
from .models import Song,UserLog,Playlist
admin.autodiscover()
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserLog)