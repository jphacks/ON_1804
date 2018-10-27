from django.shortcuts import render, get_list_or_404
from .models import TrainingMenu

def menu(request, week_id):
    training_menu = get_list_or_404(TrainingMenu, week=week_id)
    context = {'training_menu': training_menu}
    return render(request, 'training/menu.html', context)
