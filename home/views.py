from django.shortcuts import render
from .models import Establishment
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    establishment = Establishment.objects.filter(is_visible=True)
    context = {
        'establishment': establishment,
    }
    return render(request, 'home.html', context=context)
