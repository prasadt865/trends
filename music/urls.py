from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from app.models import Song
from app.views import root,playlist
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music.views.home', name='home'),
    # url(r'^music/', include('music.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'', include('social_auth.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', "django.contrib.auth.views.login", {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login",name="logout"),
    url(r'^playlist/', playlist.as_view(),name="playlist"),
    url(r'search/', root.as_view()	,name="search" ),	
    url(r'^', login_required(ListView.as_view(template_name="home.html", model=Song)), name="home")

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

