from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request, 'intro/index.html')

def shumi(request):
    return render(request, 'intro/shumi.html')
