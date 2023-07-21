
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PRODUIT.urls')),
    path('COMMANDE/', include('COMMANDE.urls')),
    path('CLIENT/', include('CLIENT.urls')),
    path('ACHAT/', include('ACHAT.urls')),
    path('STOCK/', include('STOCK.urls')),
    path('compte/', include('compte.urls')),
    
]