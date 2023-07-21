from django.shortcuts import render,redirect
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def fonctionco(request):
    commandes = Commande.objects.all()

    context = {'commandes': commandes}
    return render(request,'COMMANDE/commande.html', context)


@login_required(login_url='login')
def ajouter_commande(request):
    forms=CommandeForm()
    if request.method=='POST':
        forms=CommandeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context={'forms':forms}
    return render(request,'COMMANDE/ajouter_commande.html',context)


@login_required(login_url='login')
def modifier_commande(request,pk):
    mon_com=Commande.objects.get(id=pk)
    forms=CommandeForm(instance=mon_com)
    if request.method=='POST':
        forms=CommandeForm(request.POST,instance=mon_com)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    context={'forms':forms}
    return render(request,'COMMANDE/ajouter_commande.html',context)





@login_required(login_url='login')
def supprimer_commande(request,pk):
    items=Commande.objects.get(id=pk)
    if request.method=='POST':
        items.delete()
        return redirect('/')

    context={'items':items}
    return render(request,'COMMANDE/supprimer_commande.html',context)



