from django.db import models
from django.contrib import admin
from CLIENT.models import Client
from PRODUIT.models import Produit
from STOCK.models import Inventaire

class Commande(models.Model):
    STATUS = (
        ('livraison en cours', 'Livraison en cours'),
        ('non livré', 'Non livré'),
        ('livré', 'Livré')
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, blank=True, null=True)
    montant_total = models.FloatField(editable=False, default=0)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation = models.DateField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.montant_total = self.qty * self.produit.prix
        super(Commande, self).save(*args, **kwargs)

        # Mettre à jour l'inventaire
        inventaire, created = Inventaire.objects.get_or_create(produit=self.produit)
        inventaire.quantite_stock -= self.qty
        inventaire.save()
class ACo(admin.ModelAdmin):
    list_display = ('client','produit','status','date_creation','qty')
    list_filter = ('client','produit',)
