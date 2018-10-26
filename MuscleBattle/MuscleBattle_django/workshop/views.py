from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request,'intro/index.html')
def hobby(request):
    return render(request, 'intro/hobby.html')
def syumi(request):
    return render(request, 'intro/syumi.html')
