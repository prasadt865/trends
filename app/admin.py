from django.contrib import admin
from .models import Artist,Album,Song,UserLog
admin.autodiscover()
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(UserLog)