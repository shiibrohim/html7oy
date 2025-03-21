from django.urls import path
from .views import index, contact, detail, page_404

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('404/', page_404, name='page_404'),
]