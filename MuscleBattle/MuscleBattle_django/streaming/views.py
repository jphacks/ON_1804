from django.shortcuts import render

# Create your views here.

def start_streaming(request):
    return render(request, 'streaming/index.html')
