from haystack import indexes
from .models import Symbol

class SymbolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    symbol = indexes.CharField(model_attr='symbol')

    content_auto = indexes.EdgeNgramField(model_attr='symbol')

    def get_model(self):
        return Symbol

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
