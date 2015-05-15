import json
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render, render_to_response
from symbolsapp.models import Symbol
from haystack.query import SearchQuerySet
from yahoo_finance import Share
# from symbolsapp.forms import SearchForm

def index(request):
    # http://www.maxburstein.com/blog/simple-search-with-django-orm/
    # query = " Django search " #Search query entered by user
    # query = query.split() #Remove excess spaces and split the query into array items
    #
    # from django.db.models import Q
    # compiled = None
    # for word in query:
    # if compiled == None:
    #     compiled = Q(content__icontains=word)
    # else:
    #     compiled = compiled | Q(content__icontains=word)
    #
    # entries = Entry.objects.filter(compiled)
    # from django.db.models import Q
    # compiled = reduce(Q.__or__, [Q(content__icontains=word) for word in query])
    # entries = Entry.objects.filter(compiled)

    symbol_list = Symbol.objects.all()
    context_dict = {'Symbols': symbol_list}

    return render(request, 'symbolsapp/index.html', context_dict)

# def search_symbol(request):
#     symbol = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
#     return render_to_response('symbolsapp/search.html', {'Symbols': symbol})

"""
    Parsing financial data with: https://pypi.python.org/pypi/yahoo-finance/1.1.4
"""
def yahoo(request):
    yahoo = Share('YHOO')
    context_dict = {
        'Data': yahoo.get_historical('2015-04-25', '2015-04-29')
    }
    return render(request, 'symbolsapp/yahoo.html', context_dict)

"""
    http://www.pythoncentral.io/how-to-use-python-django-forms/
"""
# def post_form_upload(request):
#     if request.method == 'GET':
#         form = SearchForm()
#     else:
#         # A POST request: Handle Form Upload
#         form = SearchForm(request.POST) # Bind data from request.POST into a PostForm
#
#         # If data is valid, proceeds to create a new post and redirect the user
#         if form.is_valid():
#             query = form.cleaned_data['query']
#
#
#     return render(request, 'symbolsapp/yahoo.html', {
#         'form': form,
#     })