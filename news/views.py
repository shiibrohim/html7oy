from django.shortcuts import render
from .models import Category, News


# Create your views here.

def index(request):
    ctg = Category.objects.all()
    news = News.objects.all().order_by('-date')
    news_lasts = News.objects.all().order_by('-date')
    news_uzb = News.objects.filter(category_id=1)
    news_jahon = News.objects.filter(category_id=2)
    news_iqt = News.objects.filter(category_id=3)
    news_sport = News.objects.filter(category_id=5)
    ctx = {
        'ctg': ctg,
        'news': news,
        'news_lasts': news_lasts[2:],
        'news_uzb': news_uzb,
        'news_jahon': news_jahon,
        'news_iqt': news_iqt,
        'news_sport': news_sport,

    }
    return render(request, 'index.html', ctx)

def detail(request):
    return render(request, 'single_page.html')

def page_404(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')