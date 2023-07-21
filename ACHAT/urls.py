from django.urls import path
from . import views

urlpatterns = [
    path('achat/', views.achat, name="achat"),
]