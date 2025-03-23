from datetime import date

from django.shortcuts import render
from .models import Category, News, Sponsor

def get_date():
    return date.today()

def get_category():
    return Category.objects.all()


def index(request):
    news = News.objects.all().order_by('-date')
    news_lasts = News.objects.all().order_by('-date')
    news_uzb = News.objects.filter(category_id=1)
    news_jahon = News.objects.filter(category_id=2)
    news_iqt = News.objects.filter(category_id=3)
    news_sport = News.objects.filter(category_id=5)
    news_sponsor = Sponsor.objects.filter()
    popular_news = News.objects.all().order_by('views')
    ctx = {
        'ctg': get_category,
        'news': news,
        'news_lasts': news_lasts[2:],
        'news_uzb': news_uzb,
        'news_jahon': news_jahon,
        'news_iqt': news_iqt,
        'news_sport': news_sport,
        'news_sponsor': news_sponsor,
        'date': get_date(),
        'popular_news': popular_news[:4],


    }
    return render(request, 'index.html', ctx)

def detail(request, pk):
    new = News.objects.get(pk=pk)
    news = News.objects.filter(category__name=new.category).order_by('-date')
    popular_news = News.objects.filter(category__name=new.category).order_by('views')
    news_sponsor = Sponsor.objects.filter()
    new.views += 1
    new.save()
    ctx = {
        'new': new,
        'ctg': get_category,
        'date': get_date(),
        'news': news[:4],
        'popular_news': popular_news[:4],
        'news_sponser': news_sponsor,

    }
    return render(request, 'single_page.html', ctx)

def page_404(request):
    ctx = {
        'date': get_date(),
    }
    return render(request, '404.html', ctx)

def contact(request):
    ctx = {
        'date': get_date(),
    }
    return render(request, 'contact.html', ctx)

def category_detail(request, pk):
    ctg = Category.objects.get(id=pk)
    news = News.objects.filter(category__name=ctg.name).order_by('-date')
    ctx = {
        'ctg': get_category(),
        'news': news,
        'date': get_date(),

    }
    return render(request, 'category.html', ctx)
