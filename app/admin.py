from django.contrib import admin
from .models import Song,UserLog
admin.autodiscover()
admin.site.register(Song)
admin.site.register(UserLog)