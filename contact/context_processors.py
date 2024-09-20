from .models import ContactInfo
from .forms import SubscriberForm


def contacts(request):
    return {
        'subscriber_form': SubscriberForm(),
        'index_contacts': ContactInfo.objects.first()
    }
