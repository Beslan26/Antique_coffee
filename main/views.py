from django.shortcuts import render, HttpResponseRedirect
from .models import UserContact



# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('message')
        UserContact.objects.create(name=name, email=email, comments=comments)
        return HttpResponseRedirect('usermessage/')

    return render(request, 'main/index.html')


def usermessage(request):
    return render(request, 'main/usermessage.html')


