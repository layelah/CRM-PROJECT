from django.shortcuts import render
from .forms import formulaire_inscription
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def page_inscription(request):
    form = formulaire_inscription()
    if request.method=='POST':
        form = formulaire_inscription(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"compte créé avec succès pour "+ user)
            return HttpResponseRedirect('http://127.0.0.1:8000/compte/login')

    context={'form':form}
    return render(request,"compte/inscription.html",context)






def page_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
            messages.info(request,"il y a une erreur sur le nom d'utilisateur et/ou le mot de passe")
    return render(request,"compte/login.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/compte/login')