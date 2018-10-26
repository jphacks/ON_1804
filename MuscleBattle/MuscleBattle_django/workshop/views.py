from django.shortcuts import render

# Create your views here.

def intro(request):
    #introメソッドはintro/index.htmlを起動するぜ
    return render(request, 'intro/index.html')
def syumi(request):
    return render(request, 'syumi/index.html')
def hobby(request):
    return render(request, 'intro/hobby.html')
def shumi(request):
    return render(request, 'shumi/index.html')
