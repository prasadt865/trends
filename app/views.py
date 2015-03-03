# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,View,DetailView
from app.forms import SongSearchForm
from .models import Playlist

class root(View):

	def get(self,request):
		form= SongSearchForm(request.GET)
		results= form.search()
		return render(request,'search/search.html',
			{
				'songs' :results
			})


class playlist(View):

	def post(self,request):
		playlist=Playlist(user=request.user,
						  name=request.POST['name'])
		playlist.save()
		return HttpResponseRedirect("/")