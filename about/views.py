from django.http import HttpResponse
from django.shortcuts import render
from .models import About
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request) -> HttpResponse:
    """
    A view for the about page that displays information from the About model.

    This view gets all the About model objects that
    have the is_visible attribute set to True, and passes them in the context
    template 'about.html'.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'about.html'.
    """

    about = About.objects.prefetch_related("features").first()
    return render(request, "about.html", {"about": about})
