from goods.models import Products
from django.contrib.postgres.search import TrigramSimilarity

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.annotate(similarity=TrigramSimilarity('name', query) + TrigramSimilarity('description', query)).filter(similarity__gt=0.2).order_by('-similarity')
