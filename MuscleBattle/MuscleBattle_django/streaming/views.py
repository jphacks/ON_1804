from django.shortcuts import render
from .models import Room

def start_streaming(request):
    try:
        Room.objects.create(room_hash=list(request.GET.keys())[0])
    except:
        pass
    return render(request, 'streaming/index.html')

def slist_streaming(request):
    room = Room.objects.all()
    context = {'room_list': room}
    return render(request, 'streaming/list.html', context)
