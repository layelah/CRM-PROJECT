from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientForm
from COMMANDE.filters import CommandeFilter
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def fonctioncl(request,pk):
    clix = Client.objects.get(id=pk)
    ccoommaa = clix.commande_set.all()
    commande_total = ccoommaa.count()
    mon_filtre=CommandeFilter(request.GET,queryset=ccoommaa)
    ccoommaa=mon_filtre.qs

    context={'clix':clix,'ccoommaa':ccoommaa,'commande_total':commande_total,'mon_filtre':mon_filtre}
    return render(request,'CLIENT/client.html',context)


@login_required(login_url='login')
def creation_client(request):
    forms=ClientForm()
    if request.method=='POST':
        forms=ClientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context={'forms':forms}
    return render(request,'CLIENT/creation_client.html',context)


@login_required(login_url='login')
def supprimer_client(request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/')

    context={'client':client}
    return render(request,'CLIENT/supprimer_client.html',context)

@login_required(login_url='login')
def modifier_client(request,pk):
    client=Client.objects.get(id=pk)
    forms=ClientForm(instance=client)
    if request.method=='POST':
        forms=ClientForm(request.POST,instance=client)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context={'forms':forms}
    return render(request,'CLIENT/creation_client.html',context)