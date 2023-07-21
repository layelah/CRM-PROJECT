from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.fonctionpr,name="accueil"),
]
