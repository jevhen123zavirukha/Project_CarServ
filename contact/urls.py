from django.urls import path
from .views import index

app_name = 'contact'

urlpatterns = [
    path('', index, name='contact'),
]
