from django.shortcuts import render
from .models import Technicians
from django.views.decorators.cache import cache_page


@cache_page(60 * 60 * 24 * 7)
def index_404(request):
    return render(request, '404.html')


def index_team(request):
    technicians = Technicians.objects.filter(is_visible=True).order_by('sort')
    context = {
        'technicians': technicians
    }
    return render(request, 'team.html', context=context)


@cache_page(60 * 60 * 24 * 7)
def index_testimonial(request):
    return render(request, 'testimonial.html')
