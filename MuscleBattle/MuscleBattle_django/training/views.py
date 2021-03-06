from django.shortcuts import render, get_list_or_404
from .models import TrainingMenu
from django.db.models import Q
import uuid

def menu(request, week_id):
    try:
        training_menu = TrainingMenu.objects.filter(Q(week1=week_id) | Q(week2=week_id))
    except TrainingMenu.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'training_menu': training_menu}
    return render(request, 'training/menu.html', context)

def select(request):
    context = {'hash_n': uuid.uuid4().hex}
    return render(request, 'training/select.html', context)
