from django.shortcuts import render
from .models import Service
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    categories = Service.objects.filter(is_visible=True)
    context = {
        'categories': categories,
    }
    return render(request, 'service.html', context=context)
