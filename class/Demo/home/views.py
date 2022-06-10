import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home/home.html')

    


def simple_crawl(request):
    url = "https://https://www1.cycu.edu.tw/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.select('title')
    return render(request, 'home/home.html', locals())
