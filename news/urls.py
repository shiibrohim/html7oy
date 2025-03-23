from django.urls import path
from .views import index, contact, detail, page_404, category_detail

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('single_page/<int:pk>/', detail, name='single_page'),
    path('404/', page_404, name='page_404'),
    path('category/<int:pk>/', category_detail, name='ctg'),
]