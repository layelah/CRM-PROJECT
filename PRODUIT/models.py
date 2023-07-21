from django.db import models
from django.contrib import admin


class Unite(models.Model):
    titre = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.titre


class Tags(models.Model):
    nom = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    unite = models.ForeignKey(Unite, null=True, on_delete=models.CASCADE)
    prix = models.FloatField(null=True)
    quantite_stock = models.FloatField(default=0)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.nom


class AP(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    list_filter = ('nom',)
    filter_horizontal = ('tags',)
