from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'user/index.html', context)
