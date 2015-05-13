from django.shortcuts import render, render_to_response
from symbolsapp.models import Symbol
from haystack.query import SearchQuerySet

# Create your views here.
def index(request):
    symbol_list = Symbol.objects.all()
    context_dict = {'Symbols': symbol_list}

    return render(request, 'symbolsapp/index.html', context_dict)

def search_symbol(request):
    symbol = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
    return render_to_response('symbolsapp/search.html', {'Symbols': symbol})
