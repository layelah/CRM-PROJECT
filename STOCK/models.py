from django.db import models
from PRODUIT.models import Produit
from django.contrib import admin

# Create your models here.
class Inventaire(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    quantite_stock = models.FloatField(default=0)

    def __str__(self):
        return str(self.produit)

    def mettre_a_jour_quantite_stock(self):
        self.produit.quantite_stock = self.quantite_stock
        self.produit.save()


class AI(admin.ModelAdmin):
    list_display = ('produit','quantite_stock')
    list_filter = ['produit']