from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'news/news.html')


def news_detail(request):
    return render(request, 'news/news_detail.html')
