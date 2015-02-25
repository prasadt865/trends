from haystack import indexes
from django.utils import timezone
from .models import Song

class songIndex(indexes.SearchIndex,indexes.Indexable):
	text= indexes.CharField(document=True,use_template=True)
	title= indexes.CharField(model_attr='title')
	artist= indexes.CharField(model_attr='artist')
	album= indexes.CharField(model_attr='album')
	genre= indexes.CharField(model_attr='genre')

	print text
	def get_model(self):
		return Song

	def index_queryset(self,using=None):
		return self.get_model().objects.all()

		


