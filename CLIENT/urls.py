from django.urls import path
from . import views

urlpatterns = [
    path('creation_client', views.creation_client, name="creation"),
    path('<str:pk>', views.fonctioncl, name='client'),
    path('modifier_client/<str:pk>', views.modifier_client, name="modifier"),
    path('supprimer_client/<str:pk>', views.supprimer_client, name="enleve"),
    
]


