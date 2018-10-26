from django.shortcuts import render

# Create your views here.

def intro(request):
	return render(request,'intro/index.html')

def syumi(request):
	return render(request,'syumi/syumi.html')
