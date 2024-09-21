from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@user_passes_test(is_manager, login_url='/login/')
def index(request):
    return render(request, 'manager.html')
