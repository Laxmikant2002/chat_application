from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'home.html', {'users': users})

@login_required
def chat_view(request, username):
    other_user = User.objects.get(username=username)
    return render(request, 'chat.html', {'other_user': other_user})