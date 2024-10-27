from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request) -> HttpResponse:
    """
    A view for the service page that displays information from the Service model.

    This view gets all the Service model objects that
    have the is_visible attribute set to True and pass them in the context
    template 'service.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'service.html'.
    """

    services = Service.objects.filter(is_visible=True)
    return render(request, 'service.html', {'services': services})
