from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    news = News.objects.all()
    context = {
        'news' : news
    }
    return render(request,"hillightfoundation/news.html", context)

