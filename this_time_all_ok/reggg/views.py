from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'reggg/register.html', {'form': form})

# Create your views here.
