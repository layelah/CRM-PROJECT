from django.db import models
from django.contrib import admin
from django.urls import reverse


class Client(models.Model):
    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    date_creation = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('client', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id']


class AC(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'date_creation')
    list_filter = ('nom',)
