from haystack.forms import SearchForm

class SongSearchForm(SearchForm):
	
	def no_query_found(self):
		return self.searchqueryset.all()

	def search(self):
		sqs= super(SongSearchForm,self).search()

		if not self.is_valid():
			return self.no_query_found()

		sqs= sqs.order_by('title')

		return sqs

