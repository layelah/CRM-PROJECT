from django.db import models
from PRODUIT.models import Produit
from STOCK.models import Inventaire


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.nom


class Achat(models.Model):
    STATUS = (
        ('livraison en cours', 'Livraison en cours'),
        ('non livré', 'Non livré'),
        ('livré', 'Livré')
    )
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, blank=True, null=True)
    montant_total = models.FloatField(editable=False, default=0)
    date_achat = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def save(self, *args, **kwargs):
        self.montant_total = self.qty * self.produit.prix
        super(Achat, self).save(*args, **kwargs)

        # Mettre à jour l'inventaire
        inventaire, created = Inventaire.objects.get_or_create(produit=self.produit)
        if inventaire:
            inventaire.quantite_stock += self.qty
            inventaire.save()
        else:
            raise Exception("L'inventaire n'a pas été créé pour le produit associé à l'achat.")
