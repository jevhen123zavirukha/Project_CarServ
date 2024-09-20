from django.shortcuts import render
from .models import About
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    about = About.objects.filter(is_visible=True)
    context = {
        'about': about,
    }
    return render(request, 'about.html', context=context)
