from django.http import HttpResponse
from django.shortcuts import render
from .models import Establishment
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request) -> HttpResponse:
    """
    A view for the main page that displays information from the About model.

    This view gets all the Home model objects that
    have the is_visible attribute set to True, and passes them in the context
    template 'home.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'home.html'.
    """

    establishment = Establishment.objects.filter(is_visible=True)

    return render(request, 'home.html', {'establishment': establishment})
