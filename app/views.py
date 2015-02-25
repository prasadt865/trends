# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import SongSearchForm

def root(request):
    """
    Search > Root
    """

    # we retrieve the query to display it in the template
    form = SongSearchForm(request.GET) 	  	
    # we call the search method from the NotesSearchForm. Haystack do the work!
    results = form.search()
   	
    return render(request, 'search/search.html', {
   
        'songs' : results,
    })