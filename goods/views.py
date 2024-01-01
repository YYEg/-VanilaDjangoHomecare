from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Products


# Create your views here.
def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Каталог",
        "goods":  current_page,
        "slug_url": category_slug,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    prod = Products.objects.get(slug=product_slug)
    context = {
        'product': prod
    }

    return render(request, "goods/product.html", context=context)

