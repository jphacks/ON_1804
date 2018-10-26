from django.shortcuts import render

def intro(request):
    return render(request, 'intro/index.html')

def syumi(request):
    return render(request, 'intro/syumi.html')

