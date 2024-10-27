from django.http import HttpResponse
from django.shortcuts import render
from .models import Technicians, Testimonials
from django.views.decorators.cache import cache_page


@cache_page(60 * 60 * 24 * 7)
def index_404(request) -> HttpResponse:
    """
    A view for the error page.


    This view simply displays the '404.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered '404.html' template.
    """

    return render(request, '404.html')


def index_team(request) -> HttpResponse:
    """
    A view for the team page.

    This view simply displays the 'team.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered 'team.html' template.
    """

    technicians = Technicians.objects.filter(is_visible=True).order_by('sort')
    context = {
        'technicians': technicians
    }
    return render(request, 'team.html', context=context)


@cache_page(60 * 60 * 24 * 7)
def index_testimonial(request) -> HttpResponse:
    """
    A view for the testimonial page.

    This view simply displays the 'testimonial.html' template.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with rendered 'testimonial.html' template.
    """
    testimonials = Testimonials.objects.filter(is_visible=True).order_by('sort')
    context = {
        'testimonials': testimonials
    }

    return render(request, 'testimonial.html', context=context)
