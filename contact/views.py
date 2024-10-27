from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ContactInfo
from .forms import MessageFromCustomerForm, SubscriberForm
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    """
    A view for the contact page.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'contact.html'.
    """

    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')

        context = {
            'message_form': form,
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'contact.html', context=context)
    else:
        context = {
            'message_form': MessageFromCustomerForm(),
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'contact.html', context=context)


def subscribe(request) -> HttpResponse:
    """
    A view for the subscribe page.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: Response with the rendered template 'subscribe.html'.
    """

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = SubscriberForm()

    return render(request, 'subscribe.html', {'subscriber_form': form})
