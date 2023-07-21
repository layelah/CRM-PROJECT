from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.fonctionco, name="commande"),
    path('ajouter_commande',views.ajouter_commande,name="ajouter"),
    path('modifier_commande/<str:pk>',views.modifier_commande,name="update"),
    path('supprimer_commande/<str:pk>',views.supprimer_commande,name="delete"),
    
]