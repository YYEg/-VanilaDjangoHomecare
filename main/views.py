from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Homecare',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст Текст Текст Текст Текст',
    }

    return render(request, 'main/about.html', context)
