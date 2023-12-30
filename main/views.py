from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Homecare',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст Текст Текст Текст Текст',
    }

    return render(request, 'main/about.html', context)
