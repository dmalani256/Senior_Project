from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def register(request):
    
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account is created")
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = UserCreationForm()
    return render(request,'user/register.html',{'form':form})