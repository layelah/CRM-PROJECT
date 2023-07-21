from django.shortcuts import render, get_object_or_404
from COMMANDE.models import Commande
from CLIENT.models import Client
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required(login_url='login')
def fonctionpr(request):
    com_list = Commande.objects.all()
    cli_list = Client.objects.all()

    # Pagination pour les commandes
    com_paginator = Paginator(com_list, 10)  # Divise les commandes en pages avec 10 éléments par page
    com_page_number = request.GET.get('page_com')  # Obtient le numéro de page pour les commandes
    com = com_paginator.get_page(com_page_number)

    # Pagination pour les clients
    cli_paginator = Paginator(cli_list, 10)  # Divise les clients en pages avec 10 éléments par page
    cli_page_number = request.GET.get('page_cli')  # Obtient le numéro de page pour les clients
    cli = cli_paginator.get_page(cli_page_number)

    context = {'com': com, 'cli': cli}
    return render(request, 'PRODUIT/produit.html', context)